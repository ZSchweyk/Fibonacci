import time


def num_steps(n):
    start = 7
    for i in range(n-3):
        start = start * 2 + 1
    print(start)


def TowerOfHanoi(n, source, destination, middle):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, middle, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, middle, destination, source)


disks = 16
TowerOfHanoi(disks, "A", "C", "B")
print(num_steps(disks))
