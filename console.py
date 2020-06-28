#!/usr/bin/python3
"""
Contains the hbnb command interpreter
"""


import cmd
import models
import sys
import shlex  # To parse lexicon correctly
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The holby airbnb command line class"""
    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'Place', 'State',
               'City', 'Amenity', 'Review']

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
        except Exception:
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
        except Exception:
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
        except Exception:
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
        """ Display all instances based on class name """
        if len(argum) < 1:
            ac = []
            for value in models.storage.all().values():
                ac.append(str(value))
            if not ac:
                return
            print(ac)
        else:
            modelClass = argum.split(" ")
            if modelClass[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif modelClass[0] in HBNBCommand.classes:
                ac = []
                for value in models.storage.all().values():
                    if modelClass[0] in value.__class__.__name__:
                        ac.append(str(value))
                if not ac:
                    return
                print(ac)

    def do_update(self, argum):
        """ update an instance based on its UUID """
        if len(argum) == 0:
            print("** class name missing **")
            return
        else:
            ac = shlex.split(argum)
            if ac[0] not in HBNBCommand.classes:
                print("** instance id missing **")
                return
            tmp = ac[0] + '.' + ac[1]
            if tmp in models.storage.all():
                to_update = models.storage.all()[tmp].__dict__
                if len(ac) < 3:
                    print("** attribute name missing **")
                elif len(ac) < 4:
                    print("** value missing **")
                else:
                    key = ac[2]
                    try:
                        attr = type(to_update[key])
                        value = attr(ac[3])
                    except KeyError:
                        value = ac[3]
                    to_update[key] = value
                    models.storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
