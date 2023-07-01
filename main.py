from flask import Flask, render_template
from datetime import datetime
import requests
from bs4 import BeautifulSoup
resp = requests.get(url)

app = Flask(__name__)
# 產生Flask物件
# __name__當前本身


@app.route("/bmi/height=<h>&weight=<w>")
def get_bmi(h, w):
    try:
        bmi = round(eval(w) / (eval(h) / 100) ** 2, 2)
        print(bmi)
        return f"BMI:{bmi}"
    except Exception as e:
        print(e)
        return "資料有誤!"


@app.route("/book/<int:id>")#網址帶參數預設為<string:參數名稱>需要修改成<int:id>
def book(id):
    books = {1: "Python", 2: "Java", 3: "C++"}
    try:
        return books[id]
    except Exception as e:
        print(e)
        return "沒有書籍資料"


@app.route("/today")
def today():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>{datetime.now()}</h1>" #回傳文字訊息到前端網頁

    # 顯示目前日期跟時間
    # ■ 新增route(/date)


@app.route("/index")
@app.route("/")  # 裝飾器綁定 網址跟方法
def index():
    name = "jerry"
    date = get_today()
    content = {"name": name, "date": date}
    return render_template("index.html", content=content)


def get_today():
    date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    return date


@app.route("/stock")
def stock():
    
    for stock in stocks:
        print(stock["分類"], stock["指數"])

    return render_template("stock.html", date=get_today(), stocks=stocks)


if __name__ == "__main__":  # 啟動
    # 全域端宣告
    stocks = [
        {"分類": "日經指數", "指數": "22,920.30"},
        {"分類": "韓國綜合", "指數": "2,304.59"},
        {"分類": "香港恆生", "指數": "25,083.71"},
        {"分類": "上海綜合", "指數": "3,380.68"},
    ]
    print(get_bmi(167, 67.5))
    # print(stock())
    app.run(debug=True)
    # 程式碼修改後需要儲存(debug=True)➔ (自動刷新)
    # CTRL+C(停止Server)
