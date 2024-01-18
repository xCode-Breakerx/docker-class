import mysql.connector
import redis


def main():
    mydb = mysql.connector.connect(
        host="mysql",
        user="exo13",
        password="exo13",
        database="exo13_db",
        port=52000,
    )
    mydb.autocommit = True

    rc = redis.Redis(host="redis", port=6379)
    print("========= redis =========")

    rc.set('foo', 'bar')
    print(f"Redis: {rc.get('foo') = }")
    print(f"Redis: {rc.keys() = }")
    print("========= redis =========")

    print("")

    print("========= mysql =========")
    mycursor = mydb.cursor(buffered=True)
    print(f"{mycursor.execute('CREATE TABLE IF NOT EXISTS Exo13_table (name VARCHAR(255), address VARCHAR(255))') = }")
    mycursor.execute('SHOW TABLES')
    [print(X) for X in mycursor.fetchall()]
    print("========= mysql =========")

    print("")


if __name__ == '__main__':
    main()
