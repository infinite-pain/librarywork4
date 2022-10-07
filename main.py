from os import listdir
from os.path import isfile

notes = {}   # dictionary contains lists that collect dictionaries
myfiles = []    # show notebooks
existing = []    # show is there a notebook in notes

def byId(note):
    return note['id']

def byTask(note):
    return note['task']

def byTime(note):
    return note['time']

def byDate(note):
    return note['date']

def byPriority(note):
    return note['priority']

def byStatus(note):
    return note['status']


# read the notebook lines and put each one of them in the notes list
def pickbook():
    print('List of available notebooks:', listdir('./notebooks/iamdir'))
    global notebookFileName
    notebookFileName = input('Choose a notebook name you want to work with:\n')
    if notebookFileName not in existing:
        with open("./notebooks/iamdir/" + notebookFileName, "r") as f:
            notes[notebookFileName] = []
            for line in f:
                l = line.split(",")
                note = {
                    "id": int(l[0]),
                    "task": l[1],
                    "time": l[2],
                    "date": l[3],
                    "priority": l[4],
                    "status": l[5][:-1]
                }
                notes[notebookFileName].append(note)
    existing.append(notebookFileName)
    chooseOperation()

def sortbook():
    userAction = input('Choose the field to sort with: ')
    if userAction == 'exit':
        return ''
    elif userAction == 'id':
        notes[notebookFileName].sort(key=byId)
    elif userAction == 'task':
        notes[notebookFileName].sort(key=byTask)
    elif userAction == 'time':
        notes[notebookFileName].sort(key=byTime)
    elif userAction == 'date':
        notes[notebookFileName].sort(key=byDate)
    elif userAction == 'priority':
        notes[notebookFileName].sort(key=byPriority)
    elif userAction == 'status':
        notes[notebookFileName].sort(key=byStatus)
    tableprint(notes[notebookFileName])

# print the notebook using notes list
def tableprint(notes):
    print("{:<3} {:<17} {:<10} {:<15} {:<19} {:<11}".format('Id', 'Task', 'Time', 'Date', 'Priority', 'Status'))
    print()
    for note in notes:
        id, task, time, date, priority, status = note.values()
        print("{:<3} {:<17} {:<10} {:<15} {:<19} {:<11}".format(id, task[:15], time, date, priority, status))
    finish()

# ask user continue or finish operations with the notebook
def finish():
    while True:
        print()
        print('Do you want to continue? (yes or no)')
        answer = input()
        if answer.lower() == 'yes':
            chooseOperation()
            break
        elif answer.lower() == 'no':
            print('Goodbye')
            break
        else:
            print('Incorrect answer. Try again.')
            continue

# create a new notebook
def makebook():
    l = []
    l.append(notes[notebookFileName][-1]['id'] + 1)
    l.append(input('Your task: '))
    l.append(input('Time: '))
    l.append(input('Date: '))
    l.append(input('Priority: '))
    l.append(input('Status: '))
    note = {  #
        'id': l[0],
        'task': l[1],
        'time': l[2],
        'date': l[3],
        'priority': l[4],
        'status': l[5][:-1]
    }
    notes[notebookFileName].append(note)
    tableprint(notes[notebookFileName])

# change existing values in certain lines
def changebook():
    noteId = int(input('''Line's id: '''))
    noteField = input('Field (task, time, date, priority or status): ').lower()
    fieldValue = input('New value: ')
    list = notes[notebookFileName]
    list[noteId - 1][noteField] = fieldValue
    tableprint(notes[notebookFileName])

# delete certain line
def delbook():
    noteId = int(input('''Line's id: '''))
    list = notes[notebookFileName]
    del list[noteId - 1]
    for note in list:
        if note['id'] > noteId:
            note['id'] -= 1
    tableprint(list)

# ask what operation user want to perform and then redirect to the required function
def chooseOperation():
    while True:
        a = input('Choose the operation:\n'
                  '1. Show existing lists\n'
                  '2. Make a new notebook line\n'
                  '3. Change the existing notebook\n'
                  '4. Delete the existing notebook\n'
                  '5. Pick the notebook\n'
                  '6. Sort\n')
        if a == '1':
            tableprint(notes[notebookFileName])
            break
        elif a == '2':
            makebook()
            break
        elif a == '3':
            changebook()
            break
        elif a == '4':
            delbook()
            break
        elif a == '5':
            pickbook()
            break
        elif a == '6':
            sortbook()
            break
        else:
            print('Incorrect answer. Try again.')

pickbook()
