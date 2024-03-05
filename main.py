from utils import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tabulate import tabulate


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
        def custom_workout(data):
            def exercises(part): 
                #instead of this we can have a sql table in a db
                exercise_combobox.set('')
                exercise_combobox['values'] = exercise_list_factory.get_exercise_list(part)


            def cardio(cardio_combobox):
                cardio_combobox.set('')
                cardio_combobox['values'] = exercise_list_factory.get_exercise_list("Cardio")
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
                frame_3 = tk.Frame()
                frame_3.pack(side='top',expand=True,fill='both')

                #background image,gym name and gym moto
                tkinter_templates.display(root)

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
                back_button = tk.Button(root,text='Back',font=('denmark',10),background='Black',fg='White',command=lambda:[custom_workout(data=data),Features.delete_widget([back_button]),frame_3.destroy()])
                back_button.place(x=50,y=50)


            #lists to hold exercise and cardio
            exercise_list,cardio_list,part_list = [],[],[]

            #background image,gym name and gym moto
            tkinter_templates.home(root)

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
            back_button = tk.Button(root,text='Back',font=('denmark',10),background='Black',fg='White',command=lambda:[member_home(data=data),Features.delete_widget([back_button,member_id_entry,member_id_label,generate_custom_workout_button,cardio_radio,exercise_combobox,exercise_label,body_combobox,body_part_label,weight_training_label,add_cardio_button,cardio_combobox,cardio_label,add_button,cardio_radio_2])])
            back_button.place(x=50,y=50)


        def workout_history(id_num,data):
            #Creating a Frame
            frame = tk.Frame(root)
            frame.pack(side='top',expand=True,fill='both')

            #background image,gym name and gym moto
            tkinter_templates.display(root)

            #workout history
            history = Features.get_history(id_num=id_num)
            history = [str(x) for x in history]
            final_history = "\n\n".join(history)
            history_label = tk.Message(root,text=final_history,background='Black',fg='White',font=10,width=700)
            history_label.place(x=0,y=100)

            #back Button
            back_button = tk.Button(root,text="Back",font=('Denmark',10),background='Black',fg='White',command=lambda : [member_home(data=data),Features.delete_widget([history_label,back_button])])
            back_button.place(x=50,y=50)


        def display_workout(res,data,part=None):
            #frame
            mframe_2 = tk.Frame(root)
            mframe_2.pack(side='top',expand=True,fill='both')

            #background image,gym name and gym moto
            tkinter_templates.display(root)

            #greet Button
            part_dict = {'1':'Chest-Triceps','2':'Back-Biceps','3':'Shoulders-Legs'}
            greet = tk.Label(root,text=f"Hi, Welcome Back",background='black',fg='White',font=18)
            greet.place(x=int((700-greet.winfo_reqwidth())/2),y=80)
            final_data = f"  Name : {data['Name']}   id_num : {data['id_num']}   Phone Number : 9876543210\nAge : {data['Age']}   Address : Udaipur  Schedule : {part_dict[data['Day']]}"
            member_data_label = tk.Message(root,text=final_data,font=('Denmark',13),background='Black',fg='White',width=700,justify='center')
            member_data_label.place(x=int((700-member_data_label.winfo_reqwidth())/2),y=110)


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
            back_button = tk.Button(root,text="Back",font=('Denmark',10),background='Black',fg='White',command=lambda : [member_home(data=data),Features.delete_widget([back_button,wt_label,cd_label_2,wt2_label,cd_label,print_button])])
            back_button.place(x=50,y=50)


        def member_home(data):
            #frame
            mframe_1 = tk.Frame(root)
            mframe_1.pack(side='top',expand=True,fill='both')

            #background image,gym name and gym moto
            tkinter_templates.home(root=root)

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
            workout_button = tk.Button(root,text="Generate Workout",font=('Denmark',15),background='Black',fg='White',command=lambda : [display_workout(res,data=data,part=part),mframe_1.destroy()])
            workout_button.place(x=int(700/4-workout_button.winfo_reqwidth()/2),y=200)

            #Check Workout History button
            history_button = tk.Button(root,text='Workout History',font=('Denmark',15),background='Black',fg='White',command=lambda: workout_history(id_num=data["id_num"],data=data))
            history_button.place(x=int(700*3/4-history_button.winfo_reqwidth()/2),y=200)

            #custom workout button
            custom_workout_button = tk.Button(root,text="Generate Custom Workout",font=('Denmark',15),background='Black',fg='White',command= lambda:[custom_workout(data=data)])
            custom_workout_button.place(x=int(700/4-custom_workout_button.winfo_reqwidth()/2),y=270)


        def get_input():
            member_id = myentry.get()
            if member_id:
                try:
                    member_details = member_data.get_member_details(id_num=member_id)
                except:
                    wrong_id_label = tk.Label(root,text="Incorrect Member ID. Try Again",font=('Arial',10),background='Black',fg='Red')
                    wrong_id_label.place(x=int((700-wrong_id_label.winfo_reqwidth())/2),y=150)
                else:
                    member_home(member_details)

        #Home Image
        path = r'gallery\home.png'
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
        login_button = tk.Button(root,text="Login",font=('Denmark',10),background='Black',fg='White',command=lambda : [get_input()])
        login_button.place(x=int((700-login_button.winfo_reqwidth())/2),y=125)


