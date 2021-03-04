from dp_query import add_data_general_1
from dp_query import add_data_general_2
from dp_query import add_data_general_3
from dp_query import add_data_general_4
from dp_query import add_data_general_3
from dp_query import show_data_1
from dp_query import update_from_error_table
import sqlite3
import re
import logging
import itertools
import os

# الاسم : صهيب أسامة عبد الحميد جروان

os.chdir(os.path.dirname(os.path.abspath(__file__)))
logging.basicConfig(filename=r"C:\Users\hp\Desktop\my_project\script_log.log", format='%(asctime)s %(message)s',
                    datefmt='%b %d %H:%M:%S', level=logging.INFO)
exec(open(r"C:\Users\hp\Desktop\my_project\dp_creat.py").read())
dataBase = sqlite3.connect(r"C:\Users\hp\Desktop\my_project\db_login.db")
logging.info("connect with data base (db_login.db)\n")


def commit_and_close():
    dataBase.commit()


cr = dataBase.cursor()
logging.info(
    "we create a new two tables Department & users & data_operations & error")
file_read = open(r"C:\Users\hp\Desktop\my_project\login_op.log")
logging.info("we open the file login_op.log\n")
Str_1 = str(file_read.readlines())
logging.info("we open the file login_op.log and we read it\n")
# print(Str_1)
print("&" * 100)

# in the line 1- time , 2- Department , 3- event , 4- user , 5- Ip , 6- Email
search_events_1 = re.findall(
    r"(([A-Z]+\w+\s+\d+\s+\d+\:+\d+\:+\d+\s)+(\w+\s)+\w+\W+\d\d\d\d+\W+\:+( Accepted password| Invalid user/password| Invalid User/Password) +[A-z0-9]+(\s+[A-z0-9]+\s)+[A-z0-9]+\s+(\d+\.+\d+\.+\d+\.+\d)+\s+[A-z0-9]+\s+([A-z0-9]+@+\w+\.+com))", Str_1)  # for the one digit .
results_1 = search_events_1
# in the line 1- time , 2- Department , 3-event , 4- Email , 5-user , 6- IP
tabe = re.findall(r"(([A-Z]+\w+\s+\d+\s+\d+\:+\d+\:+\d+\s)+(\w+\s)+\w+\W+\d\d\d\d+\W+\:+( Accepted password| Invalid user/password| Invalid User/Password) +[A-z0-9]+(\s+[A-z0-9]+\s)+[A-z0-9]+\s+(\d+\.+\d+\.+\d+\.+1[0-2])+\s+[A-z0-9]+\s+([A-z0-9]+@+\w+\.+com))", Str_1)  # for the number from 10 to 12
results_1.extend(tabe)
search_events_2 = re.findall(
    r"(([A-Z]+\w+\s+\d+\s+\d+\:+\d+\:+\d+\s)+(\w+\s)+\w+\W+\d\d\d\d+\W+\:+( Accepted password for| Invalid Admin User)+\s(([A-z0-9]+)@+Admin+\s)+\w+\s+(\d+\.+\d+\.+\d+\.+\d+))", Str_1)  # for the option four and six
results_2 = search_events_2  # 6 option

# in the line we get 1- time , 2- Department , 3-event , 4- user
search_events_3 = re.findall(
    r"(([A-Z]+\w+\s+\d+\s+\d+\:+\d+\:+\d+\s)+(\w+\s)+\w+\W+\d\d\d\d+\W+\:+( session closed for user| session opened for user)+\s+([A-z0-9]+\s))", Str_1)
results_3 = search_events_3  # option 2

# in the line 1- time , 2- Department , 3- event , 4- user , 5- Ip , 6- Email
search_error_1 = re.findall(
    r"(([A-Z]+\w+\s+\d+\s+\d+\:+\d+\:+\d+\s)+(\w+\s)+\w+\W+\d\d\d\d+\W+\:+( Invalid user/password| Invalid User/Password)+\s+\w+\s+([A-z0-9]+\s)+\w+(\s+\d+\.+\d+\.+\d+\.+\d[3-9]\s)+\w+\s+([A-z0-9]+@+\w+\.+\w+))", Str_1)
results_error_1 = search_error_1

# for the three number in the last of the IP
search_error_1_2 = re.findall(
    r"(([A-Z]+\w+\s+\d+\s+\d+\:+\d+\:+\d+\s)+(\w+\s)+\w+\W+\d\d\d\d+\W+\:+( Invalid user/password| Invalid User/Password)+\s+\w+([A-z0-9]+\s)+\w+\s+(\d+\.+\d+\.+\d+\.+\d\d\d\s)+\w+\s+([A-z0-9]+@+\w+\.+\w+))", Str_1)
results_error_1.extend(search_error_1_2)

# in the line 1- time , 2- Department , 3- event , 4- user , 5- Ip , 7- Email
search_error_2 = re.findall(
    r"(([A-Z]+\w+\s+\d+\s+\d+\:+\d+\:+\d+\s)+(\w+\s+)\w+\W+\d\d\d\d+\W+\:+( Invalid Department)+\s+\w+\s+(\w+\s)+\w+\s+(\d+\.+\d+\.+\d+\.+\d+)+\s+\w+\s+(\w+@+\w+\.+\w+))", Str_1)
results_error_2 = search_error_2
results_error_2.extend(results_error_1)
print(results_error_2)
logging.info("we finised extract the important data and the Errors.\n")

add_data_general_1(results_1)

add_data_general_2(results_2)

add_data_general_3(results_3)

add_data_general_4(results_error_2)

# show_data_1(results_1)

update_from_error_table()

commit_and_close()
cr.close()
# (([A-Z]+\w+\s+\d+\s+\d+\:+\d+\:+\d+\s)+(\w+\s)+\w+\W+\d\d\d\d+\W+\:+( Invalid user/password| Invalid Admin User| Invalid User/Password) +[A-z0-9]+\s+([A-z0-9]+\s)+[A-z0-9]+(\s+\d+\.+\d+\.+\d+\.+(1[3-9]\s|\d\d\d\s|[2-9][0-9]\s))+\w+\s+(\w+@+\w+\.+\w+\s))
# \.+(1[3-9]|2[0-9]|\d\d\d)+\s
