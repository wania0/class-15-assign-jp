import db
from query import get_category, get_product, display_combine
import json

db_conn = db.mysqlconnect()

category = get_category(db_conn)
print(
  json.dumps(category, default=str, indent=4)
)

get_product(db_conn)
products = get_product(db_conn)
print(json.dumps(products, default=str, indent=4))


display_combine(db_conn)
combined_data = display_combine(db_conn)
print(json.dumps(products, default=str, indent=4))
