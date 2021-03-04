import sqlite3
import itertools
import os
import logging


# data_operations (user_Ip text , user_email text, events text,events_time text) , error (user_ip text , user_Email text, Events text,events_time text) , Department (name_Dep text) , users (name_users text)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
logging.basicConfig(filename=r"C:\Users\hp\Desktop\my_project\script_log.log", format='%(asctime)s %(message)s',
                    datefmt='%b %d %H:%M:%S', level=logging.INFO)
database_1 = sqlite3.connect(r"C:\Users\hp\Desktop\my_project\db_login.db")
cr = database_1.cursor()


def commit_and_close():
    database_1.commit()


def show_data_1(list_1):
    print("the item in the data_operations :")
    for key, row in enumerate(list_1):
        print(f"the time of the data_operations : '{row[1]}'")
        print(f"the Department of the data_operations : '{row[2]}'")
        print(f"the Event of the data_operations : '{row[3]}'")
        print(f"the User of the data_operations : '{row[4]}'")
        print(f"the IP of the data_operations : '{row[5]}'")
        print(f"the Email of the data_operations : '{row[6]}'")
        print("############################################################")
    commit_and_close()


# in the line 1- time , 2- Department , 3-event , 4- Email , 5-user , 6- IP
def show_data_2(list_2):
    print("###### show skills ########")

    for key, row in enumerate(list_2):
        print(f"the time of the data_operations : '{row[1]}'")
        print(f"the Department of the data_operations : '{row[2]}'")
        print(f"the Event of the data_operations : '{row[3]}'")
        print(f"the Email of the data_operations : '{row[4]}'")
        print(f"the User of the data_operations : '{row[5]}'")
        print(f"the IP of the data_operations : '{row[6]}'")
        print("############################################################")
    commit_and_close()


def show_data_3(list_3):  # 1- time , 2- Department , 3-event , 4- user
    print("###### show skills ########")
    for row in list_3:
        print(f"the Time of the data_operations : '{row[1]}'")
        print(f"the Department of the data_operations : '{row[2]}'")
        print(f"the Event of the data_operations : '{row[3]}'")
        print(f"the User of the data_operations : '{row[4]}'")
        print("############################################################")
    commit_and_close()


# in the line 1- time , 2- Department , 3- event , 4- user , 5- Ip , 6- Email
def show_data_4(list_4):
    print("###### show skills ########")
    for row in list_4:
        print(f"the Time of the data_operations : '{row[1]}'")
        print(f"the Department of the data_operations : '{row[2]}'")
        print(f"the Event of the data_operations : '{row[3]}'")
        print(f"the Email of the data_operations : '{row[4]}'")
        print(f"the User of the data_operations : '{row[5]}'")
        print(f"the IP of the data_operations : '{row[6]}'")
        print("############################################################")
    commit_and_close()


# in the line 1- time , 2- Department , 3- event , 4- user , 5- Ip , 6- Email
def add_data_general_1(list_data_1):
    print("##### add skill #########")
    for row in list_data_1:
        cr.execute(
            f"insert into data_operations (user_Ip,user_email,events ,events_time) values ('{row[5]}','{row[6]}','{row[3]}','{row[1]}')")
        cr.execute(
            f"insert into Department (name_Dep) values ('{row[2]}')")
        cr.execute(f"insert into users (name_users) values ('{row[4]}')")
    commit_and_close()


# in the line 1- time , 2- Department , 3-event , 4- Email , 5-user , 6- IP
def add_data_general_2(list_data_2):
    print("##### add skill #########")
    for row in list_data_2:
        cr.execute(
            f"insert into data_operations (user_Ip,user_email,events,events_time) values ('{row[6]}','{row[4]}','{row[3]}','{row[1]}')")
        cr.execute(
            f"insert into Department (name_Dep) values ('{row[2]}')")
        cr.execute(f"insert into users (name_users) values ('{row[5]}')")
    commit_and_close()


# in the line we get 1- time , 2- Department , 3-event , 4- user
def add_data_general_3(list_data_3):
    print("##### add skill #########")
    for row in list_data_3:
        cr.execute(
            f"insert into data_operations (user_Ip,user_email,events,events_time) values ('','','{row[3]}','{row[1]}')")
        cr.execute(
            f"insert into Department (name_Dep) values ('{row[2]}')")
        cr.execute(f"insert into users (name_users) values ('{row[4]}')")
    commit_and_close()


# in the line 1- time , 2- Department , 3- event , 4- user , 5- Ip , 6- Email
def add_data_general_4(list_data_4):
    print("##### add skill #########")
    for row in list_data_4:
        cr.execute(
            f"insert into error (user_ip,user_Email,Events,events_time) values ('{row[5]}','{row[6]}','{row[3]}','{row[1]}')")
        cr.execute(
            f"insert into Department (name_Dep) values ('{row[2]}')")
        cr.execute(f"insert into users (name_users) values ('{row[4]}')")
        logging.info(f"we have error ('{row[3]}') in the time ('{row[1]}')")
    commit_and_close()


def update_from_error_table():
    print("Enter the user Email : ", end=" ")
    user_Email = input()
    print("Enter the Ip Email : ", end=" ")
    IP = input()
    cr.execute(
        f"select * from error where Events =' Invalid Department' and user_ip = '{IP}'")
    cr.execute(
        f"update error set user_Email='{user_Email}' where user_ip = '{IP}'")
    commit_and_close()
