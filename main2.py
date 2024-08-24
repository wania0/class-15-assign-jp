import db
from query import get_category, add_category
import json

data = {}
data['id'] = input("enter category id:\n")
data['name'] = input("enter category name:\n")
data['cretaed_at'] = input("enter category created date:\n")

db_conn = db.mysqlconnect()

add_category(db_conn, data)

categoryy = get_category(db_conn)
print(
  json.dumps(categoryy, default=str, indent=4)
)

