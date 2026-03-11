# Example 3: Read Line by Line
file = open("example1", "r")
for line in file:
    print(line.strip())
file.close()