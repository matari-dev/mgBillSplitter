cards = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
}
hand = []

for _ in range(6):
    hand.append(int(cards[input()]))
print(sum(hand) / len(hand))
