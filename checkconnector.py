'''
Created on 27 feb 2022

@author: cadaval
'''
import mysql.connector

db = mysql.connector.connect(host="localhost", user="username", 
passwd="password", database="name")
print(db)
