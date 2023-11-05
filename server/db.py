import mysql.connector


def create_database():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=33060
    )

    mycursor = mydb.cursor()

    create_db = "CREATE DATABASE users"
    mycursor.execute(create_db)

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
    LOCATION VARCHAR(200),
    DATE_JOINED DATE,
    PRIMARY KEY (ID)
);
    """
    mycursor.execute(user_table)
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
    add_user_query = "INSERT INTO users (NAME, SECRET) VALUES (%s, %s)"
    user_data = (username, secret)
    mycursor.execute(add_user_query, user_data)
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
        print(f"User with username '{email}' exists.")
    else:
        print(f"User with username '{email}' does not exist.")
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
        print(f"secret '{secret}' exists.")
        mydb.close()
        return secret[0]
    else:
        print(f"secret '{secret}' does not exist.")
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


if __name__ == "__main__":
    # drop_table()
    # create_database()
    # create_user_table()
    # add_user("raxengamer001@gmail.com", "hello_world")
    check_user_exists("raxengamer001@gmail.com")
    get_user_secret("raxengamer001@gmail.com")
    get_user_secret("zumrkushi@gmail.com")
