from utils import *
import tkinter as tk
from tkinter import ttk
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
            back_button = tk.Button(root,text="Back",font=('Denmark',10),background='Black',fg='White',command=lambda : [print_member_details(data=data),Features.delete_widget([history_label,back_button])])
            back_button.place(x=50,y=50)


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
            print_button = tk.Button(root,text='Print Workout',font=('Denmark',10),background='Black',fg='White',command=lambda: Features.print_doc(result_dict=res,name=data['Name'],part=part))
            print_button.place(x=550,y=350)

            #back Button
            back_button = tk.Button(root,text="Back",font=('Denmark',10),background='Black',fg='White',command=lambda : [print_member_details(data=data),Features.delete_widget([back_button,wt_label,cd_label_2,wt2_label,cd_label,print_button])])
            back_button.place(x=50,y=50)


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

            #Logout Button
            logout_button = tk.Button(root,text='LogOut',font=('Denmark',10),background='Black',fg='White',command= lambda:home(root))
            logout_button.place(x=600,y=350)

            #Generate workout button
            workout_button = tk.Button(root,text="Generate Workout",font=('Denmark',15),background='Black',fg='White',command=lambda : [display_workout(res,data=data,part=part,workout_button=workout_button),Features.delete_widget([history_button,logout_button])])
            workout_button.place(x=int(700/4-workout_button.winfo_reqwidth()/2),y=200)

            #Check Workout History button
            history_button = tk.Button(root,text='Workout History',font=('Denmark',15),background='Black',fg='White',command=lambda: workout_history(id_num=data["id_num"],data=data))
            history_button.place(x=int(700*3/4-history_button.winfo_reqwidth()/2),y=200)


        def get_input(panel):
            member_id = myentry.get()
            if member_id:
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

        #Back Button
        back_button = tk.Button(root,text='Back',font=('denmark',10),background='Black',fg='White',command=lambda:[home(root),Features.delete_widget([back_button])])
        back_button.place(x=50,y=50)

        #Login Button
        login_button = tk.Button(root,text="Login",font=('Denmark',10),background='Black',fg='White',command=lambda : [get_input(panel),Features.delete_widget([login_button,back_button,entry_label,myentry])])
        login_button.place(x=int((700-login_button.winfo_reqwidth())/2),y=125)


