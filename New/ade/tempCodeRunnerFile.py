from tabulate import tabulate

def interleave_bits(x, y):
    result = 0
    for i in range(32):
        result |= (x & (1 << i)) << i | (y & (1 << i)) << (i + 1)
    return result

def z_order(x, y):
    return interleave_bits(x, y)

def main():
    points = [
        (5,5 ),
        (6, 6),
        (7, 7),
        (8, 8)
    ]

    print("Original points:")
    print(tabulate(points, headers=["X", "Y"], tablefmt="grid"))

    print("\nZ-order curve values:")
    z_values = []
    for point in points:
        z_value = z_order(point[0], point[1])
        z_values.append([point[0], point[1], z_value])

    print(tabulate(z_values, headers=["X", "Y", "Z-order Value"], tablefmt="grid"))

if __name__ == "__main__":
    main()
