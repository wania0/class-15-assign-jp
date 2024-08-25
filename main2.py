import db
from main import display_category, display_product, display_category_product
from query import add_category, add_product, update_product, delete_product

print("What action do you want to perform???")
print("Press 1 for Add categories")
print("Press 2 for Add products")
print("Press 3 for Update product")
print("Press 4 for Delete product")
print("Press 5 for Display all categories")
print("Press 6 for Display all products")
print("Press 7 for Display both product and categories combine")

action = int(input("Enter any number in 1-7:"))

if action == 1 :
    
    db_conn = db.mysqlconnect()
    data = {'name': input("Enter category name:\n") }
    add_category(db_conn, data)
    print(f"New category {data['name']} added successfully!")
    db.disconnect(db_conn)
    
elif action == 2 :
    
    db_conn = db.mysqlconnect()
    data = {'name': input("Enter product name:\n"),'cat_id': input("Enter cat_id:\n")}
    add_product(db_conn, data)
    print(f"New product {data['name']} added successfully!")
    db.disconnect(db_conn)

elif action == 3 :
    
    db_conn = db.mysqlconnect()
    product_id = input("Enter product ID to update:\n")
    new_product_name = input("Enter the new product name:\n")
    update_product(db_conn, product_id, new_product_name)
    db.disconnect(db_conn)

elif action == 4 :
    
    db_conn = db.mysqlconnect()
    product_id = input("Enter product ID to delete:\n")
    delete_product(db_conn, product_id)
    db.disconnect(db_conn)
    
elif action == 5 :
    
    db_conn = db.mysqlconnect()
    display_category(db_conn)
    db.disconnect(db_conn)

elif action == 6 :
    
    db_conn = db.mysqlconnect()
    display_product(db_conn)
    db.disconnect(db_conn)
    
elif action == 7 :
    
    db_conn = db.mysqlconnect()
    display_category_product(db_conn)
    db.disconnect(db_conn)
    
else:
    print("Please enter a number between 1 and 7.")