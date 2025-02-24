import argparse
from ast import arg

from todo_cli.modules import parser


def main():
    args = parser.command_parse()
    print(args)


if __name__ == "__main__":
    main()
