def calculate_painting_time (colors: list) -> int:
    result = 2
    if colors == []:
        return 0
    for i in range(len(colors) - 1):
        if colors[i] == colors[i + 1]:
            result += 2
        else:
            result += 2 + 1
    return result
colors = []
result = 2
print(calculate_painting_time(colors))
print("Hello Diyorali")

print("Hello Vali")


print("Funksiya  qosh vali")