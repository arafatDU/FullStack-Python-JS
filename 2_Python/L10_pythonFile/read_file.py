file = open('test_file.txt', 'r')
# print(file.read())


# read line by line
# print(file.readline())
# print(file.readline())

"""
while True:
    line = file.readline()
    if not line:
        break
    print(line)
"""



all_lines = file.readlines()
print(all_lines)


