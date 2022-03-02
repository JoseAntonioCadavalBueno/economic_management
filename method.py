'''
Created on 27 feb 2022

@author: cadaval
'''
from checkconnector import db

def insertLine(board):
    
    data = []
    code = ""
    
    print("write the lines here: ")
    print("if you finished, write OK")
    
    while code != "OK":
        code = input("Code: ")
        if(code!="OK"):
            name = input("Name: ")
            l1 = [code, name]
            print(l1)
            data.append(l1.copy())
            l1.clear()
    
    for i in data:
        try:
            cursor = db.cursor()
            cursor.execute("INSERT INTO {0} VALUES ('{1}','{2}')".format(board,i[0], i[1]))
            db.commit()
            print("A new line has been added")
        except:
            print("An error has ocurred")
            db.rollback()
    db.close()

def insertLineManagement():
    
    data = []
    enum = ""
    
    print("write the lines here: ")
    print("if you finished, write OK")
    
    while enum != "OK":
        enum = input("Enumerate: ")
        if(enum!="OK"):
            date = input("Date: ")
            n_reference = input("Reference: ")
            n_bill = input("Bill: ")
            n_receipt = input("Receipt: ")
            code_e1 = input("Enterprise: ")
            code_c1 = input("Cost center: ")
            code_a1 = input("Accounting account : ")
            concept = input("Concept: ")
            quantity = input("Quantity: ")
            code_u1 = input("Unit: ")
            price = input("Price: ")
            
            l1 = [enum, date, n_reference, n_bill,
                  n_receipt, code_e1, code_c1,
                  code_a1, concept, quantity,
                  code_u1, price]
            
            print(l1)
            
            data.append(l1.copy())
            l1.clear()
    
    for i in data:
        try:
            cursor = db.cursor()
            cursor.execute("INSERT INTO management (enum, date, n_reference, n_bill, n_receipt, code_e1, code_c1, code_a1, concept, quantity, code_u1, price) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}')"
                     .format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]))
            db.commit()
            
            print("A new line has been added")
        except:
            print("An error has ocurred")
            
            db.rollback()
    db.close()

def deleteLine(board):
    consultBoard(board)
    
    print("Which one you want to delete?")
    key = input("code: ")
    
    if(board == "cost_center"):
        cod = "code_c"
    elif(board == "accounting account"):
        cod = "code_a"
    elif(board == "enterprise"):
        cod = "code_e"
    elif(board == "management"):
        cod = "id"
    elif(board == "unit"):
        cod = "code_u"
    
    try:
        cursor = db.cursor()
        cursor.execute("DELETE FROM {0} WHERE {1} = '{2}'".format(board, cod, key))
        db.commit()
        
        print("Deleted line")
        
        consultBoard(board)
    except():
        print("An error has ocurred")
            
        db.rollback()
    db.close()

def modifyLine(board):
    consultBoard(board)
    
    print("Which one you want to modify?")
    clave = input("code: ")
    
    if(board == "cost_center"):
        cod = "code_c"
    elif(board == "accounting account"):
        cod = "code_a"
    elif(board == "enterprise"):
        cod = "code_e"
    elif(board == "management"):
        cod = "id"
    elif(board == "unit"):
        cod = "code_u"
    
    value = input("Value you want to modify: ")
    newValue = input("Insert new value: ")
    
    try:
        cursor = db.cursor()
        cursor.execute("UPDATE {0} SET {1} = '{2}' WHERE {3} = '{4}'".format(board, value, newValue, cod, clave))
        db.commit()
        
        print("modified line")
        
        consultBoard(board)
    except():
        print("An error has ocurred")
            
        db.rollback()
    db.close()

def consultBoard(board):
    print("This is the contents of the table: ")
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM {0}".format(board))
    
    data = cursor.fetchall()
    
    for i in data:
        print(i)
