import requests
import datetime


# 0. ファイル名に用いる日付のフォーマット定義
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
dt = now.date().strftime('%Y%m%d')

# 1. 取得したいURLを指定
page = "https://www.google.com/"
name = "google"
try:
    # 2. ページ内容を取得
    response = requests.get(page)

    # ステータスコードが200（成功）か確認
    response.raise_for_status()

    # 3. テキストファイルに書き出し（文字化け防止のためutf-8を指定）
    # filename = 'pagename_' + now.strftime('%Y%m%d') + '.txt'
    # filename = './output/' + name + '_' + now.strftime('%Y%m%d') + '.txt'
    filename = name + '_' + now.strftime('%Y%m%d') + '.txt'
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)

    print("ファイルへの書き出しが完了しました。")
    print(dt)

except requests.exceptions.RequestException as e:
    print(f"エラーが発生しました: {e}")
