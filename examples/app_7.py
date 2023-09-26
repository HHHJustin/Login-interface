from flask import Flask # 載入 Flask
from flask import request # 載入 Request 物件
from flask import redirect
import json
# 建立 Application, 可以設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder="public", # 靜態檔案的資料夾名稱
    static_url_path="/"
            ) # 靜態檔案對應的網址路徑
# 所有在static 資料夾底下的檔案，都對應到網址路徑 /www/檔案名稱
@app.route("/en/")
def index_english():
    return json.dumps({
            "status":"ok",
            "text":"Hello World"
        })

@app.route("/")
def index_chinese():
    return json.dumps({
         "status":"ok",
         "text":"你好"   
        }, ensure_ascii=False) # 指示不要用ASCII編碼處理中文

# 建立路徑 / 對應的處理函式
@app.route("/")
def index(): #用來回應路徑 / 的處理函式
    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en/")
        
    else:
        return redirect("/zh/")
        


# 啟動網站伺服器，可透過port參數指定port
app.run(port=3000)