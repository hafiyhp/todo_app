
# How not to make file hard-coded with arguments
def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def get_completed_todos(filepath):
    with open(filepath, 'r') as file_local:
        completed_todos_local = file_local.readlines()
    return completed_todos_local

print("Hello")

if __name__ == "__main15__":
    print("Hello")
    print(get_todos())