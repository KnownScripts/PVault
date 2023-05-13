from pymongo_get_database import get_db

defs = {"_id" : "ACCOUNTS","USERNAME": '',"EMAIL": '',"PASSWORD": ''}

def printdata():
    dbname = get_db()
 
    # Create a new collection
    collection_name = dbname["fivem"]
    
    item_details = collection_name.find()
    for item in item_details:
        # This does not give a very readable output
        print(item)

def endata():
    inp1 = input("Enter your username: ")
    inp2 = input("Enter your email: ")
    inp3 = input("Enter your password: ")

    defs.update({"USERNAME":inp1})
    defs.update({"EMAIL":inp2})
    defs.update({"PASSWORD":inp3})
    send()
    menu()


def getdata():
    user = input("Get your data: ")


def send():
    dbname = get_db()
    collection_name = dbname["fivem"]
    collection_name.insert_many([defs])



def menu():
    print("""

    1.Get your data
    2.Enter your data
    """)

    kasutaja = input("Sisesta valikud: ")
    
    while True:
        if kasutaja == '1':
            printdata()
            menu() 
        elif kasutaja == '2':
            endata()
        else:
            print("Valige vähemalt 1 valikutest")
menu()        
    