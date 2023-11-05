import mysql.connector
import logging
import time

logging.basicConfig(filename='./logs/db.log', encoding='utf-8',
                    format='%(asctime)s: %(message)s', level=logging.DEBUG)
logging.debug('Service started')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


def create_database():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=33060
    )

    mycursor = mydb.cursor()

    create_db = "CREATE DATABASE users"
    try:
        mycursor.execute(create_db)
        logging.debug('Database created successfully')
    except:
        logging.error('Database creation failure')

    mydb.close()


def create_ebook_database():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=33060
    )

    mycursor = mydb.cursor()

    create_db = "CREATE DATABASE ebooks"
    try:
        mycursor.execute(create_db)
        logging.debug('ebooks Database created successfully')
    except:
        logging.error('ebooks Database creation failure')

    mydb.close()


def create_user_table():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=33060,
        database="users"
    )

    mycursor = mydb.cursor()
    user_table = """
    CREATE TABLE users (
    ID INT AUTO_INCREMENT NOT NULL,
    NAME VARCHAR(200) NOT NULL,
    SECRET VARCHAR(200) NOT NULL,
    ROLE VARCHAR(20) NOT NULL,
    LOCATION VARCHAR(200),
    DATE_JOINED DATE,
    PRIMARY KEY (ID)
);
    """
    try:
        mycursor.execute(user_table)
        logging.debug('User Table Created successfully')
    except:
        logging.error('Error creating UserTable')

    mydb.close()


def create_ebook_table():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=33060,
        database="users"
    )

    mycursor = mydb.cursor()
    user_table = """
    CREATE TABLE users (
    ID INT AUTO_INCREMENT NOT NULL,
    NAME VARCHAR(200) NOT NULL,
    SECRET VARCHAR(200) NOT NULL,
    ROLE VARCHAR(20) NOT NULL,
    LOCATION VARCHAR(200),
    DATE_JOINED DATE,
    PRIMARY KEY (ID)
);
    """
    try:
        mycursor.execute(user_table)
        logging.debug('User Table Created successfully')
    except:
        logging.error('Error creating UserTable')

    mydb.close()


def add_user(username, secret):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=33060,
        database="users"
    )

    mycursor = mydb.cursor()
    add_user_query = "INSERT INTO users (NAME, SECRET, role) VALUES (%s, %s, %s)"
    user_data = (username, secret, "admin")
    try:
        mycursor.execute(add_user_query, user_data)
        logging.debug('%s User added', user_data[0])
    except:
        logging.error("Erorr adding user %s", user_data[0])

    mydb.commit()
    mydb.close()


def check_user_exists(email):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=33060,
        database="users"
    )
    mycursor = mydb.cursor()
    check_user_query = "select * from users where NAME=%s"
    user_data = (email,)
    mycursor.execute(check_user_query, user_data)
    user = mycursor.fetchone()
    if user:
        logging.debug(f"User with username '{email}' exists.")
    else:
        logging.error(f"User with username '{email}' does not exist.")
    mydb.close()


def get_user_secret(email):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=33060,
        database="users"
    )
    mycursor = mydb.cursor()
    get_user_query = "select SECRET from users where NAME=%s"
    user_data = (email,)
    mycursor.execute(get_user_query, user_data)
    secret = mycursor.fetchone()
    if secret:
        logging.debug(f"secret '{secret}' exists.")
        mydb.close()
        return secret[0]
    else:
        logging.error(f"secret '{secret}' does not exist.")
    mydb.close()
    return None


# debug
def drop_table():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=33060
    )
    mycursor = mydb.cursor()
    mycursor.execute("DROP DATABASE users")
    mydb.close()


def get_role(email):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=33060,
        database="users"
    )
    mycursor = mydb.cursor()
    get_role_query = "select ROLE from users where NAME=%s"
    user_data = (email,)
    mycursor.execute(get_role_query, user_data)
    role = mycursor.fetchone()
    if role:
        logging.debug(f"role '{role}' exists.")
        mydb.close()
        return role[0]
    else:
        logging.error(f"role '{role}' does not exist.")
    mydb.close()
    return None


# if __name__ == "__main__":
    # drop_table()
    # create_database()
    # create_user_table()
    # add_user("raxengamer001@gmail.com", "hello_world")
    # check_user_exists("raxengamer001@gmail.com")
    # get_role("raxengamer001@gmail.com")
