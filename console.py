#!/usr/bin/python3
"""
Contains the hbnb command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """The holby airbnb command line class"""
    prompt = "(hbnb) "

    def emptyline(self):
        """This make the empty spaces when you press ENTER"""
        pass

    def do_quit(self, argum):
        """This makes that you exit from the command interpreter"""
        return True

    def do_EOF(self, argum):
        """This makes that you exit from the command interpreter"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
