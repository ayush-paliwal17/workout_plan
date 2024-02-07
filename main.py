from utils import *
import os
import tkinter as tk

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
            print("Cardio")
            workout = WorkoutPlan.circuit(self,member_details)
        elif member_details["Day"] == '1':
            print("Chest and Triceps")
            member_data.update_column(key='Day',value='2',id_value=member_details['id_num'])
            workout = WorkoutPlan.chest_triceps(self,member_details)
        elif member_details["Day"] == '2':
            print("Back and Biceps")
            workout = WorkoutPlan.back_biceps(self,member_details)
            member_data.update_column(key='Day',value='3',id_value=member_details['id_num'])
        elif member_details["Day"] == '3':
            print("Shoulders and Legs")
            member_data.update_column(key='Day',value='1',id_value=member_details['id_num'])
            workout = WorkoutPlan.shoulders_legs(self,member_details)
        
        return workout


def main():
    root = tk.Tk() #calls the constructor, root is now a window

    root.geometry("700x500") #set the width and height of the window
    root.title("My GUI") #set the title of the window

    myentry = tk.Entry(root)
    myentry.pack(padx=10,pady=5)

    def get_input():
        member_id = myentry.get()
        member_details = member_data.get_member_details(id_num=member_id)
        print(f"Hi {member_details['Name']}, Welcome Back.\nToday we will be training : ",end="")
        member = WorkoutPlan()    
        res = member.get_workout(member_details=member_details)
        print(res)
        
    button = tk.Button(root,text="Click Me!!",font=('Arial',16),command=get_input)
    button.pack(padx=5,pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()