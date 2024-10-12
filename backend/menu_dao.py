# dao stands for data access object
from sql_connection import get_sql_connection

def get_all_products(connection):
    

    cursor = connection.cursor()
    query =  ("SELECT menu.menuitem_id, menu.name, menu.plate_id, menu.price , plate.plate_name FROM taco_shop.menu inner join taco_shop.plate on menu.plate_id=plate.plate_id;")

    cursor.execute(query)

    response = []

    for (menuitem_id, name, plate_id, price, plate_name) in cursor:
        response.append(
            {
                'menuitem_id': menuitem_id,
                'name':name,
                'plate_id': plate_id,
                'price': price,
                'plate_name':plate_name
            }
        )

    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("insert into taco_shop.menu (name, plate_id, price) values(%s,%s,%s);")

    data = (product['menu_item_name'],product['plate_id'],product['price'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, menuitem_id):
    cursor = connection.cursor()
    query = ("delete from taco_shop.menu where menuitem_id="+str(menuitem_id)
    )
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection,10))