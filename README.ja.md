# Codex ちいかわペット

[English](README.md) · [한국어](README.ko.md) · 日本語

![ちいかわのドット絵ペット8種類と、英語・日本語・韓国語の名前。](showcase/thumbnail.png)

Codex デスクトップアプリ向けのファンメイドのドット絵ペット8種類です。それぞれ9種類の動きと16方向の視線に対応しています。[アニメーションを見る](showcase/chiikawa-pets.gif)

## ダウンロード

[日本語 ZIP](https://github.com/tac0de/codex-chiikawa-pets/releases/download/chiikawa-v1.1.0/chiikawa-codex-pets-ja.zip) · [英語 ZIP](https://github.com/tac0de/codex-chiikawa-pets/releases/download/chiikawa-v1.1.0/chiikawa-codex-pets-en.zip) · [韓国語 ZIP](https://github.com/tac0de/codex-chiikawa-pets/releases/download/chiikawa-v1.1.0/chiikawa-codex-pets-ko.zip)

1. 好きな言語の ZIP を1つダウンロードして展開します。どの ZIP にも8種類すべて入っています。
2. ペットのフォルダー8個を `~/.codex/pets/` にコピーします。Windows では `%USERPROFILE%\.codex\pets\` です。`CODEX_HOME` を設定している場合は、その下の `pets` フォルダーを使います。
3. Codex の **Settings → Appearance → Pets** を開きます。ペットが表示されなければ、アプリを再起動してください。

<details>
<summary>1コマンドでインストール</summary>

macOS または Linux では Python 3 を使います。

```sh
curl -fsSL https://raw.githubusercontent.com/tac0de/codex-chiikawa-pets/chiikawa-v1.1.0/install_pets.py | python3 - --lang ja
```

Windows PowerShell では Python ランチャー `py` を使います。

```powershell
Invoke-RestMethod https://raw.githubusercontent.com/tac0de/codex-chiikawa-pets/chiikawa-v1.1.0/install_pets.py | py - --lang ja
```

インストーラーは ZIP のチェックサムを検証し、内容が異なる既存のペットフォルダーは保持します。[インストーラーのソース](install_pets.py)

</details>

## クレジット

非公式のファンプロジェクトです。ちいかわとキャラクターの原作者はナガノ（©nagano）です。[MIT ライセンス](LICENSE)は Python ツールに適用されます。キャラクターの権利はそれぞれの権利者に帰属します。[公式キャラクター情報](https://spiralcute.com/characters/chiikawa/)

[リリース](https://github.com/tac0de/codex-chiikawa-pets/releases) · [ペット制作ツール](TOOLS.md)
