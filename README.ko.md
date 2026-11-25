# 코덱스 치이카와 펫

[English](README.md) · 한국어 · [日本語](README.ja.md)

![치이카와 픽셀 펫 8종과 캐릭터별 한·영·일 이름.](showcase/thumbnail.png)

Codex 데스크톱 앱에서 쓸 수 있는 팬메이드 픽셀 펫 8종입니다. 각 캐릭터에 동작 9종과 시선 16방향이 들어 있습니다. [움직이는 미리보기](showcase/chiikawa-pets.gif)

## 다운로드

[한국어 ZIP](https://github.com/tac0de/codex-chiikawa-pets/releases/download/chiikawa-v1.1.0/chiikawa-codex-pets-ko.zip) · [영어 ZIP](https://github.com/tac0de/codex-chiikawa-pets/releases/download/chiikawa-v1.1.0/chiikawa-codex-pets-en.zip) · [일본어 ZIP](https://github.com/tac0de/codex-chiikawa-pets/releases/download/chiikawa-v1.1.0/chiikawa-codex-pets-ja.zip)

1. 원하는 언어 ZIP 하나를 받아 압축을 풉니다. 어느 팩이든 펫 8종이 들어 있습니다.
2. 캐릭터 폴더 8개를 `~/.codex/pets/`에 복사합니다. Windows는 `%USERPROFILE%\.codex\pets\`입니다. `CODEX_HOME`을 설정했다면 그 아래의 `pets` 폴더를 씁니다.
3. Codex에서 **설정 → 모양 → 펫**을 엽니다. 펫이 보이지 않으면 앱을 다시 엽니다.

<details>
<summary>명령 한 번으로 설치</summary>

macOS 또는 Linux에서 Python 3을 사용합니다.

```sh
curl -fsSL https://raw.githubusercontent.com/tac0de/codex-chiikawa-pets/chiikawa-v1.1.0/install_pets.py | python3 - --lang ko
```

Windows PowerShell에서는 Python 실행기 `py`를 사용합니다.

```powershell
Invoke-RestMethod https://raw.githubusercontent.com/tac0de/codex-chiikawa-pets/chiikawa-v1.1.0/install_pets.py | py - --lang ko
```

설치기는 ZIP 체크섬을 확인하고 같은 이름에 다른 파일이 있으면 보존합니다. [설치기 소스](install_pets.py)

</details>

## 크레딧

비공식 팬 프로젝트입니다. 치이카와와 캐릭터의 원작자는 나가노(©nagano)입니다. [MIT 라이선스](LICENSE)는 Python 도구에 적용됩니다. 캐릭터 권리는 각 권리자에게 있습니다. [공식 캐릭터 크레딧](https://spiralcute.com/characters/chiikawa/)

[릴리스](https://github.com/tac0de/codex-chiikawa-pets/releases) · [펫 제작 도구](TOOLS.md)
