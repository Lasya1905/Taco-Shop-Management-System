def get_plates(connection):
    cursor = connection.cursor()
    query = ('select * from taco_shop.plate')
    cursor.execute(query)

    response = []
    for(plate_id, plate_name) in cursor:
        response.append(
            {
                'plate_id' : plate_id,
                'plate_name' : plate_name
            }
        )




if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    print(get_plates(connection))