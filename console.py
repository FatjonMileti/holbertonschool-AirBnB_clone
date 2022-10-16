#!/usr/bin/python3
"""Console"""
import cmd
import models.base_model
from models.engine.file_storage import FileStorage
from models import storage
import json
import gc


class HBNBCommand(cmd.Cmd):
    """class"""
    prompt = '(hbnb)'

    def do_quit(self, line):
        return True
    
    def do_EOF(self, line):
        return True 

    def emptyline(self):
        if self.lastcmd:
            if self.lastcmd == "":
                return self.onecmd('\n')

    def do_create(self, line):
        if len(line) == 0:
            print("** class name missing **")
            return False
        if line != "BaseModel":
            print("** class doesn't exist **")
            return False
        obj = eval(f"models.base_model.{line}")()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        if len(line) == 0:
            print("** class name missing **")
            return False
        if ' ' in line:
            cls = line.split(' ')[0]
            cid = line.split(' ')[1]
        else:
            print("** instance id missing **")
            return False
        if cls != "BaseModel":
            print("** class doesn't exist **")
            return False

        dictionary = storage.all()
        if f"{cls}.{cid}" in dictionary:
            print(dictionary[f"{cls}.{cid}"])

    def do_destroy(self, line):
        if len(line) == 0:
            print("** class name missing **")
            return False
        if ' ' in line:
            cls = line.split(' ')[0]
            cid = line.split(' ')[1]
        else:
            print("** instance id missing **")
            return False
        if cls != "BaseModel":
            print("** class doesn't exist **")
            return False

        dictionary = storage.all()
        if f"{cls}.{cid}" in dictionary:
            del dictionary[f"{cls}.{cid}"]
        else:
            print("** no instance found **")

    def do_all(self, line):
        if len(line) != 0:
            if line != "BaseModel":
                print("** class doesn't exist **")
                return False

        for obj in gc.get_objects():
            if isinstance(obj, models.base_model.BaseModel):
                print(obj)


    def do_update(self, line):
        if len(line) == 0:
            print("** class name missing **")
            return False
        if ' ' in line:
            split = line.split(' ')
            if len(split) < 3:
                print("** attribute name missing **")
                return False
            if len(split) < 4:
                print("** value missing **")
                return False
            cls = split[0]
            cid = split[1]
            catr = split[2]
            cval = split[3]
        else:
            print("** instance id missing **")
            return False
        if cls != "BaseModel":
            print("** class doesn't exist **")
            return False

        dictionary = storage.all()
        for obj in gc.get_objects():
            if isinstance(obj, models.base_model.BaseModel):
                for key in dictionary:
                    if f"{split[0]}.{split[1]}" == key:
                        setattr(obj, eval(f"{catr}"), eval(f"{cval}"))


    def help_quit(self):
        print("Type 'quit' to close the console")

    def help_EOF(self):
        print("Press ^D to close the console")

    def help_create(self):
        print("Type 'create <class.name>' to create an instance of the class")

    def help_show(self):
        print("Type 'show <instance.id> to see instance information'")

    def help_destroy(self):
        print("Type 'destroy <instance.id> to remove instance permanently'")

    def help_all(self):
        print("Type 'all <class.name>' to show all instances of class"
                " (Typing 'all' will show every instance of all classes)")

    def help_update(self):
        print("Type 'update <instance.id> <attribute> <new value>' to"
                " change said attribute value to the new value")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
