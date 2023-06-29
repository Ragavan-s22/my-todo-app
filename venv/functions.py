def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of todos """
    with open(r"C:\Users\ragav\PycharmProjects\pythonProject1\web_app\venv\todos.txt", 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
 

def write_todos(todos_arg , filepath="todos.txt"):
    """ '"""
    with open(r"C:\Users\ragav\PycharmProjects\pythonProject1\web_app\venv\todos.txtt", 'w') as file_local:
        file_local.writelines(todos_arg)
