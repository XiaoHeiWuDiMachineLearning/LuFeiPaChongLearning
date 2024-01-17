from flask import Flask, render_template, jsonify
import datetime
import random

app = Flask(__name__, template_folder="templates", static_folder="static")


# 路由设置
# @app.get("/index")
# def index():
#     now = datetime.datetime.now().strftime("%y/%m/%d %X")
#     books = ["聊斋志异", "金瓶梅", "国色天香", "剪灯新话"]
#
#     return render_template("index.html", **{"xxx": now,"books":books})


@app.get("/index")
def index():
    now = datetime.datetime.now().strftime("%y/%m/%d %X")
    return render_template("index.html", **{"xxx": now})


@app.get("/login")
def login():
    return render_template("login.html")


@app.get("/books")
def get_books():
    books = ["聊斋志异", "金瓶梅", "国色天香", "剪灯新话", "西游记", "三国演义", "水浒传"]
    random_books = random.sample(books, 4)
    return jsonify(random_books)


app.run()
