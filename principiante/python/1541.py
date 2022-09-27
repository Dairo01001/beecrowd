def main():
    while True:
        abc = list(map(int, input().split(" ")))

        if len(abc) == 1: return

        area = abc[0] * abc[1] * 100 / abc[2]

        houses = 1
        while houses * houses <= area:
            houses = houses + 1

        print(houses - 1)


if __name__ == "__main__":
    main()
