#!/usr/bin/python3


class User:
    def __init__(self, name):
        self.name = name


# Create user command
def create_user(args):
    name = args[0]
    user = User(name)
    print(f"You have created user: {user.name}")


# Retrieve user command
def retrieve_user(args):
    name = args[0]
    user = User(name)
    print(f"You have retrieved user: {user.name}")


# The loop for the command intepreter
while True:
    user_insert = input("Enter command: ")
    command_parts = user_insert.split()
    command = command_parts[0]
    args = command_parts[1:]

    if command == "create" and len(args) > 0:
        create_user(args)
    elif command == "retrieve" and len(args) > 0:
        retrieve_user(args)
    elif command == "exit":
        break
    else:
        print("Invalid command")
