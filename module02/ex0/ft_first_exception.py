def input_temperature(temp_str: str) -> int:
	return int(temp_str)

def test_temperature() -> None:
	print("=== Garden Temperature ===")
	print()
	for temp_str in ("25", "abc"):
		print(f"Input data is '{temp_str}'")
		try:
			temperature = input_temperature(temp_str)
			print(f"Temerature is now {temperature}°C")
		except ValueError as error:
			print(f"Caught input_tempereture error: {error}")

	print()
	print("All tests completed - program didn't crash!")

def main():
	try:
		x = int("one")
	except ValueError as error:
		print(f"Caught input_tempereture error: {error}")

if __name__ == "__main__":
	main()
	test_temperature()
