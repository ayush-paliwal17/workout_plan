from utils import *
import tkinter as tk
from PIL import Image,ImageTk

class weight_training:
    def circuit(self,member_details):
        if member_details["Batch"] == "A":
            member_data.update_column(key='Batch',value='B',id_value=member_details['id_num'])
            return(Workout.get_weight_training(ex_id=0.1))

        elif member_details["Batch"] == "B":
            member_data.update_column(key='Batch',value='A',id_value=member_details['id_num'])
            member_data.update_column(key='Day',value='1',id_value=member_details['id_num'])
            return(Workout.get_weight_training(ex_id=0.2))


    def chest_triceps(self,member_details):
        if member_details["Batch"] == "A":
            return (Workout.get_weight_training(ex_id=1.1))
        elif member_details["Batch"] == "B":
            return (Workout.get_weight_training(ex_id=1.2))
        else:
            return (Workout.get_weight_training(ex_id=1.3))


    def back_biceps(self,member_details):
        if member_details["Batch"] == "A":
            return (Workout.get_weight_training(ex_id=2.1))
        elif member_details["Batch"] == "B":
            return (Workout.get_weight_training(ex_id=2.2))
        else:
            return (Workout.get_weight_training(ex_id=2.3))


    def shoulders_legs(self,member_details):
        if member_details["Batch"] == "A":
            member_data.update_column(key='Batch',value='B',id_value=member_details['id_num'])
            return (Workout.get_weight_training(ex_id=3.1))
        elif member_details["Batch"] == "B":
            member_data.update_column(key='Batch',value='C',id_value=member_details['id_num'])
            return (Workout.get_weight_training(ex_id=3.2))
        else:
            member_data.update_column(key='Batch',value='A',id_value=member_details['id_num'])
            return (Workout.get_weight_training(ex_id=3.3))


class WorkoutPlan(weight_training):
    def circuit(self,member_details):
        return {"Weight_Training" : super().circuit(member_details), "Cardio" : Workout.get_cardio(ex_id=1)} if member_details["Cardio"] == "Yes" else {"Weight_Training" : super().circuit(member_details)}

    def chest_triceps(self,member_details):
        return {"Weight_Training" : super().chest_triceps(member_details), "Cardio" : Workout.get_cardio(ex_id=2)} if member_details["Cardio"] == "Yes" else {"Weight_Training" : super().chest_triceps(member_details)}
    
    def back_biceps(self,member_details):
        return {"Weight_Training" : super().back_biceps(member_details), "Cardio" : Workout.get_cardio(ex_id=3)} if member_details["Cardio"] == "Yes" else {"Weight_Training" : super().back_biceps(member_details)}
    
    def shoulders_legs(self,member_details):
        return {"Weight_Training" : super().shoulders_legs(member_details), "Cardio" : Workout.get_cardio(ex_id=4)} if member_details["Cardio"] == "Yes" else {"Weight_Training" : super().shoulders_legs(member_details)}

    
    def get_workout(self,member_details):
        if member_details["Day"] == '0':
            part = 'Cardio'
            workout = WorkoutPlan.circuit(self,member_details)
        elif member_details["Day"] == '1':
            part = "Chest and Triceps"
            member_data.update_column(key='Day',value='2',id_value=member_details['id_num'])
            workout = WorkoutPlan.chest_triceps(self,member_details)
        elif member_details["Day"] == '2':
            part = "Back and Biceps"
            workout = WorkoutPlan.back_biceps(self,member_details)
            member_data.update_column(key='Day',value='3',id_value=member_details['id_num'])
        elif member_details["Day"] == '3':
            part = "Shoulders and Legs"
            member_data.update_column(key='Day',value='1',id_value=member_details['id_num'])
            workout = WorkoutPlan.shoulders_legs(self,member_details)
        
        return workout,part


def main():
    #Action of the Generate Workout button
    root = tk.Tk()
    root.title("Iron Fitness Gym")
    root.geometry("700x400")


    def display_workout(res,name,part=None):
        #greet Button
        greet = tk.Label(root,text=f"Hi {name}\n Today we will be training {part}",background='black',fg='White',font=18)
        greet.pack(pady=10)

        wt = res['Weight_Training']
        wt_str = '\n'.join(wt)
        cardio = res.get('Cardio')


        #weight training label
        wt_label =tk.Label(root,text=f"Weight Training : ",background='Black',fg='White',font=10,justify='left')
        wt_label.place(x=150,y=150)
        wt2_label =tk.Label(root,text=wt_str,background='Black',fg='White',font=10,justify='left')
        wt2_label.place(x=300,y=150)

        #Cardio Label
        if cardio:
            cd = '\n'.join(cardio)
            cd_label =tk.Label(root,text=f"cardio: ",background='Black',fg='White',font=10,justify='left')
            cd_label.place(x=180,y=310)
            cd_label =tk.Label(root,text=cd,background='Black',fg='White',font=10,justify='left')
            cd_label.place(x=300,y=310)

        #print button
        print_button = tk.Button(root,text='Print Workout',font=('Denmark',10),background='Black',fg='White',command=lambda: Features.print_doc(result_dict=res,name=name,part=part))
        print_button.place(x=550,y=350)


    def get_input(panel):
        member_id = myentry.get()
        if member_id:
            button.place_forget() #remove button after click
            entry_label.place_forget() #remove entry label
            myentry.place_forget() #remove entry box
            path = r'C:\Users\Dell\Desktop\Project\Personal_Trainer\gallery\display.jpg'
            img = ImageTk.PhotoImage(Image.open(path))
            panel.configure(image=img)
            panel.image = img
            member_details = member_data.get_member_details(id_num=member_id)
            member = WorkoutPlan()    
            res,part = member.get_workout(member_details=member_details)
            display_workout(res,name=member_details['Name'],part=part)


    #Home Image
    path = r'C:\Users\Dell\Desktop\Project\Personal_Trainer\gallery\home.png'
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(root,image=img)
    panel.image = img
    panel.place(relheight=1,relwidth=1)

    #Gym Label
    gym_label = tk.Label(root,text='IRON  FITNESS  GYM',font=('Papyrus',18),background='Black',fg='White')
    gym_label.pack(pady=1)

    #gym moto label
    moto_label = tk.Label(root,text='Break Your Limits!',font=('Papyrus',12),background='Black',fg='White')
    moto_label.pack()

    #Member_id entry
    myentry = tk.Entry(root,bg='#434343',fg='White')
    myentry.place(x=350,y=100)

    #Entry Label
    entry_label = tk.Label(root,text='Enter Your ID',font=('Arial',10),background='Black',fg='White')
    entry_label.place(x=240,y=100)

    #Generate workout button
    button = tk.Button(root,text="Generate Workout",font=('Denmark',10),background='Black',fg='White',command=lambda : get_input(panel))
    button.place(x=290,y=125)

    root.mainloop()



if __name__ == "__main__":
    main()