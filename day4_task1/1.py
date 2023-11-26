todo_list = []
bin = []

commands = ['add', 'complete', 'view_all', 'view_complete', 'view_incomplete', 'delete', 'restore', 'clear_bin', 'help', 'exit']

task_id = 0

def help():
    print(f"Here are list of available commands:\n\t1) {commands[0]}\n\t2) {commands[1]}\n\t3) {commands[2]}\n\t4) {commands[3]}\n\t5) {commands[4]}\n\t6) {commands[5]}\n\t7) {commands[6]}\n\t8) {commands[7]}\n\t9) {commands[8]}")

def add(ans):
    if any((ans.lower() in jsn['task'].lower()) for jsn in todo_list):
        print("Task already exists")
        return

    global task_id

    todo_list.append({'task_id': task_id, 'task':ans, 'status': 'incomplete'})

    
    
    task_id += 1 

def delete(ans):
    try:
        ans = int(ans)
    except:
        print("Type a integer and try again")
        return
    
    flag = 0

    for i in range(len(todo_list)):
        if todo_list[i]['task_id'] == ans:
            flag = 1
            rep = input("Do you want to delete permanently?(y/n): ")

            

            if rep.lower() == 'y':
                todo_list.remove(todo_list[i])
                break
            else:
                bin.append(todo_list[i])
                todo_list.remove(todo_list[i])

            
            break

    if not flag:
        print("Cannot find the given task id please try again")

def view_all():
    for y in todo_list:
        print(f"task_id: {y['task_id']} Task: {y['task']} status: {y['status']}")

def view_complete():
    for y in todo_list:
        if y['status'] == 'complete':
            print(f"task_id: {y['task_id']} Task: {y['task']} status: {y['status']}")

def view_incomplete():
    for y in todo_list:
        if y['status'] == 'incomplete':
            print(f"task_id: {y['task_id']} Task: {y['task']} status: {y['status']}")

def complete(ans):
    try:
        ans = int(ans)
    except:
        print("Type a integer and try again")
        return
    
    flag = 0

    for i in range(len(todo_list)):
        if todo_list[i]['task_id'] == ans:
            todo_list[i]['status'] = 'complete'
            print("Marked as completed")
            flag = 1
            break

    if not flag:
        print("Cannot find the given task id please try again")

def clear_bin():
    global bin

    bin *= 0

    print("Successfully cleared bin")

def restore():
    print("Restoring....")

    #if we want to restore all tasks
    todo_list.extend(bin)
    clear_bin()

    # restore most recently deleted task
   # todo_list.append(bin.pop())



help()

while True:
    x = input("Enter a command (type help for the list of available commands): ")

    if x not in commands:
        print("Invalid command try again")
        continue

    elif x == 'add':
        ans = input("Enter task: ")
        add(ans)
        continue
    
    elif x=='complete':
        ans = input("Enter task id: ")

        complete(ans)
        
        continue
    
    elif x=='view_all':
        view_all()
        continue
    
    elif x == 'view_complete':
        view_complete()
        continue
    
    elif x == 'view_incomplete':
        view_incomplete()
        continue

    elif x == 'delete':
        ans = input("Enter task: ")
        delete(ans)
        continue

    elif x == 'restore':
        if not bin:
            print("Bin empty")
            continue

        restore()
        continue

    elif x == 'clear_bin':
        clear_bin()
        continue

    elif x == 'help':
        help()

    else:
        ans = input("Are you sure you want to exit?(y/n)")

        if ans.lower() == 'y':
            break

        continue