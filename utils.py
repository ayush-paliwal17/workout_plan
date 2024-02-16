import os
import json
import tempfile
import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
import sqlite3
from datetime import date
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
        if result:
            member = {
                "id_num" : id_num,
                "Name" : result[1],
                "Age" : result[2],
                "Day" : result[5],
                "Cardio" : result[3],
                "Batch" : result[4]
                    }
            return member
        else:
            print("Invalid Member ID")


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

class Features:
    def print_doc(result_dict,name,part):

        #Initialize The Document
        doc = docx.Document()

        #Page Heading
        # head = doc.add_heading(level = 0).add_run("IRON FITNESS GYM")
        head = doc.add_heading(level = 0)
        head.alignment = WD_ALIGN_PARAGRAPH.CENTER
        head = head.add_run("IRON FITNESS GYM")
        font = head.font
        font.size = Pt(40)

        #Greeting
        para = doc.add_paragraph().add_run(f"Hi {name},\nToday we will be training {part}")
        font = para.font
        font.size = Pt(20)

        #Weight Training
        wt_head = doc.add_heading(level =1).add_run("Weight Training :")
        font = wt_head.font
        font.size = Pt(20)

        for item in result_dict['Weight_Training']:
            para = doc.add_paragraph(style = 'List Number').add_run(item)
            font = para.font
            font.size = Pt(18)

        #Cardio
        cardio = result_dict.get('Cardio')
        if cardio:
            cardio_head = doc.add_heading(level = 1).add_run("Cardio : ")
            font = cardio_head.font
            font.size = Pt(20)    

            for item in cardio:
                para = doc.add_paragraph(style='List Number').add_run(item)
                font = para.font
                font.size = Pt(18)

        #Open Temp file
        filename = tempfile.mktemp(".doc")
        doc.save(filename)
        os.startfile(filename)

    def add_history(id_num,workout):

        t_date = str(date.today())

        with open("workout_history.json") as f:
            fi_data = json.load(f)


        queue = fi_data[id_num]
        queue.append({t_date : workout})
        for i in range(10):
            if len(queue)>3:
                queue.pop(0)

        fi_data[id_num] = queue        
        with open("workout_history.json",'w') as f:
            json.dump(fi_data,f)


    def get_history(id_num):
        with open("workout_history.json") as f:
            fi_data = json.load(f)
        queue = fi_data[id_num]
        return queue