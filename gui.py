import functions
import PySimpleGUI as sg

label = sg.Text("Please Type in a Habit")
input_box = sg.InputText(tooltip="Enter Habit")
add_button = sg.Button("Add")

window = sg.Window('My Habit Tracker App', layout=[[label], [input_box, add_button]])
window.read() # display window on the screen
window.close()
