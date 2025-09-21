from unittest import case
task = input("Enter your task: ")
priority = input ("Priority (high/medium/low): ")
#Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
time_bound = input ("Is it time-bound? ")
match priority:
    case "high":
        if time_bound == "yes":
            print ("Reminder:" ,task,"is a high priority task that requires immediate attention today!")
        else:
            print("Note:", task , "is a high priority task. Consider completing it when you have time.")
    case "medium":
        if time_bound == "yes":
            print ("Reminder:" ,task,"is a medium priority task that requires attention this week!")
        else:
            print("Note:", task , "is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "no":
            print ("Note:", task , "is a low priority task. Consider completing it when you have free time.")
        else:
            print ("Reminder:" ,task,"is a medium priority task that requires attention this week!")

            
