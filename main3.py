import db
from query import get_category, add_category, update_product, delete_product, get_product , display_combine, add_product
import json

def main_menu():
    db_conn = db.mysqlconnect()
    
    while True:
        print("_______________________________________________________")
        print("What action do you want to perform:")
        print("1. Add categories")
        print("2. Add products")
        print("3. Update product")
        print("4. Delete product")
        print("5. Display all categories")
        print("6. Display all products")
        print("7. Display both product and categories combine")
        print("_______________________________________________________")
        
        choice = input("Enter your choice (1-7) or 'q' to quit:\n")
        
        if choice == '1':
            data = {
                'id': input("Enter category id:\n"),
                'name': input("Enter category name:\n"),
                'created_at': input("Enter category created date:\n")
            }
            add_category(db_conn, data)
            get_category(db_conn)
        elif choice == '2':
            data = {
                'id': input("Enter category id:\n"),
                'name': input("Enter product name:\n"),
                'cat_id': input("Enter cat_id:\n"),
                'created_at': input("Enter created_at:\n"),
                'updated_at': input("Enter updated_at:\n"),
            }
            add_product(db_conn, data)
        elif choice == '3':
            product_id = input("Enter product ID to update:\n")
            new_name = input("Enter the new product name:\n")
            update_product(db_conn, product_id, new_name)
        elif choice == '4':
            product_id = input("Enter product ID to delete:\n")
            delete_product(db_conn, product_id)
        elif choice == '5':
            get_category(db_conn)
        elif choice == '6':
            get_product(db_conn)
        elif choice == '7':
            display_combine(db_conn)
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()
