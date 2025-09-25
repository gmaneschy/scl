import mysql.connector
import forms

mydb = mysql.connector.connect(host="localhost", user="root", passwd="escola", database="escola")
mycursor = mydb.cursor()

def cadastrar_professores():
    pass