import sqlite3
from flask_bcrypt import Bcrypt
from datetime import datetime 

bcrypt = Bcrypt()

def createUser(name=None, lastName=None, email=None, password=None): 
    hashed = bcrypt.generate_password_hash(password).decode('utf-8')
    conn = sqlite3.connect("./data/data.db")
    c = conn.cursor()

    c.execute('''INSERT INTO users(name, lastName, email, password, registrationDate) VALUES (?, ?, ?, ?, ?)''', (name, lastName, email, hashed, datetime.now()))

    conn.commit()
    conn.close()

def checkUser(email=None, password=None):
    conn = sqlite3.connect("./data/data.db")
    c = conn.cursor()

    c.execute('''SELECT email, password FROM users WHERE email=?''', (email,))
    result = c.fetchone()
    conn.close() 
    if result:
        return bcrypt.check_password_hash(result[1], password)
    return False

def getUser(email=None):
    conn = sqlite3.connect("./data/data.db")
    c = conn.cursor()
    c.execute('''SELECT id, name, lastName, email FROM users WHERE email=?''', (email,))
    result = c.fetchone()
    conn.close()
    return result


conn = sqlite3.connect("./data/data.db")
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS users''')
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL,
    name TEXT,
    lastName TEXT,
    email TEXT,
    password TEXT,
    registrationDate TEXT,
    PRIMARY KEY (id)
)''')
createUser(name='david', lastName='agostini', email='david.agostini@gmail.com', password='troia')
createUser(name='qqqq', lastName='qqqq', email='qqqq@qqqq', password='qqqq')
checkUser(email='david.agostini@gmail.com', password='troia')
conn.commit()
conn.close()