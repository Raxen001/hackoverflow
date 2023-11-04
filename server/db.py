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
    NAME VARCHAR(20) NOT NULL,
    SECRET VARCHAR(20) NOT NULL,
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
    add_user = f"""
        INSERT INTO users
        (NAME, SECRET  )
        VALUES ({username}, {secret});
    """
    mycursor.execute(add_user)
    mydb.close()


if __name__ == "__main__":

    # create_database()
    # create_user_table()
    add_user("raxen", "hello_world")