class Trainer:
    def main(root):
        def custom_workout():
            def exercises(part): 
                exercise_combobox.set('')
                exercise_combobox['values'] = exercise_list_factory.get_exercise_list(part)


            def cardio(cardio_combobox):
                cardio_combobox.set('')
                cardio_combobox['values'] = exercise_list_factory.get_exercise_list("Cardio")
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
                frame_3 = tk.Frame()
                frame_3.pack(side='top',expand=True,fill='both')

                #background image,gym name and gym moto
                tkinter_templates.display(root)

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
                back_button = tk.Button(root,text='Back',font=('denmark',10),background='Black',fg='White',command=lambda:[custom_workout(),Features.delete_widget([back_button]),frame_3.destroy()])
                back_button.place(x=50,y=50)


            #lists to hold exercise and cardio
            exercise_list,cardio_list,part_list = [],[],[]

            #background image,gym name and gym moto
            tkinter_templates.home(root)

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


        def add_member():
            def add_mem():
                #adding the member to the database
                new_member_details = (new_id,member_name_entry.get(),member_age_entry.get(),cardio_combobox.get(),batch_combobox.get(),day_combobox.get())
                member_data.add_member(new_member_details)

                #new frame
                frame_5 = tk.Frame(root)
                frame_5.pack(side='top',expand=True,fill='both')

                #background image,gym name and gym moto
                tkinter_templates.display(root)

                #confirmation_label
                confirm_label = tk.Label(root,text='Member added Successfully',font=('Denmark',14),background='Black',fg='White')
                confirm_label.place(x=int((700-confirm_label.winfo_reqwidth())/2),y=80)

                #member_deatils_label
                member_details_label = tk.Label(root,text=f' Member ID : {new_member_details[0]}\n Member Name : {new_member_details[1]}\n Member Age : {new_member_details[2]}\n Cardio: {new_member_details[3]} \n Batch : {new_member_details[4]}\n Day : {new_member_details[5]}',font=('Denmark',18),fg='White',background='Black',justify='left')
                member_details_label.place(x=int((700-confirm_label.winfo_reqwidth())/2),y=120)

                #back button
                back_button = tk.Button(root,text='Back',font=('denmark',10),background='Black',fg='White',command=lambda:[add_member(),frame_5.destroy()])
                back_button.place(x=50,y=50)    

            #creating a new frame
            frame_4 = tk.Frame(root)
            frame_4.pack(side='top',expand=True,fill='both')

            #background image,gym name and gym moto
            tkinter_templates.display(root)

            #member_id label
            data = member_data.get_all_members()
            new_id = str(int(data[-1][0])+1)
            new_member_id_label = tk.Label(root,text=f'Member id : {new_id}',font=("Denmark",15),bg='Black',fg='White')
            new_member_id_label.place(x=int((700-new_member_id_label.winfo_reqwidth())/2),y=100)

            #new_member_name label
            new_member_name_label = tk.Label(root,text="Member Name : ",font=('Denmark',12),background='Black',fg='White')
            new_member_name_label.place(x=225,y=110+new_member_id_label.winfo_reqheight())

            #member_name entry
            member_name_entry = tk.Entry(root,bg='#434343',fg='White')
            member_name_entry.place(x=(235+new_member_name_label.winfo_reqwidth()),y=110+new_member_id_label.winfo_reqheight())

            #new_member_age label
            new_member_age_label = tk.Label(root,text="Member Age : ",font=('Denmark',12),background='Black',fg='White')
            new_member_age_label.place(x=225,y=170)

            #member_name entry
            member_age_entry = tk.Entry(root,bg='#434343',fg='White')
            member_age_entry.place(x=(235+new_member_name_label.winfo_reqwidth()),y=170)


            #new_member_cardio label
            new_member_cardio_label = tk.Label(root,text="Cardio : ",font=('Denmark',12),background='Black',fg='White')
            new_member_cardio_label.place(x=245,y=200)

            #cardio_combobox entry
            cardio_combobox = ttk.Combobox(root,values=['Yes','No'])
            cardio_combobox.place(x=235+new_member_name_label.winfo_reqwidth(),y=200)


            #new_member_name label
            new_member_batch_label = tk.Label(root,text="Batch : ",font=('Denmark',12),background='Black',fg='White')
            new_member_batch_label.place(x=245,y=230)

            #cardio_combobox entry
            batch_combobox = ttk.Combobox(root,values=['A','B','C'])
            batch_combobox.place(x=235+new_member_name_label.winfo_reqwidth(),y=230)

            #new_member_day label
            new_member_day_label = tk.Label(root,text="Day : ",font=('Denmark',12),background='Black',fg='White')
            new_member_day_label.place(x=245,y=260)

            #cardio_combobox entry
            day_combobox = ttk.Combobox(root,values=['0','1','2','3'])
            day_combobox.place(x=235+new_member_name_label.winfo_reqwidth(),y=260)

            # add button
            add_member_button = tk.Button(root,text='Add Member',background='Black',fg='White',command=lambda:[add_mem(),frame_4.destroy()])
            add_member_button.place(x=600,y=300)

            #back button
            back_button = tk.Button(root,text='Back',font=('denmark',10),background='Black',fg='White',command=lambda:[trainer_home(),frame_4.destroy()])
            back_button.place(x=50,y=50)    


        def check_member_details():
            #frame
            frame_6 = tk.Frame(root)
            frame_6.pack(side='top',expand=True,fill='both')

            #background image,gym name and gym moto
            tkinter_templates.display(root=root)

            members_data = member_data.get_all_members()
            key = ('ID ','Name','Age','Cardio','Batch','Day')

            table = tabulate(members_data,headers=key)

            #table label
            table_label = tk.Label(root,text=f"{table}",font=('Denmark',10),background='Black',fg='White')
            table_label.place(x=int((700-table_label.winfo_reqwidth())/2),y=90)

            #back button
            back_button = tk.Button(root,text='Back',font=('denmark',10),background='Black',fg='White',command=lambda:[trainer_home(),frame_6.destroy()])
            back_button.place(x=50,y=50)                


        def trainer_home():
            #trainer home frame
            frame_t = tk.Frame(root)
            frame_t.pack(side='top',expand=True,fill='both')

            #background image,gym name and gym moto
            tkinter_templates.home(root)

            #Generate workout button
            workout_button = tk.Button(root,text="Generate Workout",font=('Denmark',15),background='Black',fg='White',command= lambda:[custom_workout(),frame_t.destroy()])
            workout_button.place(x=int(700/4-workout_button.winfo_reqwidth()/2),y=120)

            #add member button
            add_member_button = tk.Button(root,text='Add New Member',font=('Denmark',15),fg='White',background='Black',command=add_member)
            add_member_button.place(x=int(700/4-add_member_button.winfo_reqwidth()/2),y=140+workout_button.winfo_reqheight())

            #member_details button
            member_details = tk.Button(root,text='Check Member details',font=('Denmark',15),fg='White',background='Black',command=check_member_details)
            member_details.place(x=int(700/4-add_member_button.winfo_reqwidth()/2),y=200+workout_button.winfo_reqheight())

            #Logout Button
            logout_button = tk.Button(root,text='LogOut',font=('Denmark',10),background='Black',fg='White',command= lambda:home(root))
            logout_button.place(x=600,y=350)


        def get_input():
            password = myentry.get()
            if password == 'A':
                frame.destroy()
                frame_2 = tk.Frame(root)
                frame_2.pack(side='top',expand=True,fill='both')

                #background image,gym label and gym moto
                tkinter_templates.home(root)

                frame_2.destroy()
                trainer_home()
            else:
                wrong_pass_label = tk.Label(root,text="Wrong Password. Try Again",font=('Arial',10),background='Black',fg='Red')
                wrong_pass_label.place(x=int((700-wrong_pass_label.winfo_reqwidth())/2),y=150)



        #Creating a Frame
        frame = tk.Frame(root)
        frame.pack(side='top',expand=True,fill='both')

        #background image,gym label and gym moto
        tkinter_templates.home(root)

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
        button = tk.Button(root,text="Login",font=('Denmark',10),background='Black',fg='White',command=lambda : get_input())
        button.place(x=int((700-button.winfo_reqwidth())/2),y=125)


def home(root):
    #background image,gym name and gym moto
    tkinter_templates.home(root)

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