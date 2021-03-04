import os
import sqlite3
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))
dataBase_1 = sqlite3.connect(r"C:\Users\hp\Desktop\my_project\db_login.db")
cursor_1 = dataBase_1.cursor()

cursor_1.execute(r"create table if not exists Department (name_Dep text)")
cursor_1.execute(r"create table if not exists users (name_users text)")
cursor_1.execute(
    r"create table if not exists data_operations (user_Ip text , user_email text, events text,events_time text)")
cursor_1.execute(
    r"create table if not exists error (user_ip text , user_Email text, Events text,events_time text)")

dataBase_1.commit()
dataBase_1.close()
# we finished this file .
