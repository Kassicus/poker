import pygame

class Card():
    def __init__(self, color, suit, value):
        self.color = color
        self.suit = suit
        self.value = value

class Deck():
    def __init__(self):
        self.cards = []