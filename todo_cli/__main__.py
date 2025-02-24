from todo_cli.modules import parser, todo_app


def main():
    args = parser.command_parse()
    app = todo_app.TodoApp()
    match args.command:
        case "create":
            app.create(args)


if __name__ == "__main__":
    main()
