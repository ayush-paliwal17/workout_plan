import sqlite3

connnection = sqlite3.connect('gym_data.db') #connect to a local database, create a new one if it dosen't exist

cursor = connnection.cursor() #cursor allows us to execute sql commands, it is an interface between the database and sql.

class member_data:

    def create_table():
        cursor.execute(f"CREATE TABLE IF NOT EXISTS member_data(id_num PRIMARY KEY ,name,age,day,cardio,batch)")


    def add_member(member_details):
        cursor.execute(f"INSERT INTO member_data VALUES {member_details}")
        connnection.commit()


    def get_member_details(id_num):
        cursor.execute(f"""
            SELECT * from member_data
            where id_num = {id_num}
        """)
        result = cursor.fetchone()

        member = {
            "id_num" : id_num,
            "name" : result[1],
            "age" : result[2],
            "day" : result[3],
            "cardio" : result[4],
            "batch" : result[5]
                }
        
        return member
