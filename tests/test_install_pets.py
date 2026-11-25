import contextlib
import hashlib
import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from zipfile import ZipFile

import install_pets as installer


def fixture_pack(missing=None):
    buffer = io.BytesIO()
    with ZipFile(buffer, "w") as archive:
        for pet_id in installer.PET_IDS:
            archive.writestr(f"pack/{pet_id}/pet.json", json.dumps({
                "id": pet_id, "spriteVersionNumber": 2, "spritesheetPath": "spritesheet.webp",
                "displayName": pet_id, "description": "A fixture pet.",
            }))
            if pet_id != missing:
                archive.writestr(f"pack/{pet_id}/spritesheet.webp", b"RIFF....WEBP")
        archive.writestr("../outside", "unused member")
    return buffer.getvalue()


class InstallPetsTest(unittest.TestCase):
    def test_all_pets_install_and_retry_preserves_a_modified_pet(self):
        data = fixture_pack()
        with TemporaryDirectory() as scratch, contextlib.redirect_stdout(io.StringIO()):
            root = Path(scratch)
            zip_path = root / "pack.zip"
            zip_path.write_bytes(data)
            with patch.dict(installer.CHECKSUMS, en=hashlib.sha256(data).hexdigest()):
                self.assertEqual(installer.main(["--archive", str(zip_path), "--pets-dir", str(root / "pets")]), 0)
            pets = root / "pets"
            self.assertEqual({path.name for path in pets.iterdir()}, set(installer.PET_IDS))
            self.assertFalse((root / "outside").exists())
            self.assertEqual(installer.install_pets(installer.read_pets(data), pets), [])
            local = pets / "chiikawa" / "pet.json"
            local.write_bytes(b"existing user content")
            self.assertEqual(installer.install_pets(installer.read_pets(data), pets), ["chiikawa"])
            self.assertEqual(local.read_bytes(), b"existing user content")

    def test_bad_or_incomplete_archive_is_rejected(self):
        with TemporaryDirectory() as scratch:
            path = Path(scratch) / "corrupt.zip"
            path.write_bytes(b"corrupt")
            with self.assertRaisesRegex(ValueError, "checksum"):
                installer.load_pack("en", path)
        with self.assertRaisesRegex(ValueError, "Incomplete package"):
            installer.read_pets(fixture_pack(missing="shisa"))


if __name__ == "__main__":
    unittest.main()
