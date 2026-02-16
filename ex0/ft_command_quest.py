import sys

# sys.argv is your argv[] (it's a list)
# len(sys.argv) is your argc
# sys.argv[0] is the program name
# sys.argv[1] is the first argument


def ft_command_quest(argv: list[str]) -> None:
    try:
        print("=== Command Quest ===")
        if not argv:
            print("No arguments provided!")
            print("Total arguments: 0")
            return
        if len(argv) > 1:
            print(f"Program name: {argv[0]}")
            print(f"Arguments received: {len(argv) - 1}")
            for i, arg in enumerate(argv[1:]):
                print(f"Argument {i + 1}: {arg}")
        else:
            print("No arguments provided!")
            print(f"Program name: {argv[0]}")
        print(f"Total arguments: {len(argv)}")
    except (TypeError, IndexError) as exc:
        print(f"Error processing arguments: {exc}")


if __name__ == "__main__":
    ft_command_quest(sys.argv)
