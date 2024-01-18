from flask import Flask, render_template, jsonify, request
import datetime
import random
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
import json

app = Flask(__name__, template_folder="templates", static_folder="static")
app.debug = True

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
    return render_template("index.html", **{"now": now})



@app.get("/login")
def login():
    return render_template("login.html")


def verify_sign(params, sign):
    try:
        # base64编码
        encrypt_data = base64.b64decode(sign)
        # AES解密,key,iv必须为16字节
        key = '0123456789abcdef'.encode()
        iv = '0123456789abcdef'.encode()
        aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
        data = aes.decrypt(encrypt_data)
        data = unpad(data, 16)
        print('解密成功')
        res = json.loads(data.decode())
        if res == params:
            print('比对成功！！请进')
            return True
        print('比对失败！')
    except Exception as e:
        print('解密报错', e)
        return False

@app.get("/books")
def get_books():
    # 查询参数
    params = request.args.to_dict()
    # 校验sign值
    if 'sign' not in params:
        return jsonify(['非法入侵!!滚出去'])
    sign = params.pop('sign')
    verify = verify_sign(params, sign)
    if not verify:
        return jsonify(['非法入侵!!滚出去'])
    page_num = int(params.get('page', 1))
    books = ["聊斋志异", "金瓶梅", "国色天香", "剪灯新话", "西游记", "三国演义", "水浒传", '大黑驴', '小黑驴', '宿舍黑驴']
    # random_books = random.sample(books, 4)
    start_index = (page_num - 1) * 2
    end_index = page_num * 2
    page_book_list = books[start_index:end_index]
    return jsonify(page_book_list)


app.run()
