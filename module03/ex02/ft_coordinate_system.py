math.sqrt()

def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = user_input.split(",")
        count = len(parts)
        if count != 3: 
            print("Invalid syntax")
            continue
            
        numbers :list[float] = []
        
        try:
            for temp in parts:
                number = float(temp)
                numbers.append(number)
        except ‎ValueError as error:
            print(f"Error on parameter {temp}: {error}")
            continue
    break
    coordinates = tuple(numbers)
    return coordinates

def calculate_distance(
    pos1: tuple[float, float, float],
    pos2: tuple[float, float, float],
) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2

    distance = math.sqrt(
        (x2 - x1)**2
        + (y2 - y1)**2
        + (z2 - z1)**2
    )

def main() -> None:
    print("=== Game Coordinate System ===")
    pos1 = get_player_pos()
    print(f"Got a first set of tuple: {pos1}")
    x, y, z = pos1
    print(f"It includes: X={x}, Y={y}, Z={z}")
    center = (0.0, 0.0, 0.0)    
    distance = calculate_distance(pos1, center)
    print(f"Distance to center: {distance:.4f}")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    distance = calculate_distance(pos1, pos2)
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{distance:.4f}"
    )
    
