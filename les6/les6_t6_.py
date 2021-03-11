import sys

argv = sys.argv[1:]
my_file = open("t6/sales.txt", "r", encoding="utf-8")
line = ""

if not argv:
    line = my_file.readline()
    while line:
        print(line)
        line = my_file.readline()
try:
    if argv[1]:
        for i in range(int(argv[0])):
            line = my_file.readline()
        for i in range(int(argv[1])-int(argv[0])):
            print(line)
            line = my_file.readline()
except IndexError:
    if argv[0]:
        for i in range(int(argv[0])):
            line = my_file.readline()
        while line:
            print(line)
            line = my_file.readline()

my_file.close()
