"""the code just below uses what we called modules to keep our code organized AFTER optimization
or we can use import functions and call for example 'todos = functions.get_todos () '"""
from functions import get_todos, write_todos, get_completed_todos
from time_now import get_formatted_time, get_epoch_time, get_day_of_week, is_leap_year

formatted_time = get_formatted_time()
print("The time is below: ")
print(f"Time: {formatted_time}")

todos = get_todos('todos.txt')
completed_todos = get_todos('completed.txt')
undone_todos = []

while True:
    user_action = input("Please type 'add', 'show', 'time', 'edit', 'delete', 'complete', 'undo', or 'exit': ")
    user_action = user_action.strip()
    if user_action.startswith('add'):
        todo = input("Enter a Habit: ")

        todos = get_todos('todos.txt')

        todos.append(todo + '\n')  # fixed the bug

        write_todos("todos.txt", todos)  # putting todos into ( ) or argument will overwrite progress

    elif user_action.startswith('show'):
        todos = get_todos('todos.txt')

        if todos:
            print('Habit List:')
            for index, item in enumerate(todos, start=1):
                item = item.strip('\n')
                print(f'{index} - {item.title()}')
        else:
            print('Your Habit List is empty!')

    elif user_action.startswith('time'):
        print("Formatted Time:", get_formatted_time())
        print("Epoch Time:", get_epoch_time())
        print("Day of Week:", get_day_of_week())
        year = int(input("Enter a year to check if it's a leap year: "))
        print(f"Is {year} a leap year? {is_leap_year(year)}")

    elif user_action.startswith('edit'):
        todos = get_todos('todos.txt')

        if todos:
            print("Current Habit List: ")
            for index, item in enumerate(todos, start=1):
                item = item.strip('\n')
                print(f"{index} - {item.title()}")
        try:
            number = int(input("Enter the number of Habit to edit"))
            if 1 <= number <= len(todos):
                existing_todo = todos[number - 1]
                print(f"here is the existing to do: {existing_todo}")
                new_todo = input(f"edit '{existing_todo.strip()}'")
                todos[number - 1] = new_todo + "\n"
                print("Habit updated!")

                with open('todos.txt', 'w') as file:
                    file.writelines(todos)
        except ValueError:
            print("Invalid Habit number. Please enter a valid Habit number!")
            user_action = input("Please type 'add', 'show', 'time', 'edit', 'delete', 'complete', 'undo', or 'exit': ")
            user_action = user_action.strip()

        else:
            print('Your Habit List is empty')

    elif user_action.startswith('complete'):
        if todos:
            print("Current Habit List: ")
            for index, item in enumerate(todos, start=1):
                item = item.strip('\n')
                print(f"{index} - {item.title()}")

            while True:
                try:
                    number = int(input("Number of Habits to complete: "))
                    if 1 <= number <= len(todos):
                        confirm = input(f"Confirm completion of {todos[number - 1].strip()}" '(yes/no)').strip().lower()
                        if confirm == 'yes':
                            completed_task = todos.pop(number - 1)
                            print(f"task '{completed_task.strip()}' completed")
                            completed_todos.append(completed_task)  # Move to completed_todos
                            with open('completed.txt', 'a') as file:
                                file.write(completed_task + '\n')
                            break
                        elif confirm == 'no':
                            print("Habit completion canceled")
                            break
                        else:
                            print("Please enter 'yes' or 'no")
                except ValueError:
                    print("Invalid Habit number. Please enter a Habit task number!")
                    user_action = input("Please type 'add', 'show', 'time', 'edit', 'delete', 'complete', 'undo', or 'exit': ")
                    user_action = user_action.strip()
        else:
            print("Your Habit List is empty!")

    elif user_action.startswith('undo'):
        if completed_todos:
            print("Completed Habit List: ")
            for index, item in enumerate(completed_todos, start=1):
                item = item.strip('\n')
                print(f"{index} - {item.title()}")
            try:
                number = int(input("Enter the number of Habit to undo: "))
                if 1 <= number <= len(completed_todos):
                    undone_task = completed_todos.pop(number - 1)
                    todos.append(undone_task)
                    write_todos("todos.txt", todos)
                    print(f"Habit '{undone_task.strip()}' undone")

            except ValueError:
                print("Invalid Habit number. Please enter a valid Habit number!")
                user_action = input("Please type 'add', 'show', 'time', 'edit', 'delete', 'complete', 'undo', or 'exit': ")
                user_action = user_action.strip()
        else:
            print('Completed Habit List is empty!')

    elif user_action.startswith('delete'):
        if not todos:
            print("Your Habit list is empty.")
        completed_todos = get_completed_todos('completed.txt')

        if todos:
            try:
                number = int(input("Enter the number of Habit to delete: "))
                if 1 <= number <= len(todos):
                    deleted_todo = todos.pop(number - 1)
                    print(f"Deleted: '{deleted_todo}'")

                    # update the file after deleting
                    write_todos("todos.txt", todos)

            except ValueError:
                print("Invalid Habit number. Please enter a valid Habit number!")
                user_action = input("Please type 'add', 'show', 'time', 'edit', 'delete', 'complete', 'undo', or 'exit': ")
                user_action = user_action.strip()

    elif 'exit' in user_action:
        break

    else:
        print("Invalid input! Please type 'add', 'show', 'time', 'edit', 'delete', 'complete', 'undo', or 'exit'.")
print("Goodbye!")
