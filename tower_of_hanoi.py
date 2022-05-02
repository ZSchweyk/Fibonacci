def TowerOfHanoi(n, source, destination, middle):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, middle, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, middle, destination, source)


r = TowerOfHanoi(8, "A", "C", "B")
print(f"{r} steps")
