with open("2025/day_1/input.txt") as f:
    input_data = f.read().strip()

position = 50
password1 = 0
password2 = 0

for rotation in input_data.splitlines():
    direction = rotation[0]
    distance = int(rotation[1:])
    for _ in range(distance):
        if direction == 'L':
            position = (position - 1 + 100) % 100
        else:
            position = (position + 1) % 100
        if position == 0:
            password2 += 1
    if position == 0:
        password1 += 1

print("Part 1:", password1)
print("Part 2:", password2)
