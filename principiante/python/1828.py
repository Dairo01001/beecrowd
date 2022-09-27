def winner(sheldon: str, raj: str) -> str:
    game = {
        "tesoura": "papel lagarto",
        "papel": "pedra Spock",
        "pedra": "lagarto tesoura",
        "lagarto": "Spock papel",
        "Spock": "tesoura pedra"
    }
    return game[sheldon].__contains__(raj)


def main():
    T: int = int(input())

    for case in range(1, T + 1):
        sheldon, raj = input().split(" ")
        print(
            f'Caso #{case}: {"De novo!" if sheldon == raj else "Bazinga!" if winner(sheldon, raj) else "Raj trapaceou!"}'
        )


if __name__ == "__main__":
    main()