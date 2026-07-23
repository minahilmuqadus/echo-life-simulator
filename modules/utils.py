def get_valid_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")