todo_list = []

commands = ['add', 'complete', 'view_all', 'view_complete', 'view_incomplete', 'help', 'exit']

task_id = 0

print("Here are list of available commands:\n\t1) add\n\t2) complete\n\t3) view_all\n\t4) view_complete\n\t5) view incomplete\n\t6) exit")

while True:
    x = input("Enter a command (type help for the list of available commands): ")

    if x not in commands:
        print("Invalid command try again")
        continue

    elif x == 'add':
        ans = input("Enter task: ")

        if any((ans.lower() in jsn['task'].lower()) for jsn in todo_list):
            print("Task already exists")
            continue

        todo_list.append({'task_id': task_id, 'task':ans, 'status': 'incomplete'})
        task_id += 1
    
    elif x=='complete':
        ans = input("Enter task id: ")

        try:
            ans = int(ans)
        except:
            print("Type a integer and try again")
        
        flag = 0

        for i in range(len(todo_list)):
            if todo_list[i]['task_ids'] == ans:
                todo_list[i]['status'] = 'complete'
                print("Marked as completed")
                flag = 1
                break

        if not flag:
            print("Cannot find the given task id please try again")
        
        continue
    
    elif x=='view_all':
        for y in todo_list:
            print(f"task_id: {y['task_id']} Task: {y['task']} status: {y['status']}")
        continue
    
    elif x == 'view_complete':
        for y in todo_list:
            if y['status'] == 'complete':
                print(f"task_id: {y['task_id']} Task: {y['task']} status: {y['status']}")
    
    elif x == 'view_incomplete':
        for y in todo_list:
            if y['status'] == 'incomplete':
                print(f"task_id: {y['task_id']} Task: {y['task']} status: {y['status']}")

    elif x == 'help':
        print("Here are list of available commands:\n\t1) add\n\t2) complete\n\t3) view_all\n\t4)view_complete\n\t5)view incomplete\n\t6)exit")
    
    else:
        ans = input("Are you sure you want to exit?(y/n)")

        if ans.lower() == 'y':
            break

        continue