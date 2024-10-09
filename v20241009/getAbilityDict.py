import requests
from bs4 import BeautifulSoup

# カタカナからひらがなへの変換辞書（小文字含む）
katakana_to_hiragana_dict = {
    "ア": "あ", "イ": "い", "ウ": "う", "エ": "え", "オ": "お",
    "カ": "か", "キ": "き", "ク": "く", "ケ": "け", "コ": "こ",
    "サ": "さ", "シ": "し", "ス": "す", "セ": "せ", "ソ": "そ",
    "タ": "た", "チ": "ち", "ツ": "つ", "テ": "て", "ト": "と",
    "ナ": "な", "ニ": "に", "ヌ": "ぬ", "ネ": "ね", "ノ": "の",
    "ハ": "は", "ヒ": "ひ", "フ": "ふ", "ヘ": "へ", "ホ": "ほ",
    "マ": "ま", "ミ": "み", "ム": "む", "メ": "め", "モ": "も",
    "ヤ": "や", "ユ": "ゆ", "ヨ": "よ",
    "ラ": "ら", "リ": "り", "ル": "る", "レ": "れ", "ロ": "ろ",
    "ワ": "わ", "ヲ": "を", "ン": "ん",
    "ガ": "が", "ギ": "ぎ", "グ": "ぐ", "ゲ": "げ", "ゴ": "ご",
    "ザ": "ざ", "ジ": "じ", "ズ": "ず", "ゼ": "ぜ", "ゾ": "ぞ",
    "ダ": "だ", "ヂ": "ぢ", "ヅ": "づ", "デ": "で", "ド": "ど",
    "バ": "ば", "ビ": "び", "ブ": "ぶ", "ベ": "べ", "ボ": "ぼ",
    "パ": "ぱ", "ピ": "ぴ", "プ": "ぷ", "ペ": "ぺ", "ポ": "ぽ",
    "ヴ": "ぶ", "ー": "ー", "ァ": "ぁ", "ィ": "ぃ", "ゥ": "ぅ", "ェ": "ぇ", "ォ": "ぉ",
    "ッ": "っ", "ャ": "ゃ", "ュ": "ゅ", "ョ": "ょ", "ヮ": "ゎ"
}

# 英数字からひらがな読みへ変換する辞書
alnum_to_hiragana_dict = {
    "0": "ぜろ", "1": "いち", "2": "に", "3": "さん", "4": "し",
    "5": "ご", "6": "ろく", "7": "なな", "8": "はち", "9": "きゅう",
    "A": "えー", "B": "びー", "C": "しー", "D": "でぃー", "E": "いー",
    "F": "えふ", "G": "じー", "H": "えいち", "I": "あい", "J": "じぇー",
    "K": "けー", "L": "える", "M": "えむ", "N": "えぬ", "O": "おー",
    "P": "ぴー", "Q": "きゅー", "R": "あーる", "S": "えす", "T": "てぃー",
    "U": "ゆー", "V": "ぶい", "W": "だぶりゅー", "X": "えっくす", "Y": "わい", "Z": "ぜっと"
}

# カタカナをひらがなに変換し、英数字をひらがな読みへ変換する関数
def katakana_to_hiragana(text):
    # カタカナからひらがなへの変換
    for katakana, hiragana in katakana_to_hiragana_dict.items():
        text = text.replace(katakana, hiragana)

    # 英数字があればそのまま変換
    for alnum, hiragana in alnum_to_hiragana_dict.items():
        text = text.replace(alnum, hiragana)

    return text

# 外国語名のリストから辞書を生成する関数
def generate_dictionaries(foreign_names_list):
    katakana_to_hiragana_dict = {}
    English_to_hiragana_dict = {}

    for name, english_name in foreign_names_list:
        hiragana = katakana_to_hiragana(name)  # カタカナからひらがなに変換

        # 辞書への登録
        katakana_to_hiragana_dict[hiragana] = name
        English_to_hiragana_dict[hiragana] = english_name  # 英語名との対応

    return katakana_to_hiragana_dict, English_to_hiragana_dict

