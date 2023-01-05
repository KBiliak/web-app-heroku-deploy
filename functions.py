FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    """Read a text file and return the list of to-do items"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):

    with open(filepath, "w") as file:
        file.writelines(todos_arg)
        # return todos_arg
if __name__ == "__main__":
    while True:
        user_action = input("Choose the action: add, show, edit, exit or complete: ")
        user_action = user_action.strip()

        if user_action.startswith("add"):
            todo = user_action[4:]

            todos = get_todos()

            todos.append(todo + "\n")

            write_todos(filepath=FILEPATH, todos_arg=todos)

        elif user_action.startswith("show"):

            todos = get_todos()

            new_todos =[todo.strip("\n") for todo in todos]


            for index, todo in enumerate(new_todos):
                index = index + 1
                row = (f"{index}. {todo}")
                print(row)


        elif user_action.startswith("edit") :
            try:
                number = int(user_action[5:])
                print(number)
                number = number - 1

                todos = get_todos()


                new_todo = input("Edit existing todo: ")
                todos[number] = new_todo + "\n"
                print("Here is how it will be", todos)

                write_todos(todos)

            except ValueError:
                print("Your command is not valid.")
                continue


        elif user_action.startswith("Complete"):
            try:
                number = int(user_action[9:])

                todos = get_todos()

                index = number - 1
                completed_item = todos[index].strip("\n")
                todos.pop(index)
                print(f"Item '{completed_item}' was deleted")

                with open("todos.txt", "w") as file:
                    file.writelines(todos)
            except ValueError:
                print("There is no item with that number")
                continue

        elif user_action.startswith("exit"):
            break

        else:
            print("Command is not valid.")
    print("Bye")
