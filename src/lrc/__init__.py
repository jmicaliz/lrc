import sys
import click
import random

from collections import Counter
from loguru import logger

random.seed()

logger.remove()
logger.add(sys.stdout, level="INFO")


def roll(num_dice):
    dice = []

    for i in range(num_dice):
        dice.append(random.choice([0, 0, 0, -1, 2, 1]))

    return dice


def any_left(curr_table):
    players_left = 0

    for val in curr_table:
        if val > 0:
            players_left += 1
        if players_left > 1:
            return True
    return False


def sim_game(people, dollars):
    table = [dollars] * people

    position = 0
    while any_left(table):
        curr_dolllars = table[position]
        if curr_dolllars > 0:
            dres = roll(curr_dolllars)
            for die in dres:
                if die != 0:
                    if die != 2:
                        to_give = position + die
                        if to_give == people:
                            table[0] += 1
                        else:
                            table[to_give] += 1

                    table[position] -= 1

        position += 1
        if position == people:
            position = 0

    for index, dollars_left in enumerate(table):
        if dollars_left > 0:
            return index + 1


@click.command()
@click.option("--games", "-g", required=True, type=int, help="Number of games to play")
@click.option("--people", "-p", required=True, type=int, help="Number of people playing")
@click.option("--dollars", "-d", required=True, type=int, help="Dollars per person")
def lrc(games, people, dollars):
    games_won = []
    for game in range(games):
        seat = sim_game(people, dollars)
        games_won.append(seat)
        logger.debug(f"Game #{game+1} goes to player #{seat}!")

    print("And the top seats are...")
    counts = Counter(games_won).most_common()
    for player in counts:
        print(f"Seat {player[0]} with {player[1]}")


if __name__ == "__main__":
    lrc()
