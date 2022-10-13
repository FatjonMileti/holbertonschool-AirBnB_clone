#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, line):
        self.close()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
