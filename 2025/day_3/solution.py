from functools import lru_cache
from pathlib import Path

INPUT_PATH = Path(__file__).with_name("input.txt")


def best_two_digit_value(line):
    best = -1
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            score = int(line[i] + line[j])
            if score > best:
                best = score
    return best


def best_twelve_digit_value(line):
    @lru_cache(maxsize=None)
    def dfs(idx, used):
        if idx == len(line):
            return 0 if used == 12 else -10**20

        skip = dfs(idx + 1, used)
        take = -10**20
        if used < 12:
            place_value = 10 ** (12 - 1 - used)
            take = place_value * int(line[idx]) + dfs(idx + 1, used + 1)
        return max(skip, take)

    return dfs(0, 0)


if __name__ == "__main__":
    lines = INPUT_PATH.read_text().strip().splitlines()
    part1 = 0
    part2 = 0
    for line in lines:
        part1 += best_two_digit_value(line)
        part2 += best_twelve_digit_value(line)
    print(part1)
    print(part2)
