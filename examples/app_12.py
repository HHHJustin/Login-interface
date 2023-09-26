from flask import Flask # 載入 Flask
from flask import request # 載入 Request 物件
from flask import redirect
from flask import render_template
from flask import session
import json
# 建立 Application, 可以設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder="public", # 靜態檔案的資料夾名稱
    static_url_path="/"
            ) # 靜態檔案對應的網址路徑

app.secret_key="any string but secret" # 設定 Session 密鑰

# 建立路徑 / 對應的處理函式
@app.route("/")
def index(): #用來回應路徑 / 的處理函式
    return "Hi"

# 使用 GET 方法處理路徑 /hello
@app.route("/hello")
def hello():
    name=request.args.get("name", "")
    session["username"]=name
    return "你好 " + name

# 使用 GET 方法處理路徑 /talk
@app.route("/talk")
def talk():
    name=session["username"]
    return "請多指教 " + name 
        
# 啟動網站伺服器，可透過port參數指定port
app.run(port=3000)