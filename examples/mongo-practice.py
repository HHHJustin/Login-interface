import pymongo
# 連線到 MongoDB 雲端資料庫
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId

uri = "mongodb+srv://root:root123@mycluster.vmhkfiv.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection

db = client.website #選擇要操作 website 資料庫
connection = db.users # 選擇操作 users 集合
result = connection.update_many({
    "level":"test@test.com"
},{
    "$inc":{
        "level": 5
    }
}
)
print(result.matched_count)
print(result.modified_count)

# 把資料新增到集合中

# result = connection.insert_many([
#     {
#         "name":"YAYA",
#         "email":"test@test.com",
#         "gender":"男",
#         "level":1,
#     },
#     {
#         "name":"YAYA1",
#         "email":"test1@test.com",
#         "gender":"男",
#         "level":2,
#     }]
# )
# print("資料新增成功")
# print(result.inserted_ids)