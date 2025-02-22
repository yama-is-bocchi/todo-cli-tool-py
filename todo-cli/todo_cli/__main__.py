import argparse


def main():
    parser = argparse.ArgumentParser(description="Todo CLI Tool")
    parser.add_argument("command", choices=[
                        "create", "list", "edit", "delete"], help="Command to execute")
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
