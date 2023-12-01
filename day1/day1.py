from common import read_input


def extract_numbers_from_str(string: str) -> list[int]:
    return [int(character) for character in string if character.isdigit()]


def extract_numbers_from_str_b(string) -> list[int]:
    # Since replacing the values didn't work because of intertwined numbers we have to do things differently.
    int_list = []
    for count, character in enumerate(string):
        if character.isdigit():
            int_list.append(int(character))
        else:
            char = extract_next_written_character(string[count:])
            if char:
                int_list.append(char)
    return int_list


def extract_next_written_character(string) -> int | None:
    written_character_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    for key in written_character_dict:
        if string.startswith(key):
            return written_character_dict[key]
    return None


if __name__ == '__main__':
    dataset = read_input('day1/input.txt')
    total = 0

    # Part 1
    for str in dataset:
        number_list = extract_numbers_from_str(str)

        num_1 = number_list[0]
        num_2 = number_list[-1]
        total += int(f"{num_1}{num_2}")
    print(total)

    # Part 2
    total_2 = 0
    for str in dataset:
        number_list = extract_numbers_from_str_b(str)
        num_1b = number_list[0]
        num_2b = number_list[-1]
        total_2 += int(f"{num_1b}{num_2b}")
    print(total_2)
