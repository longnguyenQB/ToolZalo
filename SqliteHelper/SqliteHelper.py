import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        
    return conn

def delete_table(conn, table):
    c = conn.cursor()
    sql = f"""DROP TABLE IF EXISTS {table};""" 
    c.execute(sql)

def create_table(conn, query):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)

def insert_table(conn, table, columns, values, realtime):
    """insert values of row to table

    Args:
        cur (_type_): cursor
        table (str): table name
        columns (List): list of column name
        values (List): list of values
    """    
    columns = ",".join(columns)
    value = ",".join(["?"]*len(values))
    sql = f''' INSERT INTO {table}({columns})
                VALUES({value}) '''
    cur = conn.cursor()
    cur.execute(sql, values)
    if realtime == True:
        conn.commit()

def update_table(conn, table, columns, values, column_where, value_where ):
    """update values of columns where another column

    Args:
        conn (_type_): cursor
        table (_type_): table name
        columns (List): list of column name need update
        values (List): list of value need update
        column_where (str): column condition
        value_where (str): value condition
    """    
    q = []
    for i in range(len(columns)):
        q.append(columns[i] + " = ? ")
    
    sql = f'''UPDATE {table} SET 
            {",".join(q)}
            WHERE {column_where} = ?'''
    values.append(value_where)
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()

def select_get_value(conn, table, id, column):
    cur = conn.cursor()
    cur.execute(f"SELECT {column} FROM {table} WHERE id == {id}")
    return cur.fetchall()[0]

def get_columns_name(conn, table):
    print(table)
    cur = conn.cursor()
    cur.execute(f"select * from {table} where 1=2")
    column_names = [i[0] for i in cur.description]
    return column_names

def get_length(conn, query):
    """Get length of table

    Args:
        conn (_type_): connection
        query (_type_): query select table

    Returns:
        _type_: _description_
    """    
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()[0][0]

def create_column(conn, table_name, column_name, type_column):
    c = conn.cursor()
    query = f"ALTER TABLE {table_name} ADD {column_name} {type_column};"
    c.execute(query)