class Trainer:
    def main(root):
        def custom_workout():
            def exercises(part): 
                #instead of this we can have a sql table in a db
                exercise_combobox.set('')
                exer_dict = {"Chest" : (x for x in range(1,13)),
                            "Back" : ("Cable Lat Pull Down - Front","Cable Lat Pull Down - Back","Seated Cable Machine Rows","Cable Close Grip Pull Down","Machine Lat Pull Down","Machine Rows","Single Hand DB Rows","DB DeadLift","Bend over bar Rows","T-bar Rows","Cable Pullovers","Conventional Deadlifts"),
                            "Shoulders" : ("Snatch and press rod"," Front raise rod"," Lateral raise rod","Rear delts rod","Db Parallel grip front raise (Hold one hand)","DB Lateral raises (hold one)","DB rear delts","Arnold Press","Straight press","Standing rear delta + upright","Arnold","Shrugs"),
                            "Biceps" : ("Wide-Grip Cable Bicep Curls - EZ ROD","Close-Grip Cable Bicep Curls -EZ ROD","Cable Biceps Curls - Flat Rod","Cable Reverse Curls - Rod","Hanging Curls","Twisted Curls","Hammer Curls","Concentration Curls","Wide-Grip Rod Bicep Curls","Close-Grip Rod Bicep Curls","Mid-Grip rod Biceps Curls","Rod Reverse Curls"),
                            "Triceps" : (x for x in range(1,13)),
                            "Legs" : ("Squats","Ez bar lunges"," Wall sit"," Hamstring deadlift","DB Squats","DB chair Climb","DB hamstring deadlift","Calves","Leg press","Lunges dumbbell walking","Extension","Curls")
                            }

                exercise_combobox['values'] = exer_dict.get(part)


            def cardio(cardio_combobox):
                cardio_combobox.set('')
                cardio_combobox['values'] = ("WALK","Cross Trainer","Cycle","Mountain Climbs","Burpees","High Knees","Walk+Run","Crunch","Leg Raises","Plank")
                cardio_combobox.place(x=300,y=285)
                add_cardio_button.place(x=300+add_cardio_button.winfo_reqwidth(),y=310)


            def add_exercise_to_list():
                selection = exercise_combobox.get()
                exercise_combobox.set('')
                exercise_list.append(selection)
                exercise_combobox['values'] = [value for value in exercise_combobox["values"] if value != selection]
                part = body_combobox.get()
                part_list.append(part)


            def add_cardio_to_list():
                selection = cardio_combobox.get()
                cardio_combobox.set('')
                cardio_list.append(selection)
                cardio_combobox['values'] = [value for value in cardio_combobox['values'] if value != selection]


            def generate_custom_workout(name):

                res = {'Weight_Training': exercise_list, 
                        'Cardio': cardio_list}


                wt = exercise_list
                wt_str = '\n'.join(wt)
                cardio = cardio_list

                #creating a new frame
                frame = tk.Frame()
                frame.pack(side='top',expand=True,fill='both')

                #dispay image
                path = r"C:\Users\Dell\Desktop\Project\Personal_Trainer\gallery\display.jpg"
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

                #greet label
                greet_label = tk.Label(root,text=f"Hi Trainers,\n Workout generated for member : {name}",font=('Denmark',12),background='Black',fg='White')
                greet_label.place(x=int((700-greet_label.winfo_reqwidth())/2),y=80)

                #weight training label
                wt_label =tk.Label(root,text=f"Weight Training : ",background='Black',fg='White',font=10,justify='left')
                wt_label.place(x=150,y=130)
                wt2_label =tk.Label(root,text=wt_str,background='Black',fg='White',font=10,justify='left')
                wt2_label.place(x=300,y=130)

                #Cardio Label
                if cardio:
                    cd = '\n'.join(cardio)
                    cd_label =tk.Label(root,text=f"Cardio: ",background='Black',fg='White',font=10,justify='left')
                    cd_label.place(x=180,y=140+wt2_label.winfo_reqheight())
                    cd_label_2 =tk.Label(root,text=cd,background='Black',fg='White',font=10,justify='left')
                    cd_label_2.place(x=300,y=140+wt2_label.winfo_reqheight())

                #print button
                print_button = tk.Button(root,text='Print Workout',font=('Denmark',10),background='Black',fg='White',command=lambda: Features.print_doc(result_dict=res,name=member_id_entry.get(),part=Features.format_part_list(part_list=part_list)))
                print_button.place(x=550,y=350)

                #back button
                back_button = tk.Button(root,text='Back',font=('denmark',10),background='Black',fg='White',command=lambda:[custom_workout(),Features.delete_widget([back_button])])
                back_button.place(x=50,y=50)


            #lists to hold exercise and cardio
            exercise_list,cardio_list,part_list = [],[],[]

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

            #member_id label
            member_id_label = tk.Label(root,text='Member Name',font=("Denmark",10),bg='Black',fg='White')
            member_id_label.place(x=225,y=80)

            #member_id entry
            member_id_entry = tk.Entry(root,bg='#434343',fg='White')
            member_id_entry.place(x=(235+member_id_label.winfo_reqwidth()),y=80)

            #weight_training label
            weight_training_label = tk.Label(root,text="Weight Training",font=('Denmark',12),background='Black',fg='White')
            weight_training_label.place(x=150,y=(90+member_id_label.winfo_reqheight()))

            #body_part label
            body_part_label = tk.Label(root,text="Body Part :",font=('Denmark',10),background='Black',fg='White')
            body_part_label.place(x=225,y=150)

            #body_part combobox
            body_combobox = ttk.Combobox(root)
            body_combobox.place(x=235+body_part_label.winfo_reqwidth(),y=150)
            body_combobox['values'] = ('Chest','Back','Shoulders','Biceps','Triceps','Legs')

            body_combobox.bind('<<ComboboxSelected>>',lambda event: exercises(body_combobox.get()))

            #exercise label
            exercise_label = tk.Label(root,text="Exericses :",font=('Denmark',10),background='Black',fg='White')
            exercise_label.place(x=225,y=180)

            #exercise_combobox
            exercise_combobox = ttk.Combobox(root)
            exercise_combobox.set('Select Body Part')
            exercise_combobox.place(x=235+exercise_label.winfo_reqwidth(),y=180)

            #add to list button
            add_button = tk.Button(root,text='Add to List',font=('Denmark',10),background='Black',fg='White',command=add_exercise_to_list)
            add_button.place(x=300+exercise_label.winfo_reqwidth(),y=205)

            #cardio label
            cardio_label = tk.Label(root,text='Cardio :',font=('Denmark',12),background='Black',fg='White')
            cardio_label.place(x=170,y=235)

            #cardio combobox
            cardio_combobox = ttk.Combobox(root)

            #add cardio button
            add_cardio_button = tk.Button(root,text="Add to list",font=("Denmark",10),background="Black",fg="White",command=add_cardio_to_list)

            #cardio radio button
            check_cardio = tk.IntVar()
            check_cardio.set(1)
            cardio_radio = tk.Radiobutton(root,text='Yes',variable=check_cardio,value=1,background='Black',fg='#3498DB',command=lambda:cardio(cardio_combobox))
            cardio_radio.place(x=250+cardio_label.winfo_reqwidth(),y=255)
            cardio_radio_2 = tk.Radiobutton(root,text='No',variable=check_cardio,value=0,background='Black',fg='#E74C3C',command=lambda:Features.delete_widget([cardio_combobox,add_cardio_button]))
            cardio_radio_2.place(x=300+cardio_label.winfo_reqwidth(),y=255)

            #generate_custom_workout button
            generate_custom_workout_button = tk.Button(root,text="Generate Workout",font=('Denmark',10),background='Black',fg='White',command=lambda:generate_custom_workout(member_id_entry.get()))
            generate_custom_workout_button.place(x=530,y=340)

            #back button
            back_button = tk.Button(root,text='Back',font=('denmark',10),background='Black',fg='White',command=lambda:[trainer_home(),Features.delete_widget([back_button,member_id_entry,member_id_label,generate_custom_workout_button,cardio_radio,exercise_combobox,exercise_label,body_combobox,body_part_label,weight_training_label,add_cardio_button,cardio_combobox,cardio_label,add_button,cardio_radio_2])])
            back_button.place(x=50,y=50)           


        def trainer_home():
            frame.destroy()
            #Generate workout button
            workout_button = tk.Button(root,text="Generate Workout",font=('Denmark',15),background='Black',fg='White',command= lambda:[custom_workout(),Features.delete_widget([workout_button])])
            workout_button.place(x=int(700/4-workout_button.winfo_reqwidth()/2),y=200)

            #Logout Button
            logout_button = tk.Button(root,text='LogOut',font=('Denmark',10),background='Black',fg='White',command= lambda:home(root))
            logout_button.place(x=600,y=350)


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
                trainer_home()
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

        #Back Button
        back_button = tk.Button(root,text='Back',font=('denmark',10),background='Black',fg='White',command=lambda:[home(root),Features.delete_widget([back_button])])
        back_button.place(x=50,y=50)

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