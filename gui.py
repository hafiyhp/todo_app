import functions
import PySimpleGUI as sg

label = sg.Text("Please Type in a Habit")
input_box = sg.InputText(tooltip="Enter Habit", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My Habit Tracker App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica',20))
while True:
    event, values = window.read() # display window on the screen
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todos'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
