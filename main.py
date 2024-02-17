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


class Members:
    def main(root):
        def workout_history(id_num,data):
            #Creating a Frame
            frame = tk.Frame(root)
            frame.pack(side='top',expand=True,fill='both')

            #background Image
            path = r'C:\Users\Dell\Desktop\Project\Personal_Trainer\gallery\display.jpg'
            img = ImageTk.PhotoImage(Image.open(path))
            panel = tk.Label(root,image=img)
            panel.image = img
            panel.place(relheight=1,relwidth=1)

            #Gym Label
            gym_label = tk.Label(root,text='IRON  FITNESS  GYM',font=('Papyrus',18),background='Black',fg='White')
            gym_label.place(x=(int(700-gym_label.winfo_reqwidth())/2))

            #gym moto label
            moto_label = tk.Label(root,text='Break Your Limits!',font=('Papyrus',12),background='Black',fg='White')
            moto_label.place(x=(int(700-moto_label.winfo_reqwidth())/2),y=45)

            #workout history
            history = Features.get_history(id_num=id_num)
            history = [str(x) for x in history]
            final_history = "\n\n".join(history)
            history_label = tk.Message(root,text=final_history,background='Black',fg='White',font=10,width=700)
            history_label.place(x=0,y=100)

            #back Button
            back_button = tk.Button(root,text="Back",font=('Denmark',12),background='Black',fg='White',command=lambda : [print_member_details(data=data),Features.delete_widget([history_label,back_button])])
            back_button.place(x=600,y=300)


        def display_workout(res,data,workout_button,part=None):
            #Remove Button after click
            workout_button.place_forget()

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
                cd_label_2 =tk.Label(root,text=cd,background='Black',fg='White',font=10,justify='left')
                cd_label_2.place(x=300,y=310)

            #print button
            print_button = tk.Button(root,text='Print Workout',font=('Denmark',10),background='Black',fg='White',command=lambda: Features.print_doc(result_dict=res,data=data['Name'],part=part))
            print_button.place(x=550,y=350)

            #back Button
            back_button = tk.Button(root,text="Back",font=('Denmark',12),background='Black',fg='White',command=lambda : [print_member_details(data=data),Features.delete_widget([back_button,wt_label,cd_label_2,wt2_label,cd_label,print_button])])
            back_button.place(x=600,y=300)


        def print_member_details(data):
            #greet Button
            part_dict = {'1':'Chest-Triceps','2':'Back-Biceps','3':'Shoulders-Legs'}
            greet = tk.Label(root,text=f"Hi, Welcome Back",background='black',fg='White',font=18)
            greet.place(x=int((700-greet.winfo_reqwidth())/2),y=80)
            final_data = f"  Name : {data['Name']}   id_num : {data['id_num']}   Phone Number : 9876543210\nAge : {data['Age']}   Address : Udaipur  Schedule : {part_dict[data['Day']]}"
            member_data_label = tk.Message(root,text=final_data,font=('Denmark',13),background='Black',fg='White',width=700,justify='center')
            member_data_label.place(x=int((700-member_data_label.winfo_reqwidth())/2),y=110)

            #Create Object for member
            member = WorkoutPlan()
            res,part = member.get_workout(member_details=data)

            #Generate workout button
            workout_button = tk.Button(root,text="Generate Workout",font=('Denmark',15),background='Black',fg='White',command=lambda : [display_workout(res,data=data,part=part,workout_button=workout_button),Features.delete_widget([history_button])])
            workout_button.place(x=int(700/4-workout_button.winfo_reqwidth()/2),y=200)

            #Check Workout History button
            history_button = tk.Button(root,text='Workout History',font=('Denmark',15),background='Black',fg='White',command=lambda: workout_history(id_num=data["id_num"],data=data))
            history_button.place(x=int(700*3/4-history_button.winfo_reqwidth()/2),y=200)


        def get_input(panel):
            member_id = myentry.get()
            if member_id:
                button.place_forget() #remove button after click
                button.place_forget() #remove button after click
                entry_label.place_forget() #remove entry label
                myentry.place_forget() #remove entry box
                path = r'C:\Users\Dell\Desktop\Project\Personal_Trainer\gallery\display.jpg'
                img = ImageTk.PhotoImage(Image.open(path))
                panel.configure(image=img)
                panel.image = img
                member_details = member_data.get_member_details(id_num=member_id)
                print_member_details(member_details)


        #Home Image
        path = r'C:\Users\Dell\Desktop\Project\Personal_Trainer\gallery\home.png'
        img = ImageTk.PhotoImage(Image.open(path))
        panel = tk.Label(root,image=img)
        panel.image = img
        panel.place(relheight=1,relwidth=1)

        #Gym Label
        gym_label = tk.Label(root,text='IRON  FITNESS  GYM',font=('Papyrus',18),background='Black',fg='White')
        gym_label.place(x=(int(700-gym_label.winfo_reqwidth())/2))

        #gym moto label
        moto_label = tk.Label(root,text='Break Your Limits!',font=('Papyrus',12),background='Black',fg='White')
        moto_label.place(x=(int(700-moto_label.winfo_reqwidth())/2),y=45)

        #Member_id entry
        myentry = tk.Entry(root,bg='#434343',fg='White')
        myentry.place(x=350,y=100)

        #Entry Label
        entry_label = tk.Label(root,text='Enter Your ID',font=('Arial',10),background='Black',fg='White')
        entry_label.place(x=240,y=100)

        #Login Button
        button = tk.Button(root,text="Login",font=('Denmark',10),background='Black',fg='White',command=lambda : get_input(panel))
        button.place(x=int((700-button.winfo_reqwidth())/2),y=125)


