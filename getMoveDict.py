import requests, os
from bs4 import BeautifulSoup

# カタカナからひらがなへの変換辞書（小文字含む）
# 各カタカナ文字を対応するひらがなに変換するための辞書
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

# 英数字からひらがな読みへの変換辞書
# 各英数字をひらがな読みの文字列に変換するための辞書
alnum_to_hiragana_dict = {
    "0": "ぜろ", "1": "いち", "2": "に", "3": "さん", "4": "し",
    "5": "ご", "6": "ろく", "7": "なな", "8": "はち", "9": "きゅう",
    "A": "えー", "B": "びー", "C": "しー", "D": "でぃー", "E": "いー",
    "F": "えふ", "G": "じー", "H": "えいち", "I": "あい", "J": "じぇー",
    "K": "けー", "L": "える", "M": "えむ", "N": "えぬ", "O": "おー",
    "P": "ぴー", "Q": "きゅー", "R": "あーる", "S": "えす", "T": "てぃー",
    "U": "ゆー", "V": "ぶい", "W": "だぶりゅー", "X": "えっくす", "Y": "わい", "Z": "ぜっと"
}

# テキスト中のカタカナをひらがなに、英数字をひらがな読みへ変換する関数
def katakana_to_hiragana(text):
    # カタカナをひらがなに変換
    for katakana, hiragana in katakana_to_hiragana_dict.items():
        text = text.replace(katakana, hiragana)

    # 英数字をひらがな読みへ変換
    for alnum, hiragana in alnum_to_hiragana_dict.items():
        text = text.replace(alnum, hiragana)

    return text

# 辞書データを書き出す共通関数（TXT/Plist両対応）
# file_typeに応じてテキストまたはPlist形式で辞書を書き出す
def write_dictionary_to_file(file_type, dict_data, dir_path, file_path):
    os.makedirs(dir_path, exist_ok=True)
    if file_type == "txt":
        # TXTファイルとして辞書を書き出し
        with open(file_path, "w", encoding="utf-8") as f:
            for hiragana, original in dict_data.items():
                f.write(f"{hiragana}\t{original}\t固有名詞\t\n")
    elif file_type == "plist":
        # Plistファイルのヘッダーとフッター
        header = """<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<array>\n"""
        footer = "</array>\n</plist>\n"
        # Plistのデータフォーマット
        main_format = "\t<dict>\n\t\t<key>phrase</key>\n\t\t<string>{}</string>\n\t\t<key>shortcut</key>\n\t\t<string>{}</string>\n\t</dict>\n"

        # Plistファイルとして辞書を書き出し
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(header)
            for hiragana, original in dict_data.items():
                f.write(main_format.format(original, hiragana))
            f.write(footer)

# 外国語名のリストから辞書を生成する関数
def generate_dictionaries(foreign_names_list):
    katakana_to_hiragana_dict = {}
    English_to_hiragana_dict = {}

    for name, english_name in foreign_names_list:
        hiragana = katakana_to_hiragana(name)  # カタカナからひらがなに変換
        katakana_to_hiragana_dict[hiragana] = name
        English_to_hiragana_dict[hiragana] = english_name

    return katakana_to_hiragana_dict, English_to_hiragana_dict

# スクレイピングしてポケモンの外国語名一覧を取得する関数
def scrape_foreign_names(url, class_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    foreign_names_list = []
    tables = soup.find_all("table", {"class": class_name})

    for table in tables:
        rows = table.find_all("tr")[1:]  # ヘッダーをスキップ
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 3:
                japanese_name = cols[0].text.strip()
                english_name = cols[1].text.strip()
                foreign_names_list.append((japanese_name, english_name))

    return foreign_names_list

# データ元のURLとクラス名
url = "https://wiki.xn--rckteqa2e.com/wiki/%E3%82%8F%E3%81%96%E3%81%AE%E5%A4%96%E5%9B%BD%E8%AA%9E%E5%90%8D%E4%B8%80%E8%A6%A7"
class_name = "bluetable"

# ポケモン名をスクレイピング
foreign_names_list = scrape_foreign_names(url, class_name)

# 辞書を生成
katakana_to_hiragana_dict, English_to_hiragana_dict = generate_dictionaries(foreign_names_list)

# 辞書をtxtとplistファイルに書き出し
write_dictionary_to_file("txt", katakana_to_hiragana_dict, "Move", "Move/pokemonMoveIMEDictHira2Kata.txt")
write_dictionary_to_file("txt", English_to_hiragana_dict, "Move", "Move/pokemonMoveIMEDictHira2Eng.txt")
write_dictionary_to_file("plist", katakana_to_hiragana_dict, "Move", "Move/pokemonMoveIMEDictHira2Kata.plist")
write_dictionary_to_file("plist", English_to_hiragana_dict, "Move", "Move/pokemonMoveIMEDictHira2Eng.plist")

print("辞書ファイルの作成が完了しました。")
