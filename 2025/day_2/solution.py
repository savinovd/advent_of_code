def check_duplicated_number(num: int) -> bool:
    str_num = str(num)
    mid = len(str_num) // 2
    return str_num[:mid] == str_num[mid:]


def check_duplicated_number_more_than_two_times(num: int) -> bool:
    str_num = str(num)
    for i in range(1, len(str_num) // 2 + 1):
        part = str_num[:i]
        if part * (len(str_num) // i) == str_num:
            return True
    return False


def sum_duplicated_numbers_in_range(L: int, R: int, predicate_func) -> int:
    range_total = 0
    for num in range(L, R + 1):
        if predicate_func(num):
            range_total += num
    return range_total


if __name__ == '__main__':
    total_p1 = 0
    total_p2 = 0
    with open('2025/day_2/input.txt') as f:
        line = f.read().strip()
        ranges = line.split(',')
        for range_str in ranges:
            L, R = range_str.split('-')
            total_p1 += sum_duplicated_numbers_in_range(
                int(L),
                int(R),
                check_duplicated_number,
            )
            total_p2 += sum_duplicated_numbers_in_range(
                int(L),
                int(R),
                check_duplicated_number_more_than_two_times,
            )
    print("Part 1:", total_p1)
    print("Part 2:", total_p2)
