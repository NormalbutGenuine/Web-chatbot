from pymongo import MongoClient
from pymongo import CursorType
import datetime

client = MongoClient('127.0.0.1', 27017)
db = client.test_database   # db생성
collection = db.test_collection

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts               # 테이블 생성(posts)
post_id = posts.insert_one(post).inserted_id
print(post_id)