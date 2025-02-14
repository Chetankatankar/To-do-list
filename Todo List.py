# TO-DO LIST 
#dictionary: it is a key value pair.

todo={"pending":[], "completed":[]}

while True:
    print()
    print(" « To do list » ".center(100, '•'))
    print("\nSelect Operation - ")
    print("\n1.Add Task  ")
    print("2.View Task")
    print("3.Update Task")
    print("4.Delete Task")
    print("5.Exit TO-Do List")
    op = int(input("\nEnter your choice: "))
    if op==1:
        n = int(input("Enter, How many task do you want to add: "))
        for i in range(n):
            task=input("\nEnter task to add : ")
            todo["pending"].append(task)
            print(task, "added!")
    if op==2:
        print()
        print(" Task List ".center(30, '–'))
        print("Pending Task ↠")
        count=1
        for data in todo["pending"]:
            print(f"{count}. {data}")
            count=count+1
        print()
        print("Completed Task ↠")
        count=1
        for data in todo["completed"]:
            print(f"{count}. {data}")
            count=count+1
    if op==3:
        print(" Update List ".center(20, '–'))
        count=1
        for data in todo["pending"]:
            print(f"{count}. {data}")
            count=count+1
        index = int(input("Select Task by number: "))
        ele = todo["pending"].pop(index-1)
        todo["completed"].append(ele)
        print(f"{ele} added to complete!")
    if op==4:
        if len(todo["pending"]) == 0:
            print("No pending tasks to delete!")
        else:
            print(" Pending Tasks ".center(30, '–'))
        count = 1
        for data in todo["pending"]:
            print(f"{count}. {data}")
            count += 1
        n = int(input("Select Task number to delete: "))
        
        if n > 0 and n <= len(todo["pending"]):
            task = todo["pending"].pop(n - 1)
            print(task, "deleted!")
    if op==5:
        print("Thankk Youu!")
        break