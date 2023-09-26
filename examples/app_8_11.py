from flask import Flask # 載入 Flask
from flask import request # 載入 Request 物件
from flask import redirect
from flask import render_template
import json
# 建立 Application, 可以設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder="public", # 靜態檔案的資料夾名稱
    static_url_path="/"
            ) # 靜態檔案對應的網址路徑

# 建立路徑 / 對應的處理函式
@app.route("/")
def index(): #用來回應路徑 / 的處理函式
    return render_template("index.html")

@app.route("/page")
def index_2(): #用來回應路徑 / 的處理函式
    return render_template("page.html")

# 處理路徑 /show
@app.route("/show")
def show(): #用來回應路徑 / 的處理函式
    name = request.args.get("n","")
    return "歡迎光臨 " + name

@app.route("/calculate", methods=["POST"])
def calculate(): #用來回應路徑 / 的處理函式
    # maxNumber = request.args.get("max","100") # GET取得要求方法
    maxNumber = request.form["max"]
    maxNumber = int(maxNumber)
    count = 0
    for i in range(1, maxNumber + 1):
        count += i
    return render_template("result.html", data=str(count))
        
# 啟動網站伺服器，可透過port參數指定port
app.run(port=3000)