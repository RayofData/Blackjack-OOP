from blackjack.card import Card
from constants import RANKS, SUITS, VALUES


def create_deck():
    return [
        Card(rank, suit, value, "hidden")
        for suit in SUITS
        for rank, value in zip(RANKS, VALUES)
    ]