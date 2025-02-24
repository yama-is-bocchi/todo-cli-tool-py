import argparse


def command_parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Todo CLI Tool")

    # サブパーサーを作成 (必須にする)
    subparsers = parser.add_subparsers(dest="command", required=True)

    # create コマンド
    create_parser = subparsers.add_parser(
        "create", help="Create a new todo")
    create_parser.add_argument(
        "--title", required=True)
    create_parser.add_argument(
        "--description", required=True)
    create_parser.add_argument(
        "--date", required=True, help="Follow this format YYYY-MM-DD")

    # edit コマンド
    edit_parser = subparsers.add_parser(
        "edit", help="Edit an existing todo")
    edit_parser.add_argument(
        "--number", required=True, type=int, help="Todo number to edit")
    edit_parser.add_argument("--title")
    edit_parser.add_argument("--description")
    edit_parser.add_argument(
        "--date", help="Follow this format YYYY-MM-DD")

    # delete コマンド
    delete_parser = subparsers.add_parser("delete", help="Delete a todo")
    delete_parser.add_argument(
        "--number", required=True, type=int, help="Todo number to delete")

    # list コマンド
    subparsers.add_parser("list", help="List all todos")

    return parser.parse_args()
