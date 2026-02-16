import math


def create_position(x: int, y: int, z: int) -> tuple[int, int, int]:
    return x, y, z


def distance(
    p1: tuple[int, int, int], p2: tuple[int, int, int]
) -> float:
    try:
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    except (TypeError, ValueError) as exc:
        print(f"Error calculating distance: {exc}")
        return 0.0


def parse_position(s: str) -> tuple[int, int, int] | None:
    try:
        parts = s.split(",")
        if len(parts) != 3:
            raise ValueError("Expected exactly three coordinates")
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        return x, y, z
    except (ValueError, IndexError) as exc:
        print(f"Error parsing coordinates: {exc}")
        print(
            f"Error details - Type: {type(exc).__name__}, Args: {exc.args}\n"
        )
        return None


def unpack_demo(pos: tuple[int, int, int]) -> None:
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
    if p is not None:
        print(f"Distance between {origin} and {p}: {distance(origin, p)}\n")
    else:
        print("Distance between origin and invalid position: N/A\n")

    print('Parsing invalid coordinates: "abc,def,ghi"')
    parse_position("abc,def,ghi")

    print("Unpacking demonstration:")
    if p is not None:
        unpack_demo(p)
