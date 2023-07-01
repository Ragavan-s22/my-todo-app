FILEPATH = "venv/todos.txt"
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of todos """
    with open(FILEPATH, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
 

def write_todos(todos_arg , filepath=FILEPATH):
    """ Write a text file """
    with open(FILEPATH, 'w') as file_local:
        file_local.writelines(todos_arg)
