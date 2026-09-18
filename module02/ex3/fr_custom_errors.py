class GardenError(Exception):
	pass

class PlantError(GardenError):
	pass

class WaterError(GardenError):
	pass

def check_plant(name: str) -> None:
	if name == "":
		raise PlantError()

def check_Water(num: int) -> None:
	if num < 0:
		raise WaterError()


def test_custom_errors() -> None:
	print("=== Custom Garden Errors Demo ===")

	print()
	print("Testing PlantError...")
	try:
		check_plant("")
	except PlantError as error:
		print(error)
	except WaterError as error:
			print(error)
