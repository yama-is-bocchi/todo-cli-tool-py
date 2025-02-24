import argparse

from todo_cli.modules import parser


def main():
    args = parser.parseCommand()
    print(args)


if __name__ == "__main__":
    main()
