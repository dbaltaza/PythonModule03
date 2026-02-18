import sys

# sys.argv is your argv[] (it's a list)
# len(sys.argv) is your argc
# sys.argv[0] is the program name
# sys.argv[1] is the first argument


def ft_command_quest(argv: list[str]) -> None:
    try:
        print("=== Command Quest ===")
        argc = len(argv)
        if argc == 0:
            print("No arguments provided!")
            print("Total arguments: 0")
            return
        if argc > 1:
            print(f"Program name: {argv[0]}")
            print(f"Arguments received: {argc - 1}")
            i = 1
            while i < argc:
                print(f"Argument {i}: {argv[i]}")
                i += 1
        else:
            print("No arguments provided!")
            print(f"Program name: {argv[0]}")
        print(f"Total arguments: {argc}")
    except (TypeError, IndexError) as exc:
        print(f"Error processing arguments: {exc}")


if __name__ == "__main__":
    ft_command_quest(sys.argv)
