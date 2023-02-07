from database import *

db = Database.ConnectToDatabase()
record = Database.LastRecord(db)
print(record)
# Database.UpdateDatabase(db, ("EPIC", record[1]), "Cliente")
