#!/usr/bin/env python3
"""Install the existing Chiikawa pet pack using only Python's standard library."""

import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import sys
import tempfile
from urllib.error import URLError
from urllib.request import urlopen
from zipfile import BadZipFile, ZipFile

RELEASE = "https://github.com/tac0de/codex-pet-tools/releases/download/chiikawa-v1.0.0"
CHECKSUMS = {
    "en": "fe7a0ba66a20b074c20c6e87e7f2eff0f34b6fb63f4f7d17de427a2d4e4f03a6",
    "ja": "3d5d2b000b16c67bea5c9e4a239f87d28033879d50b385b8a0f19f7147533e21",
    "ko": "cbcb7a279f6c53d3b7c507143a710f916cec2329fe88a9c43aecf7d67b142dec",
}
PET_IDS = ("chiikawa", "chiikawa-usagi", "furuhonya", "hachiware",
           "kurimanju", "momonga", "rakko", "shisa")
FILES = {"pet.json": 8192, "spritesheet.webp": 4 * 1024 * 1024}
MAX_DOWNLOAD = 16 * 1024 * 1024


def load_pack(language, archive):
    if archive is None:
        url = f"{RELEASE}/chiikawa-codex-pets-{language}.zip"
        with urlopen(url, timeout=60) as response:
            data = response.read(MAX_DOWNLOAD + 1)
    else:
        with archive.open("rb") as source:
            data = source.read(MAX_DOWNLOAD + 1)
    if len(data) > MAX_DOWNLOAD or hashlib.sha256(data).hexdigest() != CHECKSUMS[language]:
        raise ValueError(f"The ZIP does not match the published {language} pack checksum.")
    return data


def read_pets(data):
    pets = {pet_id: {} for pet_id in PET_IDS}
    with ZipFile(io.BytesIO(data)) as package:
        for entry in package.infolist():
            parts = PurePosixPath(entry.filename).parts
            if len(parts) < 2 or parts[-2] not in pets or parts[-1] not in FILES:
                continue
            pet_id, name = parts[-2:]
            target = pets[pet_id]
            if name in target or entry.file_size > FILES[name]:
                raise ValueError(f"Unexpected {name} in the {pet_id} package.")
            # Read only the known members. Archive paths never decide output paths.
            target[name] = package.read(entry)
    for pet_id, files in pets.items():
        if files.keys() != FILES.keys():
            raise ValueError(f"Incomplete package for {pet_id}.")
        manifest = json.loads(files["pet.json"])
        if (not isinstance(manifest, dict) or manifest.get("id") != pet_id or manifest.get("spriteVersionNumber") != 2
                or manifest.get("spritesheetPath") != "spritesheet.webp"
                or not manifest.get("displayName") or not manifest.get("description")):
            raise ValueError(f"Invalid pet manifest for {pet_id}.")
        image = files["spritesheet.webp"]
        if image[:4] != b"RIFF" or image[8:12] != b"WEBP":
            raise ValueError(f"Invalid spritesheet format for {pet_id}.")
    return pets


def install_pets(pets, directory):
    directory.mkdir(parents=True, exist_ok=True)
    skipped = []
    with tempfile.TemporaryDirectory(prefix=".chiikawa-", dir=directory) as staging:
        for pet_id, files in pets.items():
            destination = directory / pet_id
            if destination.exists() or destination.is_symlink():
                if (not destination.is_symlink() and destination.is_dir()
                        and all((destination / name).is_file()
                                and not (destination / name).is_symlink()
                                and (destination / name).stat().st_size == len(data)
                                and (destination / name).read_bytes() == data
                                for name, data in files.items())):
                    print(f"Already installed {pet_id}")
                else:
                    skipped.append(pet_id)
                continue
            prepared = Path(staging) / pet_id
            prepared.mkdir()
            for name, data in files.items():
                (prepared / name).write_bytes(data)
            prepared.rename(destination)
            print(f"Installed {pet_id}")
    return skipped


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lang", choices=tuple(CHECKSUMS), default="en", help="Pack language")
    parser.add_argument("--archive", type=Path, help="Use a previously downloaded official ZIP")
    parser.add_argument("--pets-dir", type=Path, help="Override the destination pets directory")
    args = parser.parse_args(argv)
    codex_home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex").expanduser()
    directory = (args.pets_dir or codex_home / "pets").expanduser()
    try:
        skipped = install_pets(read_pets(load_pack(args.lang, args.archive)), directory)
    except (BadZipFile, OSError, URLError, ValueError) as error:
        print(f"Installation stopped: {error}", file=sys.stderr)
        return 1
    if skipped:
        print("Preserved existing folders with different files: " + ", ".join(skipped), file=sys.stderr)
        return 1
    print(f"Eight pets are ready in {directory}. Use Settings > Appearance > Pets in Codex.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
