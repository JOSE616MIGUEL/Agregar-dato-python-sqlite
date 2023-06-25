from tkinter import *
from tkinter import messagebox

import sqlite3

con = sqlite3.connect("db/agenda.sqlite3")

ventana = Tk()
ventana.title("Practica sqlite")
ventana.geometry("800x600")

def consulta():
    consulta = con.cursor()
    consulta.execute("SELECT * FROM agenda")
    datos = consulta.fetchall()
    for dato in datos:
        agenda.insert(INSERT,dato)
        agenda.insert(INSERT,"\n")

def agregar():
    cursor1 = con.cursor()
    lista = [(valor.get())]
    cursor1.execute('INSERT INTO agenda(nombre) values(?)', lista)
    con.commit()
    messagebox.showinfo("Datos agregados", "La información a sido actualizada")
    agenda.delete("1.0", END)
    consulta()
    

valor = StringVar()

etiqueta1 = Label(ventana, text="Excibe un nombre: ").place(x=20, y=20)
cajanombre = Entry(ventana, textvariable=valor).place(x=140, y=20)
botonagregar = Button(ventana, text="Agregar", command=agregar).place(x=270, y=17)

agenda = Text(ventana, width=80, height=15)
agenda.place(x=20, y=45)

consulta()
mainloop()