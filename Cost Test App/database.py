# this is the database class file

# modules
import sqlite3

class Database:
    def ConnectToDatabse():
        try:
            db = sqlite3.connect('cotizaciones.db')
            c = db.cursor()
            c.execute("""CREATE TABLE if not exists cotizaciones (id INTEGER PRIMARY KEY, N_cotizacion VARCHAR(255) NOT NULL,
            Cliente VARCHAR(255) NOT NULL, Rut VARCHAR(255) NOT NULL, Solicitud VARCHAR(255) NOT NULL, Descripcion VARCHAR(255),
            Fecha_creacion VARCHAR(255) NOT NULL, Neto INTEGER NOT NULL, Iva INTEGER NOT NULL, Estado BIT NOT NULL,
            Ganada BIT NOT NULL, Entregada BIT NOT NULL, Facturada BIT NOT NULL, Pagado BIT NOT NULL,
            Folio VARCHAR(255) NOT NULL, Fecha_factura VARCHAR(255) NOT NULL, Factoring VARCHAR(255))""")
            print("DATABASE CONNECTED")
            return db
        except Exception as e:
            print(e)
    
    def InsertDatabase(db, values):
        c = db.cursor()
        # also make sure to use ? for the inputs for security purposes
        c.execute("""INSERT INTO cotizaciones (N_cotizacion, Cliente, Rut, Solicitud, Descripcion, Fecha_creacion, Neto, Iva, Estado,
        Ganada, Entregada, Facturada, Pagado, Folio, Fecha_factura, Factoring) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", values)
        db.commit()
        print("QUOTE INSERTED INTO THE DATABASE")

    #TODO: ARREGLAR LAS FUNCIONES PARA LA BASE DE DATOS DE DPERIC LTDA
    def ReadDatabase(db):
        c = db.cursor()
        # make sure to name the columns and not SELECT * FROM...
        c.execute("""SELECT Task, Date FROM tasks""")
        records = c.fetchall()
        return records

    def DeleteDatabase(db, value):
        c = db.cursor()
        # quick note: here we're assuming that no two task description are the
        # same and as a result we are deleting based on task
        # an ideal app would not do this but instead delete based on the actual inmutable
        # database ID. but for the sake of the tutorial and length, we will do it this way...
        c.execute("DELETE FROM tasks WHERE Task=?", value)
        db.commit()

    def UpdateDatabase(db, value):
        c = db.cursor()
        c.execute("UPDATE tasks SET Task=? WHERE Task=?", value)
        db.commit()