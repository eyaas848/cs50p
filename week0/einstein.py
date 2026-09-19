def main():
    mass = int(input("Mass: "))
    e = get_energy(mass)
    print("Energy:", e)


def get_energy(m):
    c = 300000000
    return m * c**2


if __name__ == "__main__":
    main()
