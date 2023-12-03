import re

from common import read_input

# special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "/", "+", "=", "-"]
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "?", "_", "=", "<", ">", "/"]


def fetch_numbers(string: str) -> list[int]:
    numbers = re.findall(r'\d+', string)
    return [int(num) for num in numbers]


def fetch_horizontal_serials(row: str, numbers: list[int]) -> list[int]:
    serial_numbers = []
    min_location = 0
    for number in numbers:
        relative_location = row[min_location:].find(str(number))
        location = relative_location + min_location
        if row[max(location - 1, 0)] in special_characters:
            serial_numbers.append(number)
        if location < 137:
            if row[location + len(str(number))] in special_characters:
                serial_numbers.append(number)
        min_location = location + len(str(number))
    return serial_numbers


def fetch_vertical_serials(input: list[str], numbers: list[int], row: str, row_number: int) -> list[int]:
    serial_numbers = []
    min_location = 0
    for number in numbers:
        relative_location = row[min_location:].find(str(number))
        location = relative_location + min_location
        is_valid = False
        for loc in range(len(str(number)) + 2):
            if row_number > 0:
                if location + loc <= 140:
                    if input[row_number - 1][location + loc - 1] in special_characters:
                        is_valid = True
            if row_number < 139:
                if location + loc <= 140:
                    if input[row_number + 1][location + loc - 1] in special_characters:
                        is_valid = True
        if is_valid:
            serial_numbers.append(number)
        min_location = location + len(str(number))
    return serial_numbers


if __name__ == "__main__":
    input = read_input("input.txt")
    # for row_number, row in enumerate(input):
    total_sum = 0
    for row_number, row in enumerate(input):
        numbers = fetch_numbers(row)
        horizontal_serial_numbers = fetch_horizontal_serials(row, numbers)
        vertical_serial_numbers = fetch_vertical_serials(input, numbers, row, row_number)
        serials = []
        all_serials = horizontal_serial_numbers + vertical_serial_numbers
        print(all_serials)
        for s in all_serials:
            total_sum += s
    print(total_sum)
