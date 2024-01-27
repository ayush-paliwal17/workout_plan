class weight_training:
    def circuit(self,member_details):
        if member_details["Batch"] == "A":
            member_details["Batch"] = "B"
            return("circuit 1")

        elif member_details["Batch"] == "B":
            member_details["Batch"] = "A"
            return("circuit 2")


    def chest_triceps(self,member_details):
        if member_details["Batch"] == "A":
            member_details["Batch"] = "B"
            return ("chest_triceps_1")
        elif member_details["Batch"] == "B":
            member_details["Batch"] = "C"
            return ("chest_triceps_2")
        else:
            member_details["Batch"] = "A"
            return ("chest_triceps_3")


    def back_biceps(self,member_details):
        if member_details["Batch"] == "A":
            member_details["Batch"] = "B"
            return ("back_biceps_1")
        elif member_details["Batch"] == "B":
            member_details["Batch"] = "C"
            return ("back_biceps_2")
        else:
            member_details["Batch"] = "A"
            return ("back_biceps_3")


    def shoulders_legs(self,member_details):
        if member_details["Batch"] == "A":
            member_details["Batch"] = "B"
            return ("shoulders_legs_1")
        elif member_details["Batch"] == "B":
            member_details["Batch"] = "C"
            return ("shoulders_legs_2")
        else:
            member_details["Batch"] = "A"
            return ("shoulders_legs_3")


class WorkoutPlan(weight_training):
    def circuit(member_details):
        return super().circuit(member_details)+ "cardio1" if member_details["cardio"] == "Yes" else super().circuit(member_details)

    def chest_triceps(member_details):
        return super().chest_triceps(member_details) + "cardio2" if member_details["cardio"] == "Yes" else super().chest_triceps(member_details)
    
    def back_biceps(self,member_details):
        return super().back_biceps(member_details) + "cardio3" if member_details["cardio"] == "Yes" else super().chest_triceps(member_details)
    
    def shoulders_legs(member_details):
        return super().shoulders_legs(member_details) + "cardio4" if member_details["cardio"] == "Yes" else super().chest_triceps(member_details)


members = (
    {"Name" : "Ayush", "Age" : 23, "class" : "I","cardio" : "Yes", "Batch" : "A","Day" : "1"},
    {"Name" : "Mrityunjay", "Age" : 23, "class" : "B","cardio" : "No", "Batch" : "B","Day" : "1"},
    {"Name" : "Harsh", "Age" : 23, "class" : "I","cardio" : "No" , "Batch" : "C","Day" : "1"},
    {"Name" : "Karan", "Age" : 23, "class" : "I","cardio" : "Yes", "Batch" : "A","Day" : "1"}
)

# for member in members:
#     print(WorkoutPlan.back_biceps(member))
ayush = WorkoutPlan()
print(ayush.back_biceps(member_details=members[0]))