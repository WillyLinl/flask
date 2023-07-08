from flask import Flask, render_template
from datetime import datetime
from crawler.stock import get_stock
from crawler.lottory import get_lottory


app = Flask(__name__)


@app.route("/bmi/height=<h>&weight=<w>")
def get_bmi(h, w):
    try:
        bmi = round(eval(w) / (eval(h) / 100) ** 2, 2)
        print(bmi)
        return f"BMI:{bmi}"
    except Exception as e:
        print(e)
        return "資料有誤!"


@app.route("/book/<int:id>")
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
    return f"<h1>{datetime.now()}</h1>"


@app.route("/index")
@app.route("/")
def index():
    name = "jerry"
    date = get_today()
    content = {"name": name, "date": date}
    return render_template("index.html", content=content)


def get_today():
    date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    return date


@app.route("/lottory")
def lottory():
    return render_template("lottory.html", lottorys=get_lottory())


@app.route("/stock")
def stock():
    # 呼叫爬蟲程式
    stocks = get_stock()
    for stock in stocks:
        print(stock["分類"], stock["指數"])

    return render_template("stock.html", date=get_today(), stocks=stocks)


if __name__ == "__main__":
    # print(get_bmi(167, 67.5))
    # print(stock())
    app.run(debug=True)
