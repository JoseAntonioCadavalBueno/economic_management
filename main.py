# coding=utf-8
'''
Created on 27 feb 2022

@author: cadaval
'''
from method import insertLine, insertLineManagement, deleteLine, modifyLine, consultBoard

if __name__ == '__main__':
    
    print("which table you want to access? \ncost_center\naccounting account\nenterprise\nmanagement\nunit")
    
    board = input()
    
    print("what you want to do?: \nwrite what corresponds \n1: Insert a new line \n2: Delete a line \n3: Modify a line \n4: consult a board")
    
    menu = input()
    
    if(board != "gestion"):
        if(menu == "1"):
            insertLine(board)
        elif(menu == "2"):
            deleteLine(board)
        elif(menu == "3"):
            modifyLine(board)
        elif(menu == "4"):
            consultBoard(board)
    else:
        if(menu == "1"):
            insertLineManagement()
        elif(menu == "2"):
            deleteLine(board)
        elif(menu == "3"):
            modifyLine(board)
        elif(menu == "4"):
            consultBoard(board)
    pass