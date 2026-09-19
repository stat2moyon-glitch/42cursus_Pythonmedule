class GardenError(Exception):
	pass

class PlantError(GardenError):
	pass

class WaterError(GardenError):
	pass

def check_plant(name: str) -> None:
	if name == "":
		raise PlantError()

def check_Water(mount: int) -> None:
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
		check_water(-1)
	except WaterError as error:
		print(error)
	try:
		check_plant("")
	except GardenError as error:
		print(error)
