def get_todos(filepath=r"todos.txt"):
    """ Read a text file and return the list of todos """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
 

def write_todos(todos_arg , filepath=r"todos.txt"):
    """ '"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
