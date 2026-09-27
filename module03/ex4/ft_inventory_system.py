import sys

def parse_inventory(arguments: list[str]) -> dict[str,int]:
    inventory: dict[str, int] = {}

    for argument in arguments:
        parts = argument.split(":")
    
        if len(parts) !=2 or parts[0] == "":
            print(f"Error - invalid parameter '{argument}'")
            continue
        
        name = parts[0]
        
        if name in inventory:
            print("Redundant item '{name}' - discarding")
            continue
        
        try:
            quantity = int(parts[1])
        except ValueError as error:
            print(f"Quantity error for '{name}': {error}")
            continue
            
        inventory[name] = quantity
        
    return inventory

def show_inventory(inventory: dict[str,int]) -> None:
    print(f"Got inventory: {inventory}")

    items = list(inventory.keys())
    print(f"Item list: {items}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    for name in inventory:
        if total == 0:
            print(f"Item {name} represents N/A")
        else:
            percentage = round(inventory[name] / total * 100, 1)
            print(f"Item {name} represents {percentage}%")

        if not items:
            return

        most = items[0]
        least = items[0]

        for name in inventory:
            if inventory[name] > inventory[most]:
                most = name

            if inventory[name] < inventory[least]:
                least = name

        print(
            f"item most abundant: {most}"
            f"with quantity {inventory[most]}
        )
        print(
            f"item most abundant: {least}"
            f"with quantity {inventory[least]}"
        )
                    

def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])
    




  
    


  
  
