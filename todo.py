import tododb 
import calendar
from os import system, name 
from time import sleep

# define function to clear
def clear():
    # windows
    if name == 'nt': 
        _ = system('cls')
    # linux and mac 
    else:
        _ = system('clear')

#define function to save task in mongo
def savetask(task):
    mongo = tododb.mongo_configs()
    mongo.insert_one(task)
    return print("Task has been added")   

#define function to create object to be add 
def addtaskmenu():  
    title = input('Type a Title: ')
    startDate = input('Type an Start Date Ex. 03/04/2019(D,M,Y): ')
    dueDate = input('Type an Due Date Ex. 03/04/2019(D,M,Y): ')
    description = input('Type a Description Max. 100 words: ')
    #selection to choose priority of the task
    prioritySelection = int(input('Choose a Priority, Options:\n1.High\n2.Medium\n3.Low\nSelected Option: '))
    if prioritySelection == 1:
        priority = 'High'
    elif prioritySelection == 2:
        priority = 'Medium'
    else:
        priority = 'Low' 
    #object to be return which is going to be add in the DB
    task = {
        "title" : title, 
        "dates": [{
            "startdate": startDate,
            "duedate": dueDate
        }],
        "description": description,
        "priority": priority,
        "state": "Pending",
        "porcentage": 0
    } 
    return task

#define main fuction wich manage all the process of the app 
def manager():        
    print('To Do App\n\nPrincipal Menu\n\n1.Add Task\n2.Delete or Edit Task\n3.Pending Tasks\n4.Completed Tasks\n5.All Tasks')
    selectedOption = int(input('Select an Option: '))
    if selectedOption == 1:  
        try:
            savetask(addtaskmenu())
        except:
            print('Error on Adding New Task')
    elif selectedOption == 2:
        addtaskmenu()
    else: 
        print('hola')    


if __name__ == "__main__":
    manager()