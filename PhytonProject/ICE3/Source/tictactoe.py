size = int(input("Enter game board size:"))

def print_horiz_line():
    print("--- ", sep=' ', end='', flush=True)

def print_vert_line():
    print("|  ", sep=' ', end='', flush=True)

for index in range(size):
    print("")
    for horiz in range(size):
        print_horiz_line()
    print("")
    for vert in range(size+1):
        print_vert_line()
print("")
for horiz in range(size):
    print_horiz_line()