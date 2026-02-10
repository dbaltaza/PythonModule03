import sys

""" sys.argv is your argv[] (it's a list)
 len(sys.argv) is your argc
 sys.argv[0] is the program name
 sys.argv[1] is the first argument """


def ft_command_quest(argv):
    print("=== Command Quest ===")
    print(f"Program name: {argv[0]}")
    if len(sys.argv) > 1:
        print(f"Arguments received: {len(argv)}")
        for i, arg in enumerate(argv[1:]):
            print(f"Arguments {i + 1}: {arg}")
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest(sys.argv)
