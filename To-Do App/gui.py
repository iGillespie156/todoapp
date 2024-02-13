import Functions as fun

import PySimpleGUI as pg

label = pg.Text("Type in a to-do:")
input_box = pg.InputText(tooltip="Enter to-do", key="todo")
add_button = pg.Button("Add")
complete_button = pg.Button("Complete")
close_button = pg.Button("Exit")
list_box = pg.Listbox(values=fun.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = pg.Button("Edit")

window = pg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [close_button]],
                   font=('Helvetica', 20))


while True:
    event, values = window.read()
    print(values)

    match event:
        case "Add":
            todos = fun.get_todos()
            new_todo = values["todo"] + '\n'
            todos.append(new_todo)
            fun.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'

            todos = fun.get_todos()
            todo_index = todos.index(todo_to_edit)
            todos[todo_index] = new_todo
            fun.write_todos(todos)
            window['todos'].update(values=todos)

        case "todos":
            window["todo"].update(value=values['todos'][0])

        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = fun.get_todos()
            todo_index =todos.index(todo_to_complete)
            todos.pop(todo_index)
            fun.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(values='')

        case "Exit":
            break

        case pg.WIN_CLOSED:
            break


window.close()




