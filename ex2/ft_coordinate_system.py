
import math


def create_position(x, y, z):
    return x, y, z


def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2 + (z2-z1) ** 2)


def parse_position(s):
    try:
        parts = s.split(",")
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        return (x, y, z)
    except (ValueError, IndexError) as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")
        return None


def unpack_demo(pos):
    x, y, z = pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    pos = create_position(10, 20, 5)
    print("Position created:", pos)

    origin = (0, 0, 0)
    d = distance(origin, pos)
    print(f"Distance between {origin} and {pos}: {d:.2f}\n")

    print('Parsing coordinates: "3,4,0"')
    p = parse_position("3,4,0")
    print("Parsed position:", p)
    print(f"Distance between {origin} and {p}: {distance(origin, p)}\n")

    print('Parsing invalid coordinates: "abc,def,ghi"')
    parse_position("abc,def,ghi")

    print("Unpacking demonstration:")
    unpack_demo(p)
