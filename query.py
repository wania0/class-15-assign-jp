def get_category(db_conn):
  cur = db_conn.cursor()
  cur.execute("SELECT * FROM category")
  return cur.fetchall()

def add_category(db_conn, data):
    cur = db_conn.cursor()
    name = data['name']
    cur.execute(f"INSERT INTO category (name) VALUES ('{name}')")
    db_conn.commit()
    
def get_product(db_conn):
  cur = db_conn.cursor()
  cur.execute("SELECT * FROM product")
  return cur.fetchall()

def add_product(db_conn, data):
    cur = db_conn.cursor()
    name = data['name']
    cat_id = data['cat_id']
    cur.execute(f"INSERT INTO product (name, cat_id) VALUES ('{name}', '{cat_id}')")
    db_conn.commit()

def update_product(db_conn, product_id, new_name):
    cur = db_conn.cursor()
    cur.execute(f"UPDATE product SET name = '{new_name}' WHERE id = {product_id}")
    db_conn.commit()
    
def delete_product(db_conn, product_id):
    cur = db_conn.cursor()
    cur.execute(f"DELETE FROM product WHERE id = {product_id}")
    db_conn.commit()

def display_combine(db_conn):
    cur = db_conn.cursor()
    cur.execute("select c.name as category_name, p.name as product_name from category as c left join product as p on c.id = p.cat_id")
    return cur.fetchall()
