import math
import sys


def compute_distance(o: tuple, p: tuple) -> float:
    """Get the distance between two point in space"""
    return (math.sqrt((p[0] - o[0])**2 + (p[1] - o[1])**2 + (p[2] - o[2])**2))


def parse_coords(coords: str) -> tuple:
    """get coord tuple from coord string"""
    return (tuple(int(x) for x in coords.split(",")))


if (__name__ == "__main__"):
    origin: tuple = (0, 0, 0)
    position: tuple = (10, 20, 5)
    print("=== Game Coordinate System ===\n")
    print("Position created:", position)
    print(f"Distance between {origin} and {position}: \
{compute_distance(origin, position):.2f}\n")
    coords: str = "3,4,0"
    print("Parsing coordinates:", coords)
    position = parse_coords(coords)
    print("Parsed position:", position)
    print(f"Distance between {origin} and {position}: \
{compute_distance(origin, position)}\n")
    try:
        coords = "abc,def,ghi"
        print("Parsing invalid coordinates:", coords)
        position = parse_coords(coords)
    except ValueError as e:
        print("Error parsing coordinates:", e)
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    print("\nUnpacking demonstration:")
    x, y, z = (3, 4, 0)
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
    # Faire bouvle for sur les coords en parametre de programme argv
    for i in range(len(sys.argv)):
        if (i > 0):
            try:
                coords = parse_coords(sys.argv[i])
                if (len(coords) != 3):
                    raise Exception
                x, y, z = coords
                print(f"\nPlayer at x={x}, y={y}, z={z}")
                print(f"Coordinates: X={x}, Y={y}, Z={z}")
            except Exception:
                print("\nInvalid coords")
