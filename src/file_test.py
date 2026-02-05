with open("message.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

with open("message.txt", "a", encoding="utf-8") as f:
    f.write("\nLearning File I/O")

with open("message.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())