import time
import logging
import random
import string
import struct
import socket
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))
logging.basicConfig(filename=r"C:\Users\hp\Desktop\my_project\login_op.log",
                    format='%(asctime)s %(message)s', datefmt='%b %d %H:%M:%S',  level=logging.INFO)
logging.info("Hallo World")


# 1: DateTime        #2: Department      #3:Session ID       #4:username     #5: IP      #6:email
users = {}
user_name = ["Ali", "Alaa", "Ahmed", "Mohammad", "Ameer", "Blal",
             "Ali2", "Alaa2", "Ahmed2", "Mohammad2", "Ameer2", "Blal2"]
departments = ["Management", "Marketing",
               "Finance", "Operations", "Sales", "Other"]
sid = range(1, 99999)
###########################  Genarate Random IP ##########################
#ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))##
##########################################################################
ip = ["10.20.30." + str(i+1) for i in range(len(user_name))]
email = [str(s).lower() + "@gamil.com" for s in user_name]

# This for to genarate a dict of users with a randome department
for i in range(len(user_name)):
    users[user_name[i]] = (departments[random.randint(
        0, len(departments)-1)], email[i], ip[i])

users = {
    'Ali':      ('Management',  'ali@gamil.com',        '10.20.30.1'),
    'Alaa':     ('Marketing',   'alaa@gamil.com',       '10.20.30.2'),
    'Ahmed':    ('Finance',     'ahmed@gamil.com',      '10.20.30.3'),
    'Mohammad': ('Operations',  'mohammad@gamil.com',   '10.20.30.4'),
    'Ameer':    ('Sales',       'ameer@gamil.com',      '10.20.30.5'),
    'Blal':     ('Other',       'blal@gamil.com',       '10.20.30.6'),
    'Ali2':     ('Operations',  'ali2@gamil.com',       '10.20.30.7'),
    'Alaa2':    ('Sales',       'alaa2@gamil.com',      '10.20.30.8'),
    'Ahmed2':   ('Management',  'ahmed2@gamil.com',     '10.20.30.9'),
    'Mohammad2': ('Other',       'mohammad2@gamil.com',  '10.20.30.10'),
    'Ameer2':   ('Marketing',   'ameer2@gamil.com',     '10.20.30.11'),
    'Blal2':    ('Finance',     'blal2@gamil.com',      '10.20.30.12')
}
print("#"*50)
print(users)
print("#"*50)

status = 0
end_time = time.time()
sidd = 0

while True:
    # while time.time() - end_time < 300:
    for user in users:
        sidd = sidd + 1 if sidd <= 99999 else 0
        stat = random.randint(0, 15)
        status = random.randint(1, 4)
        dep = users[user][0]
        eml = users[user][1]
        IP = users[user][2]

        if stat not in (1, 3, 2, 4):

            if status == 1:
                logging.info("{} sid[{:04d}]: Accepted password for {} from {} by {}".format(
                    dep, sidd, user, IP, eml))
                sidd = sidd + 1
                time.sleep(1)
                logging.info("{} sid[{:04d}]: session opened for user {} for sid2[{:04d}]".format(
                    dep, sidd, user, sidd-1))
                sidd = sidd + 1
                time.sleep(3)
                logging.info("{} sid[{:04d}]: session closed for user {} for sid2[{:04d}]".format(
                    dep, sidd, user, sidd-1))
            elif status == 2:
                logging.info(
                    "{} sid[{:04d}]: Invalid user/password for {} from {} by {}".format(dep, sidd, user, IP, eml))
            elif status == 3:
                dep = (set(departments) - {dep}).pop()
                logging.info(
                    "{} sid[{:04d}]: Invalid user/password for {} from {} by {}".format(dep, sidd, user, IP, eml))
            elif status == 4:
                if user in ("Ali", "Ahmed2"):
                    print("Inside status  #4  "*3)
                    logging.info(
                        "{} sid[{:04d}]: Accepted password for {}@admin from {} by {}".format(dep, sidd, user, IP, eml))
                    sidd = sidd + 1
                    time.sleep(1)
                    logging.info("{} sid[{:04d}]: session opened for user {} for sid2[{:04d}]".format(
                        dep, sidd, user, sidd-1))
                    sidd = sidd + 1
                    time.sleep(3)
                    logging.info("{} sid[{:04d}]: session closed for user {} for sid2[{:04d}]".format(
                        dep, sidd, user, sidd-1))

        elif stat in (1, 3):
            if status == 1:
                sidd = sidd + 1
                time.sleep(3)
                logging.info(
                    "{} sid[{:04d}]: session closed for user {}".format(dep, sidd+1, user))
            elif status == 2:
                logging.info("{} sid[{:04d}]: Invalid User or Password for {} from {} by {}".format(
                    dep, sidd, user, IP, eml))
            elif status == 3:
                dep = (set(departments) - {dep}).pop()
                logging.info("{} sid[{:04d}]: Invalid Department for {} from {} by {}".format(
                    dep, sidd, user, IP, eml.upper()))
            elif status == 4:
                if user in ("Ali", "Ahmed2"):
                    print("Inside status  #4  "*3)
                    logging.info(
                        "{} sid[{:04d}]: Accepted password for {}@Admin from {} By {}".format(dep, sidd, user, IP, eml))
                    sidd = sidd + 1
                    time.sleep(1)
                    logging.info("{} sid[{:04d}]: Session Opened for user {} for sid2[{:04d}]".format(
                        dep, sidd, user.lower(), sidd-1))
                    sidd = sidd + 1
                    time.sleep(3)
                    logging.info("{} sid[{:04d}]: session closed for user {}".format(
                        dep.lower(), sidd, user))
        elif stat in (2, 4):
            if status == 1:
                logging.info("{} sid[{:04d}]: Invalid User/Password for {} from {} by {}".format(
                    dep, sidd, user+"_qwe", IP, eml))
            elif status == 2:
                logging.info("{} sid[{:04d}]: Invalid User or Password for {} from {} by {}".format(
                    dep, sidd, user, IP, "qwe."+eml))
            elif status == 3:
                IP = socket.inet_ntoa(struct.pack(
                    '>I', random.randint(1, 0xffffffff)))
                logging.info("{} sid[{:04d}]: Invalid user/password for {} from {} by {}".format(
                    dep, sidd, user, IP, eml.upper()))
            elif status == 4:
                if user not in ("Ali", "Ahmed2"):
                    logging.info(
                        "{} sid[{:04d}]: Invalid Admin User {}@Admin from {} By {}".format(dep, sidd, user, IP, eml))
