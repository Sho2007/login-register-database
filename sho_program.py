import mysql.connector
import random
import sys
import datetime
import sys
from time import sleep
import time

current_time = datetime.datetime.now().strftime('%H:%M:%S')

number_whitelist = random.randint(22072007,70020722)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sho_data"
)

data = [] # for get the data user pass # [('Sho', 'Sho22072007'), ('Shoyashi', 'shoya')]
data_whitelist = []
mycursor = mydb.cursor()

def register():
  global data_whitelist
  global data_text_whitelist
  #put whitelist number
  f = open("whitelist.txt", "w")
  f.write(str(number_whitelist))
  f.close()
  #get whitelist number
  with open('whitelist.txt') as f:
      data_text_whitelist = f.read()  # Get data whitelist from this [23444354....]
      #print(contents)
  #------------------------------
  Username = input("["+current_time+"]" +" Username: ")
  Password = input("["+current_time+"]" +" Password: ")
  sql = "INSERT INTO user_data (User, Pass, Whitelist_Number) VALUES (%s, %s, %s)"
  val = (Username,Password,data_text_whitelist)
  mycursor.execute(sql, val)
  mydb.commit()
  words1 = ("["+current_time+"] " +mycursor.rowcount, "inserted data BY.SHO\n")
  for char in words1:
      sleep(0.03)
      sys.stdout.write(char)
      sys.stdout.flush()

# get data zone
mycursor.execute("SELECT User , Pass FROM user_data")
myresult = mycursor.fetchall()
for x in myresult:
  data.append(x)

#print(len(data))
#for i in range(len(data)):
#print(str(data[1][0]) +" "+ str(data[1][1])) #get user & pass

def login():
  username_login = input("["+current_time+"]" +" Username: ")
  password_login = input("["+current_time+"]" +" Password: ")
  mycursor.execute("SELECT User , Pass FROM user_data")
  myresult = mycursor.fetchall()
  for x in myresult:
    data.append(x)
  #print(data) # [('Sho', 'Sho22072007'), ('Shoyashi', 'shoya')]

  countnum_login = 0
  count_error_login = 0
  
  while countnum_login == 0:
    for i in range(len(data)):
      if username_login == data[i][0]:
        if password_login == data[i][1]:
          words2 = ("["+current_time+"]" +" Successfully :D\n")
          for char in words2:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        else:
          words3 = ("["+current_time+"]" +" Wrong Password :(\n")
          for char in words3:
            sleep(0.03)
            sys.stdout.write(char)
            sys.stdout.flush()
          time.sleep(100)
          quit()
      else:
        count_error_login += 1
    break # when end for loop
  if count_error_login == len(data): # for wrong user and passowrd
    words4 = ("["+current_time+"]" +' Username or Password is Wrong :(\n')
    for char in words4:
      sleep(0.03)
      sys.stdout.write(char)
      sys.stdout.flush()
    time.sleep(100)
    quit()

  # get the whitelist
  #mycursor.execute("SELECT Whitelist_Number	 FROM user_data")
  #myresult = mycursor.fetchall()
  #for x in myresult:
    #data_whitelist.append(x)

# select menu function
def select_menu_login_register():
    print("""
   LOGIN & REGISTER
    _______________
   |               |
   | [1] Login     |    BY. $H0
   | [2] Register  |
   |_______________|
    """)
    select_num_login_register = int(input("["+current_time+"]" + " Typing the menu number: "))
    if select_num_login_register == 1:
        login()
    elif select_num_login_register == 2:
        register()

# Working zone

select_menu_login_register()
#checking whitelist
check_data_whitelist_number = []
mycursor.execute("SELECT Whitelist_Number FROM user_data")
myresult = mycursor.fetchall()
for x in myresult:
  check_data_whitelist_number.append(x)

#print(check_whitelist_number)  # [('22072007',), ('70020722',), ('30020721',), ('27076001',), ('22335744',), ('34325654',)]

with open('whitelist.txt') as f:
      check_text_whitelist = f.read()
for i in range(len(check_data_whitelist_number)):
  if check_text_whitelist in check_data_whitelist_number[i]:
    words5 = ("["+current_time+"]" +' success\n')
    for char in words5:
      sleep(0.03)
      sys.stdout.write(char)
      sys.stdout.flush()
    time.sleep(1100)   # Test
  else:
     print("Wrong whitelist")
     time.sleep(1100)
     quit() # out from program

time.sleep(1100)