#!/usr/bin/python3

"""Command Line Intepreter"""
import cmd
from models import storage
from models import *
import re
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, *args):
        """End of file command to exit the program"""
