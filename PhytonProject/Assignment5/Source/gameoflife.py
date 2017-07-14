import numpy

def play_life(a):
    xmax, ymax = a.shape
    b = a.copy() # copy grid & Rule 2
    for x in range(xmax):
        for y in range(ymax):
            n = numpy.sum(a[max(x - 1, 0):min(x + 2, xmax), max(y - 1, 0):min(y + 2, ymax)]) - a[x, y]
            if a[x, y]:
                if n < 2 or n > 3:
                    b[x, y] = 0 # Rule 1 and 3
            elif n == 3:
                b[x, y] = 1 # Rule 4
    return(b)


life = numpy.zeros((10, 10), dtype=numpy.byte)

life[4, 1:6] = 1

print("Gamee of life:\n")
print("Input is:\n")
print(life)
print("Output is:\n")
for i in range(3):
    life = play_life(life)
    print(life)
    print("\n")