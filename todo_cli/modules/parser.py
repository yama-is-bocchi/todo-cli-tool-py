import argparse


def parseCommand() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Todo CLI Tool")
    parser.add_argument("command", choices=[
                        "create", "list", "edit", "delete"], help="Command to execute")
    return parser.parse_args()
