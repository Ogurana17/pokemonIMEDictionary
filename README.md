# Pokemon IME Dictionary

![Dec-19-2022 10-09-40](https://user-images.githubusercontent.com/36149909/208329894-553013c3-cead-442e-bbe6-19a32d0d74c6.gif)

ポケモンの名前を簡単に出せるようにする辞書。
`特性`,`木の実`,`アイテム`,`技`,`性格`も用意しました。

Googleスプレッドシートで強引に作成しています。
<https://drive.google.com/drive/folders/1oKhRNsdcKU27HQ4VobmATZQvXWYdvYtm>

## 導入

1. <https://github.com/Ogurana17/pokemonIMEDictionary/archive/refs/heads/main.zip>からダウンロード
2. ダウンロードしたファイルを解凍します。

### Google 日本語入力

1. Google日本語入力の辞書ツールを開く
2. 管理をクリック
3. 新規辞書にインポートをクリック
4. ファイルを選択からインストールしたい`txt`ファイルを選択
5. 適当な辞書名をつける
6. インポートをクリック

### Microsoft IME

1. ユーザー辞書ツールを開く
2. ツールをクリック
3. ツール→一覧の出力で現在の辞書をバックアップ
4. ユーザー辞書ツールのツールをクリック
5. テキストファイルからの登録をクリック
6. ファイルを選択からインストールしたい`txt`ファイルを選択
7. OKをクリック

### Macユーザー辞書

現在の辞書をバックアップしてからインストールしたい`plist`をドラック＆ドロップ
（[公式案内](https://support.apple.com/ja-jp/guide/japanese-input-method/jpim10228/mac#:~:text=%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E3%81%97%E3%81%BE%E3%81%99%E3%80%82-,%E3%83%A6%E3%83%BC%E3%82%B6%E8%BE%9E%E6%9B%B8%E3%82%92%E6%9B%B8%E3%81%8D%E5%87%BA%E3%81%99/%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%82%80,-Mac%E3%81%A7%E3%80%81)）

## 以下の通り変換できます

### ポケモンの名前

| 変換元   | 変換先  |
| ----- | ---- |
| ひらがな  | カタカナ |
| ひらがな  | 英語   |
| 図鑑No. | カタカナ |
| 図鑑No. | 英語   |

#### 例

| 変換元  | 変換先    |
| ---- | ------ |
| えーふぃ | エーフィ   |
| えーふぃ | Espeon |
| 196p | エーフィ   |
| 196p | Espeon |

**姿違い（フォルムチェンジ）は更新処理が煩雑なので廃止。**

## データ元

- <https://wiki.xn--rckteqa2e.com/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8>