# 辞書をtxtファイルに書き出す関数（3列目は「固有名詞」、4列目は空列）
def save_dictionaries_to_txt(katakana_to_hiragana_dict, English_to_hiragana_dict, katakana_to_hiragana_file, English_to_hiragana_file):
    with open(katakana_to_hiragana_file, "w", encoding="utf-8") as f:
        for hiragana, katakana in katakana_to_hiragana_dict.items():
            f.write(f"{hiragana}\t{katakana}\t固有名詞\t\n")

    with open(English_to_hiragana_file, "w", encoding="utf-8") as f:
        for hiragana, english in English_to_hiragana_dict.items():
            f.write(f"{hiragana}\t{english}\t固有名詞\t\n")

# 辞書をplistファイルに書き出す関数
def save_dictionaries_to_plist(katakana_to_hiragana_dict, English_to_hiragana_dict, katakana_to_hiragana_file, English_to_hiragana_file):
    with open(katakana_to_hiragana_file, "w", encoding="utf-8") as f:
        f.write(f"<?xml version=1.0 encoding=UTF-8?>\n<!DOCTYPE plist PUBLIC -//Apple//DTD PLIST 1.0//EN http://www.apple.com/DTDs/PropertyList-1.0.dtd>\n<plist version=1.0>\n<array>\n")
        for hiragana, katakana in katakana_to_hiragana_dict.items():
            f.write(f"\t<dict>\n\t\t<key>phrase</key>\n\t\t<string>{katakana}</string>\n\t\t<key>shortcut</key>\n\t\t<string>{hiragana}</string>\n\t</dict>\n")
        f.write(f"</array>\n</plist>\n")

    with open(English_to_hiragana_file, "w", encoding="utf-8") as f:
        f.write(f"<?xml version=1.0 encoding=UTF-8?>\n<!DOCTYPE plist PUBLIC -//Apple//DTD PLIST 1.0//EN http://www.apple.com/DTDs/PropertyList-1.0.dtd>\n<plist version=1.0>\n<array>\n")
        for hiragana, english in English_to_hiragana_dict.items():
            f.write(f"\t<dict>\n\t\t<key>phrase</key>\n\t\t<string>{english}</string>\n\t\t<key>shortcut</key>\n\t\t<string>{hiragana}</string>\n\t</dict>\n")
        f.write(f"</array>\n</plist>\n")

# スクレイピングしてポケモンの外国語名一覧を取得する関数
def scrape_foreign_names(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    foreign_names_list = []

    # テーブルをクラスで取得
    tables = soup.find_all("table", {"class": className})

    # 各テーブルから名前を抽出
    for table in tables:
        rows = table.find_all("tr")[1:]  # 最初の行はヘッダーなので除く

        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 2:
                japanese_name = cols[0].text.strip()  # カタカナの名前
                english_name = cols[1].text.strip()  # 英語の名前

                foreign_names_list.append((japanese_name, english_name))

    return foreign_names_list

# データ元のURL
url = "https://wiki.xn--rckteqa2e.com/wiki/%E3%81%A8%E3%81%8F%E3%81%9B%E3%81%84%E3%81%AE%E5%A4%96%E5%9B%BD%E8%AA%9E%E5%90%8D%E4%B8%80%E8%A6%A7"

# データ元のclass名
className = "bluetable"

# ポケモン名をスクレイピング
foreign_names_list = scrape_foreign_names(url)

# 辞書を生成
katakana_to_hiragana_dict, English_to_hiragana_dict = generate_dictionaries(foreign_names_list)

# 辞書をtxtファイルに書き出し
save_dictionaries_to_txt(katakana_to_hiragana_dict, English_to_hiragana_dict, "pokemonAbilityIMEDictHira2Kata.txt", "pokemonAbilityIMEDictHira2Eng.txt")

# 辞書をplistファイルに書き出し
save_dictionaries_to_plist(katakana_to_hiragana_dict, English_to_hiragana_dict, "pokemonAbilityIMEDictHira2Kata.plist", "pokemonAbilityIMEDictHira2Eng.plist")

print("辞書ファイルの作成が完了しました。")
