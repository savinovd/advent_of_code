from pathlib import Path


INPUT_PATH = Path(__file__).with_name("input.txt")


def count_numbers_in_ranges(ranges, numbers):
    count = 0
    for number in numbers:
        for lo, hi in ranges:
            if lo <= number <= hi:
                count += 1
                break
    return count


def merge_ranges(ranges):
    sorted_ranges = sorted(ranges)
    if not sorted_ranges:
        return []

    merged = []
    current_lo, current_hi = sorted_ranges[0]

    for lo, hi in sorted_ranges[1:]:
        if current_hi < lo:
            merged.append((current_lo, current_hi))
            current_lo, current_hi = lo, hi
        else:
            current_hi = max(current_hi, hi)

    merged.append((current_lo, current_hi))
    return merged


def total_coverage(ranges) -> int:
    return sum(hi - lo + 1 for lo, hi in ranges)


if __name__ == "__main__":
    raw = INPUT_PATH.read_text().strip().split("\n\n")
    raw_ranges, raw_numbers = raw
    ranges = [
        tuple(map(int, line.split("-")))
        for line in raw_ranges.splitlines()
        if line
    ]
    numbers = [int(line) for line in raw_numbers.splitlines() if line]
    part1 = count_numbers_in_ranges(ranges, numbers)
    merged = merge_ranges(ranges)
    part2 = total_coverage(merged)

    print(part1)
    print(part2)
