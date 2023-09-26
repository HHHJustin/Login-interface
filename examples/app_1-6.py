from flask import Flask # 載入 Flask
from flask import request # 載入 Request 物件
# 建立 Application, 可以設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder="public", # 靜態檔案的資料夾名稱
    static_url_path="/"
            ) # 靜態檔案對應的網址路徑
# 所有在static 資料夾底下的檔案，都對應到網址路徑 /www/檔案名稱

# 建立路徑 /getSum 對應的處理函式
# 利用要求字串(Quert String) 提供彈性: /getSum?max=最大數字

@app.route("/getSum")
def getSum():
    maxNumber=request.args.get("max", 100)
    minNumber=request.args.get("min", 1)
    maxNumber=int(maxNumber)
    minNumber=int(minNumber)
    result = 0
    for n in range(minNumber, maxNumber+1):
        result += n
    return "結果  " + str(result)

# 建立路徑 / 對應的處理函式
@app.route("/")
def index(): #用來回應路徑 / 的處理函式
    # print("請求方法", request.method)
    # print("通訊協定", request.scheme)
    # print("主機名稱", request.host)
    # print("路徑", request.path)
    # print("完整的網址", request.url)
    # print("瀏覽器和作業系統", request.headers.get("user-agent"))
    # print("語言偏好", request.headers.get("accept-language"))
    # print("引薦網址", request.headers.get("referrer"))
    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        return "Hello Flask"
    else:
        return "你好"
    

# 建立路徑 /data 對應的處理函式
@app.route("/data")
def handleData():
    return "My Data"

# 建立動態路由：建立路徑 /user/使用者名稱 對應的處理函式
@app.route("/user/<username>")
def handleUser(username):
    if username == "YAYA":
        return "你好 " + username
    return "Hello " + username

# 啟動網站伺服器，可透過port參數指定port
app.run(port=3000)