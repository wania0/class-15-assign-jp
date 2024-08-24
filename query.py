def get_category(db_conn):
  cur = db_conn.cursor()
  cur.execute("SELECT * FROM category")
  return cur.fetchall()

def add_category(db_conn, data):
    cur = db_conn.cursor()
    id = data['id']
    name = data['name']
    created_at = data['created_at']
    cur.execute(
    f"INSERT INTO category (id, name, created_at) VALUES ({id}, '{name}', '{created_at}')"
)
    db_conn.commit()
    
def get_product(db_conn):
  cur = db_conn.cursor()
  cur.execute("SELECT * FROM product")
  return cur.fetchall()

def add_product(db_conn, data):
    cur = db_conn.cursor()
    id = data['id']
    name = data['name']
    cat_id = data['cat_id']
    created_at = data['created_at']
    updated_at = data['updated_at']
    cur.execute(
    f"INSERT INTO product (id, name, cat_id, created_at, updated_at) VALUES ({id}, '{name}', {cat_id}', {created_at}', '{updated_at}')"
)
    db_conn.commit()
  

def update_product(db_conn, product_id, new_name):
    cur = db_conn.cursor()
    query = f"""
        UPDATE product SET name = '{new_name}' WHERE id = {product_id}
    """
    cur.execute(query)
    db_conn.commit()
    
def delete_product(db_conn, product_id):
    cur = db_conn.cursor()
    query = f"DELETE FROM product WHERE id = {product_id}"
    cur.execute(query)
    db_conn.commit()

def display_combine(db_conn):
    cur = db_conn.cursor()
    cur.execute("""
        SELECT c.name AS category_name, p.name AS product_name
        FROM category c
        LEFT JOIN product p ON c.id = p.category_id
    """)

    combined_data = cur.fetchall()
