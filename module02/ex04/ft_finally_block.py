class PlantError(Exception)
  def __init__(self, message: str ="Invalid plant name") -> None:
    super().__init__(message)

def water_plant(plant_name: str) -> None:
  if plant_name != plant_name.capitalize():
    raise plant_error()
  print(f"Watering {plant_name}: [OK]")
  
def test_watering_system() -> None:
  print("=== Garden Watering System ===")
  print()
  print("Testing valid plants...")
  print("Opening watering system")
  try:
    for plant_name in ["Tomato", "Lettuce", "Carrots"]:
      water_plant(plant_name)
    
  except PlantError as error:
    print(error)
    print(".. ending tests and returning to main")
    return
    
  finally:
    print("Closing watering system")

  print("Testing invalid plants...")
  print("Opening watering system")
  try:
    for plant_name in ["Tomato", "lettuce", "Carrots"]:
      water_plant(plant_name)
    
  except plant_error as error:
    print(error)
    print(".. ending tests and returning to main")
    return
    
  finally:
    print("Closing watering system")

if __name__ == "__main__"
  test_watering_system()
  print("Cleanup always happens, even with errors!")

