FILEPATH = 'todo.txt'


def get_and_write_todos(filepath: str = FILEPATH, item: str = None, substituir: str = None, remove_item: str = None) -> list:
    """
    Reads the to-do list from a text file, adds a new `todo` if provided,
    and writes the updated list back to the file.

    :param filepath: The path to the to-do list file. Defaults to 'Files/to-do.txt'
    :param item: A new to-do `todo` to add to the list. Defaults to None.
    :param substituir: The `todo` que quero substituir
    :param remove_item: The `todo` que quero remover
    :return: The updated list of to-do items
    """

    with open(filepath, 'r') as file:
        todos: list = file.readlines()  # Read existing todos
        if item:
            index = len(todos)
            if substituir:
                index = todos.index(substituir)
                todos.remove(substituir)
            todos.insert(index, f'{item}')  # Add new todo if provided

        if remove_item:
            del todos[todos.index(remove_item)]

    with open(filepath, 'w') as output:
        output.writelines(todos)

    return todos
