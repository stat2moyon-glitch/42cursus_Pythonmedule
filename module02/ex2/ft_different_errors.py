def garden_operations(operation_number: int) -> None:
	if operation_number == 0:
		int("abc")
	elif operation_number == 1:
		_ = 10 / 0
	elif operation_number == 2:
		open("/non/existent/file")
	elif operation_number == 3:
		_ = "temperature" + 5
	else:
		return

def test_error_types() -> None:
	print("=== Garden Error Types Demo ===")

	for operation_number in (0,1,2,3,4):
		print(f"Testing operation {operation_number}...")
	try:
		garden_operations(operation_number)
	except ValueError as error:
		print(f"Caught ValueError: {error}")
	except ZeroDivisionError as error:
		print(f"Caught ZeroDivisionError: {error}")