class Trainer:
    def main(root):
        def get_input(panel):
            password = myentry.get()
            if password == 'A':
                frame.destroy()
                new_frame = tk.Frame(root)
                new_frame.pack(side='top',expand=True,fill='both')
                path = r'C:\Users\Dell\Desktop\Project\Personal_Trainer\gallery\display.jpg'
                img = ImageTk.PhotoImage(Image.open(path))
                panel = tk.Label(root,image=img)
                panel.image = img
                panel.place(relheight=1,relwidth=1)

                #Gym Label
                gym_label = tk.Label(root,text='IRON  FITNESS  GYM',font=('Papyrus',18),background='Black',fg='White')
                gym_label.place(x=(int(700-gym_label.winfo_reqwidth())/2))

                #gym moto label
                moto_label = tk.Label(root,text='Break Your Limits!',font=('Papyrus',12),background='Black',fg='White')
                moto_label.place(x=(int(700-moto_label.winfo_reqwidth())/2),y=45)

            else:
                wrong_pass_label = tk.Label(root,text="Wrong Password. Try Again",font=('Arial',10),background='Black',fg='Red')
                wrong_pass_label.place(x=int((700-wrong_pass_label.winfo_reqwidth())/2),y=150)



        #Creating a Frame
        frame = tk.Frame(root)
        frame.pack(side='top',expand=True,fill='both')

        #Home Image
        path = r'C:\Users\Dell\Desktop\Project\Personal_Trainer\gallery\home.png'
        img = ImageTk.PhotoImage(Image.open(path))
        panel = tk.Label(root,image=img)
        panel.image = img
        panel.place(relheight=1,relwidth=1)

        #Gym Label
        gym_label = tk.Label(root,text='IRON  FITNESS  GYM',font=('Papyrus',18),background='Black',fg='White')
        gym_label.place(x=(int(700-gym_label.winfo_reqwidth())/2))

        #gym moto label
        moto_label = tk.Label(root,text='Break Your Limits!',font=('Papyrus',12),background='Black',fg='White')
        moto_label.place(x=(int(700-moto_label.winfo_reqwidth())/2),y=45)

        #Member_id entry
        myentry = tk.Entry(root,show='*',bg='#434343',fg='White')
        myentry.place(x=350,y=100)

        #Entry Label
        entry_label = tk.Label(root,text='Enter Password',font=('Arial',10),background='Black',fg='White')
        entry_label.place(x=240,y=100)

        #Login Button
        button = tk.Button(root,text="Login",font=('Denmark',10),background='Black',fg='White',command=lambda : get_input(panel))
        button.place(x=int((700-button.winfo_reqwidth())/2),y=125)



def home(root):
    #Home Screen
    path = r'C:\Users\Dell\Desktop\Project\Personal_Trainer\gallery\home.png'
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(root,image=img)
    panel.image = img
    panel.place(relheight=1,relwidth=1)
    
    #Gym Label
    gym_label = tk.Label(root,text='IRON  FITNESS  GYM',font=('Papyrus',18),background='Black',fg='White')
    gym_label.place(x=(int(700-gym_label.winfo_reqwidth())/2))

    #gym moto label
    moto_label = tk.Label(root,text='Break Your Limits!',font=('Papyrus',12),background='Black',fg='White')
    moto_label.place(x=(int(700-moto_label.winfo_reqwidth())/2),y=45)

    #Member Login
    button = tk.Button(root,text="Member Login",font=('Denmark',13),background='Black',fg='White',command=lambda : Members.main(root))
    button.place(x=int(700/4-button.winfo_reqwidth()/2),y=125)

    #Trainer Login
    button = tk.Button(root,text="Trainer Login",font=('Denmark',13),background='Black',fg='White',command=lambda:Trainer.main(root))
    button.place(x=int(700*3/4-button.winfo_reqwidth()/2),y=125)


def main():
    #Action of the Generate Workout button
    root = tk.Tk()
    root.title("Iron Fitness Gym")
    root.geometry("700x400")
    home(root)

    root.mainloop()


if __name__ == "__main__":
    main()