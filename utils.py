import sqlite3

connnection = sqlite3.connect('gym_data.db') #connect to a local database, create a new one if it dosen't exist

cursor = connnection.cursor() #cursor allows us to execute sql commands, it is an interface between the database and sql.

class member_data:

    def create_table():
        cursor.execute("CREATE TABLE IF NOT EXISTS member_data(id_num PRIMARY KEY ,name,age,cardio,batch,day)")
        print('Table Created')


    def add_member(member_details):
        cursor.execute(f"INSERT INTO member_data VALUES {member_details}")
        connnection.commit()


    def get_member_details(id_num):
        cursor.execute(f"""
            SELECT * from member_data
            where id_num = '{id_num}'
        """)
        result = cursor.fetchone()

        member = {
            "id_num" : id_num,
            "Name" : result[1],
            "Age" : result[2],
            "Day" : result[5],
            "Cardio" : result[3],
            "Batch" : result[4]
                }
        
        return member


    def get_all_members():
        cursor.execute(f"""
            SELECT * from member_data
        """)
        result = cursor.fetchall()

        return result

    
    def update_column(key,value,id_value):
        cursor.execute(f"""
            UPDATE member_data
            SET {key} = '{value}'
            WHERE id_num = '{id_value}'
        """)
        connnection.commit()

class Workout:
    def get_weight_training(ex_id):
        cursor.execute(f"""
            SELECT * from weight_training
            WHERE ex_id = '{ex_id}'
        """)
        result = cursor.fetchone()
        weight_training = [x for x in result[1:]]
        return weight_training

    def get_cardio(ex_id):
        cursor.execute(f"""
            SELECT * from cardio
            where ex_id = {ex_id}
        """)
        result = cursor.fetchone()
        cardio = [x for x in result[1:]]
        return cardio

# member_data.update_column(key='Day',value='3',id_value='1')
# print(member_data.get_all_members())
# cursor.execute("""
#         UPDATE member_data
#         SET 'day' = '1'
#         where id_num = '1'
# """)
# print(member_data.get_all_members())