from pymongo_get_database import get_db
import random
import socket 
from random import randint
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)




compdata = {}




import os
#kausta asukoht/teekond
directory = "./Files"

def dire():
  if not os.path.exists(directory):
    os.makedirs(directory)
    print("Saved Accounts directory created!")

dire()

class Account():
  #määran konstruktoris klassi atribuudid
  def __init__(self, item):
    self.accounts = item
  #funktsioon kontojääki ülekirjutamiseks/uuendamiseks
  def deposit(self,item):
    self.balance += item
    print("Successfully deposited data")


def save_data():
    dbname = get_db()
 
   
    collection_name = dbname["DATA"]
    a = collection_name.find()


    for b in a:

        filename = 'accs.json'
        file = open(directory+"/"+filename,"a")
        file.write("\nAccount data:%s" %b)
        file.close()
        
        print("Account data saved")
        #menu()


def printdata():
    dbname = get_db()
 
    # Create a new collection
    collection_name = dbname["DATA"]
    
    item_details = collection_name.find()
    for item in item_details:
        # This does not give a very readable output
        print(item)
       

def endata():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    inp1 = input("Username: ")
    inp2 = input("Email: ")
    inp3 = input("Password: ")

    compdata.update({"_id": random.randrange(2, 10000)})
    
    compdata.update({"USERNAME": inp1})


    compdata.update({"EMAIL": inp2})



    compdata.update({"PASSWORD": inp3})


    compdata.update({"HOSTNAME": hostname})

    compdata.update({"ADDRESS": IPAddr})


    
    send()
    menu()





def send():
    dbname = get_db()
    collection_name = dbname["DATA"]
    collection_name.insert_many([compdata])


    

def menu():
    print("""

    1.Get your data
    2.Enter your data
    3.Save your data to an file
    """)

    u = input("Enter your options:  ")
    
    while True:
        if u == '1':
            printdata()
            menu() 
        elif u == '2':
            endata()
        elif u == '3':
            save_data()
            menu()
        else:
            print("Choose atleast one")
menu()






    