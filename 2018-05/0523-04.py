#生成的激活码 保存到数据库

import pymysql
import random

def create_number(number, long):
    str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    b = []
    for i in range(number):
        a = ''
        for j in range(long):
            a +=random.choice(str)
        b.append(a)
    return b

def insert_sql (list):
    db = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mysql')
    cur = db.cursor()
    cur.execute('DROP DATABASE mydb')
    cur.execute('CREATE DATABASE IF NOT EXISTS mydb')
    cur.execute('USE mydb')
    cur.execute('''CREATE TABLE IF NOT EXISTS code(
                    id INT NOT NULL AUTO_INCREMENT,
                    code VARCHAR(32) NOT NULL,
                    PRIMARY KEY(id))''')
    for code in list:
        cur.execute('INSERT INTO code(code) VALUES(%s)',(code))
        cur.connection.commit()
    db.close()


if __name__ == '__main__':
    number = int(input('number:'))
    long = int(input('long:'))
    insert_sql(create_number(number,long))



