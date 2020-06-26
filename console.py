#!/usr/bin/python3
"""
Contains the hbnb command interpreter
"""


import cmd
import models
import sys
from models.base_model import BaseModel



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

    def do_create(self, argum):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and
prints the id."""
        if len(argum) == 0:
            print("** class name missing **")
            return
        argum_list = argum.split()
        try:
            instance = eval(argum_list[0])()
            print(instance.id)
            instance.save()
        except:
            print("** class doesn't exist **")
            return

    def do_show(self, argum):
        """Prints the string representation of an instance based on the class
name and id."""
        if len(argum) == 0:
            print("** class name missing **")
            return
        argum_list = argum.split()
        try:
            instance = eval(argum_list[0])
        except:
            print("** class doesn't exist **")
            return
        if len(argum_list) == 1:
            print("** instance id missing **")
            return
        elif len(argum_list) > 1:
            key = argum_list[0] + "." + argum_list[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")
                return

    def do_destroy(self, argum):
        """Deletes an instance based on the class name and id"""
        if len(argum) == 0:
            print("** class name missing **")
            return
        argum_list = argum.split()
        try:
            instance = eval(argum_list[0])
        except:
            print("** class doesn't exist **")
            return
        if len(argum_list) == 1:
            print("** instance id missing **")
            return
        elif len(argum_list) > 1:
            key = argum_list[0] + "." + argum_list[1]
            if key in models.storage.all():
                models.storage.all().pop(key)
                models.storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, argum):
        """Prints all string representation of all instances based or not on the
class name."""
        


if __name__ == "__main__":
    HBNBCommand().cmdloop()
