from flask_login import UserMixin
import sqlite3

class User(UserMixin):
    def __init__(self, id=None, name=None, lastName=None, email=None):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.email = email
    def is_active(self):
        return True
