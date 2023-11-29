import json

todo_list = []

commands = ['add', 'complete', 'view_all', 'view_complete', 'view_incomplete', 'help', 'exit']

def read_file():
    with open('file.json', 'r') as f:
        try:
            return json.load(f)
        except:
            return False
    
def write_file(jsn):
    with open('file.json', 'w') as f:
        f.write(json.dumps(jsn))

jsn = read_file()

if not jsn:
    task_id = 0
else:
    jsn[-1]['task_id']

print("Here are list of available commands:\n\t1) add\n\t2) complete\n\t3) view_all\n\t4) view_complete\n\t5) view incomplete\n\t6) exit")



while True:
    x = input("Enter a command (type help for the list of available commands): ")

    if x not in commands:
        print("Invalid command try again")
        continue

    elif x == 'add':

        jsn = read_file()

        if not jsn:
            jsn = []

        ans = input("Enter task: ")

        if any((ans.lower() in jsn['task'].lower()) for jsn in todo_list):
            print("Task already exists")
            continue
        
        jsn.append({'task_id': task_id, 'task':ans, 'status': 'incomplete'})

        write_file(jsn)

        task_id += 1
    
    elif x=='complete':
        ans = input("Enter task id: ")

        try:
            ans = int(ans)
        except:
            print("Type a integer and try again")
        
        flag = 0

        jsn = read_file()

        for i in range(len(jsn)):
            if jsn[i]['task_ids'] == ans:
                jsn[i]['status'] = 'complete'
                print("Marked as completed")
                flag = 1

                write_file(jsn)

                break

        if not flag:
            print("Cannot find the given task id please try again")
        
        continue
    
    elif x=='view_all':
        jsn = read_file()
        for y in jsn:
            print(f"task_id: {y['task_id']} Task: {y['task']} status: {y['status']}")
        continue
    
    elif x == 'view_complete':
        jsn = read_file()
        for y in jsn:
            if y['status'] == 'complete':
                print(f"task_id: {y['task_id']} Task: {y['task']} status: {y['status']}")
    
    elif x == 'view_incomplete':
        jsn = read_file()
        for y in jsn:
            if y['status'] == 'incomplete':
                print(f"task_id: {y['task_id']} Task: {y['task']} status: {y['status']}")

    elif x == 'help':
        print("Here are list of available commands:\n\t1) add\n\t2) complete\n\t3) view_all\n\t4)view_complete\n\t5)view incomplete\n\t6)exit")
    
    else:
        ans = input("Are you sure you want to exit?(y/n)")

        if ans.lower() == 'y':
            break

        continue