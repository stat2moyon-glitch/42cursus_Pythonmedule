
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
        
        
  
          
        
        
      
    break
  print(parts)
  
