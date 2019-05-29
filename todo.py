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

#calling mongo confings 
mongo = tododb.mongo_configs()        


#define function to save task in mongo
def savetask(task):
    mongo.insert_one(task)
    return print("Task has been added")   


#define function to create object to be add 
def addtaskmenu():
    try:  
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
    except:
        return print("Error")


#define function to get all pending tasks 
def getPendingTasks():
    pendingTasks = mongo.find({"state": "Pending"})
    taskNumber = 1
    for task in pendingTasks:
        name = task.get("title")
        print(taskNumber,name)
        taskNumber += 1


def getCompletedTasks():
    pendingTasks = mongo.find({"state": "Completed"})
    taskNumber = 1
    for task in pendingTasks:
        name = task.get("title")
        print(taskNumber,name)
        taskNumber += 1


def deleteTasks(task):
    old_data = mongo.find_one({"title": task}) 
    mongo.delete_many(old_data)

def markTaskCompleted(task):
    mongo.update_one({"title": task}, {"$set":{ "state": "Completed"}}) 
    return print(task, 'Marked as Completed')


#define main fuction wich manage all the process of the app 
def manager(): 
    try:       
        print('To Do App\n\nPrincipal Menu\n\n1.Add Task\n2.Delete\n3.Edit Task\n4.Mark Task As Completed\n5.Pending Tasks\n6.Completed Tasks\n7.All Tasks')
        selectedOption = int(input('Select an Option: '))
        if selectedOption == 1:  
            try:
                savetask(addtaskmenu())
            except:
                print('Error on Adding New Task')
        elif selectedOption == 2: 
            task = input("Type Task Title to be Deleted: ")
            deleteTasks(task)
        elif selectedOption == 4:
            task = input("Type Task Title to be Marked as Completed: ")
            markTaskCompleted(task)
        elif selectedOption == 5:
            getPendingTasks()
        elif selectedOption == 6:
            getCompletedTasks()    
        else: 
            print('hola') 
    except:
        print("ERROR FATAL")   


if __name__ == "__main__":
    while True:
        manager()
        sleep(5)
        clear()