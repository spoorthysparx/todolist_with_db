import PySimpleGUI as sg 
from db_ops import *
tasks = select_incomplete_records()

sg.theme("bluepurple")
layout=[
    [sg.Text("enter your choice",font=("Arial",16)),
    sg.In("",size=(20,1),font=("Arial",16),key="choice"),
    sg.Button("Add",key="add_save"),
    sg.Button("save task",key="save_tasks"),
    sg.Button("show tasks",key="show_tasks")
    ],
    [sg.Listbox(values=tasks,size=(70,5),font=("Arial",16),key="tasks"),
    sg.InputCombo([2,1,0],"choose the priority",size=(20,3),
    font=("Arial",16),key="priority"),
    sg.Button("Edit",key="edit"),
    sg.Button("Delete",key="delete")
    ],
    [sg.Button("exit",key="exit")],
    [sg.Text('Calendar')],
    [sg.In(key='date', enable_events=True, visible=False),
     sg.CalendarButton('Calendar', target='date',
    button_color=('black', 'white'), key='cal', format=('%d %B, %Y'))],[sg.Button("view completed",key="complete"),sg.Button("view incomplete",key="incomplete")]     
]

def add_tasks(values):
    if window.FindElement("add_save").GetText()=="Add":
        insert_into_task_table(values["choice"],values["priority"])
    else:
        old_task=values["tasks"][0]
        new_task=values["choice"]
        update_task(old_task,new_task)
    update_UI()

def delete_tasks(values):
    mark_task_as_complete(values["tasks"][0][0])
    update_UI()

def edit_tasks(values):
    window.FindElement("choice").update(value=values["tasks"])
    old_value = values["tasks"]
    new_value = values["choice"]
    window.FindElement("add_save").update("save")
    update_task(old_value,new_value)

def update_UI():
    tasks=select_incomplete_records()
    window.FindElement("tasks").update(values=tasks)
    window.FindElement("choice").update(value="")

def completed_UI():
    tasks=select_completed_records()
    window.FindElement("tasks").update(values=tasks)

def incomplete_UI():
    tasks=select_incomplete_records()
    window.FindElement("tasks").update(values=tasks)
       
if __name__ == "__main__":
    window= sg.Window("first app",layout)
    while True:
        event,values=window.read()
        if event== sg.WINDOW_CLOSED:
            break
        elif event=="add_save":
            add_tasks(values)
        elif event=="delete":
            delete_tasks(values)
        elif event=="edit":
            edit_tasks(values)
        elif event=="complete":
            completed_UI()
        elif event=="incomplete":
            incomplete_UI()
    #eli#f event == "save_tasks":
        #save_tasks()
   # elif event=="show_tasks":
        #show_tasks()
   # elif event == "date":
        #set_deadline(values)    

window.close()