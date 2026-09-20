class GardenError(Exception):
	pass

class PlantError(GardenError):
	def __init__(self, message: str = "Unknown plant error") -> None:
		super().__init__(message)

class WaterError(GardenError):
	def __init__(self, message: str = "Unknown water error") -> None:
		super().__init__(message)

def check_plant(name: str) -> None:
	if name == "":
		raise PlantError()

def check_Water(amount: int) -> None:
	if amount < 0:
		raise WaterError()

def test_custom_errors() -> None:
	print("=== Custom Garden Errors Demo ===")

	print()
	print("Testing PlantError...")
	try:
		check_plant("")
	except PlantError as error:
		print(error)
	try:
		check_Water(-1)
	except WaterError as error:
		print(error)
	try:
		check_plant("")
	except GardenError as error:
		print(error)

if __name__ == "__main__":
	test_custom_errors()
