'''
Create a simple todo app using PySimpleGUI

def save_tasks(values):
    task= values['save_task']
    a = open('tasks.txt', 'w')
    for i in range:
        a.write='taskname'



def open_tasks(values):
    f = open("test.txt", "r")


    sg.Combo(['high', 'medium', 'low', ] ,font = ("Times New Roman" , 9) , background_color= "white", text_color= "black" , key = 'priority')
'''

import PySimpleGUI as sg

task=[]
priority=[]
datelist=[]
todolist=[]
sg.theme
tasklist=[i + j for i, j in zip(priority, todolist)]
my_file = open('tasks.txt')
all_the_lines = my_file. readlines()
items = []
for i in all_the_lines:
    tasklist.append(i)

def add_task(values):
    task = values['taskname']
    Combo= values['priority']
    todolist.append(task)
    priority.append(Combo)
    tasklist=[i + j for i, j in zip(priority, todolist)]
    with open("tasks.txt", 'a') as t:
        for x in tasklist:
            t.write(x+'\n')
    window.FindElement('taskname').Update(value="")
    window.FindElement('todolist').Update(values=tasklist)
    window.FindElement('add_save').Update('Add')

def edit_tasks(values):
    edit_val = values[tasklist][0]
    edit_prior= values['taskname'][0]
    window.FindElement('priority').Update(value=edit_prior)
    window.FindElement('taskname').Update(value=edit_val)
    whole_edit=zip(edit_val, edit_prior)
    taskname.remove(whole_edit)
    window.FindElement('add_save').Update('Save')

def delete_tasks(values):
    delete_val = values['todolist'][0]
    delete_task= values['priority'][0]
    todolist.remove(delete_val)
    priority.remove(delete_task)
    window.FindElement('todolist').Update(values=todolist)



layout = [
     [sg.Text("Enter the task", font=("Arial", 14)), sg.InputText("", font=("Arial", 14), size=(20,1),key="taskname"),
     sg.Button("Add", font=("Arial", 14), key="add_save"), sg.Combo(['high      ', 'medium      ', 'low     ', ] ,font = ("Times New Roman" , 9) , background_color= "white", text_color= "black" , key = 'priority') ],
    [sg.Listbox(tasklist, size=(40, 10), font=("Arial", 14), key='todolist', text_color= "black"), sg.Button("Edit", font=("Arial", 14)),
     sg.Button("Delete", font=("Arial", 14))],
    [sg.Button("Save", font=("Arial",14), key="save_task")]
]
todolist = []

window = sg.Window("Week1", layout)
while True:
    event, values = window.Read()
    if event == 'add_save':
        add_task(values)
    elif event =='Edit':
        edit_tasks(values)
    elif event == 'Delete':
        delete_tasks(values)
    elif event == 'Save':    
        save_tasks(values)
    else:
        break
window.Close()