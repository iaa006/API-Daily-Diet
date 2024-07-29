from src.database import db
from datetime import datetime

class Meal():
    def __init__(self, name:str, description:str, date_time:str, on_diet:bool) -> None:
        self.name = name
        self.description = description
        self.date_time = datetime.strptime(date_time, "%d/%m/%Y %H:%M:%S")
        self.on_diet = on_diet 
    
    def meal_to_dict(self) -> dict:
        return {
            "name" :self.name,
            "description" : self.description,
            "date_time" : self.date_time,
            "on_diet" : self.on_diet
        }
    
    @staticmethod
    def to_dict(meal:list) -> dict:
        return {
            "name" :meal[1],
            "description" : meal[2],
            "date_time" : meal[3],
            "on_diet" : meal[4]
        }

    def create_meal(self) -> None:
        db.connect()
        cursor = db.get_connection().cursor()
        cursor.execute('''
        INSERT INTO Meal (name, description, date_time, on_diet) values
        (?, ?, ?, ?)''', (
            self.name,
            self.description,
            self.date_time,
            self.on_diet,
        ))
        db.get_connection().commit()

    @staticmethod
    def get_users() -> tuple:
        db.connect()
        cursor = db.get_connection().cursor()
        cursor.execute('''
        SELECT * FROM Meal    
        ''')

        return cursor.fetchall()
    
    @staticmethod
    def get_user(id:int) -> tuple:
        db.connect()
        cursor = db.get_connection().cursor()
        cursor.execute('''
            Select * from Meal where id = ?
        ''', (id,))

        return cursor.fetchone()
    
    @staticmethod
    def update_user(id:int, data:dict) -> None:
        db.connect()
        cursor = db.get_connection().cursor()
        
        if data['name']:
            cursor.execute(f'''Update Meal set name = '{data['name']}' where id = {id}''')
            db.get_connection().commit()
        if data['description']:
            cursor.execute(f'''Update Meal set description = '{data['description']}' where id = {id}''')
            db.get_connection().commit()
        if data['date_time']:
            date = datetime.strptime(data['date_time'], "%d/%m/%Y %H:%M:%S")
            print(f'''Update Meal set date_time = DATETIME('{date}') where id = {id}''')
            cursor.execute(f'''Update Meal set date_time = DATETIME('{date}') where id = {id}''')
            db.get_connection().commit()
        if data['on_diet']:
            cursor.execute(f'''Update Meal set on_diet = {data['on_diet']} where id = {id}''')
            db.get_connection().commit()


    @staticmethod
    def delete_user(id:int) -> None:
        db.connect()
        cursor = db.get_connection().cursor() 
        cursor.execute('''Delete from Meal where id = ?''', (id,))   
        db.get_connection().commit()