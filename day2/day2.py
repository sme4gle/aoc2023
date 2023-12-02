from common import read_input


def split_gamedata(game: str) -> tuple[int, list[str]]:
    game_id = int(game.split(":")[0].split(" ")[1])
    sequences = game.split(": ")[1].split("; ")
    return game_id, sequences


def split_sequence(sequence: str) -> dict[str, int]:
    colors = sequence.split(", ")
    red = 0
    green = 0
    blue = 0
    for color in colors:
        count = int(color.split(" ")[0])
        color_str = color.split(" ")[1]
        if color_str == "red":
            red += count
        elif color_str == "green":
            green += count
        elif color_str == "blue":
            blue += count
    return {
        "red": red,
        "green": green,
        "blue": blue,
    }


def solution_1(input: list[str]) -> int:
    game_id_sum = 0

    for game in input:
        game_id, sequences = split_gamedata(game)

        valid_color_sum = True

        for sequence in sequences:
            color_data = split_sequence(sequence)
            if color_data["red"] > 12 or color_data["green"] > 13 or color_data["blue"] > 14:
                valid_color_sum = False

        if valid_color_sum:
            game_id_sum += game_id

    return game_id_sum


def solution_2(input: list[str]) -> int:
    total_sum = 0
    for game in input:
        game_id, sequences = split_gamedata(game)

        min_red, min_green, min_blue = 0, 0, 0

        for sequence in sequences:
            color_data = split_sequence(sequence)
            min_red = max(color_data["red"], min_red)
            min_green = max(color_data["green"], min_green)
            min_blue = max(color_data["blue"], min_blue)

        sum = min_red * min_green * min_blue
        total_sum += sum
    return total_sum


if __name__ == '__main__':
    input = read_input("input.txt")
    print(solution_1(input))
    print(solution_2(input))
