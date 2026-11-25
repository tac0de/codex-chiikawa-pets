# Chiikawa Pets for Codex

English · [한국어](README.ko.md) · [日本語](README.ja.md)

![Eight Chiikawa pixel pets in two rows, with their names in English, Japanese, and Korean.](showcase/thumbnail.png)

Eight fan-made pixel pets for the Codex desktop app. Each has nine animations and 16 gaze directions. [Watch the animated preview](showcase/chiikawa-pets.gif)

## Download

[English ZIP](https://github.com/tac0de/codex-chiikawa-pets/releases/download/chiikawa-v1.1.0/chiikawa-codex-pets-en.zip) · [한국어 ZIP](https://github.com/tac0de/codex-chiikawa-pets/releases/download/chiikawa-v1.1.0/chiikawa-codex-pets-ko.zip) · [日本語 ZIP](https://github.com/tac0de/codex-chiikawa-pets/releases/download/chiikawa-v1.1.0/chiikawa-codex-pets-ja.zip)

1. Download and unzip one pack. Each pack contains all eight pets.
2. Copy the eight pet folders into `~/.codex/pets/` (Windows `%USERPROFILE%\.codex\pets\`). Create the folder if needed. If you set `CODEX_HOME`, use its `pets` folder.
3. Open **Settings → Appearance → Pets** in Codex. Restart Codex if the pets do not appear.

<details>
<summary>Install with one command</summary>

macOS or Linux with Python 3

```sh
curl -fsSL https://raw.githubusercontent.com/tac0de/codex-chiikawa-pets/chiikawa-v1.1.0/install_pets.py | python3 -
```

Windows PowerShell with the Python launcher

```powershell
Invoke-RestMethod https://raw.githubusercontent.com/tac0de/codex-chiikawa-pets/chiikawa-v1.1.0/install_pets.py | py -
```

Append `--lang ko` or `--lang ja` to install Korean or Japanese names. The installer verifies the ZIP checksum and preserves existing pet folders with different files. [Installer source](install_pets.py)

</details>

## Credits

Unofficial fan project. Chiikawa and its characters are by Nagano (©nagano). The [MIT License](LICENSE) covers the Python tools. Character rights remain with their respective holders. [Official character credits](https://spiralcute.com/characters/chiikawa/)

[Releases](https://github.com/tac0de/codex-chiikawa-pets/releases) · [Pet-making tools](TOOLS.md)
