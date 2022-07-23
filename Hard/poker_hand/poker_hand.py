# tests
hand = input().split()
# hand = "KC 8C KS KD 8D".split() # Full House
# hand = "5C 2C KC AC 7C".split() # Flush
# hand = "2C 2S 3D 4C 5H".split() # One Pair
# hand = "2C 2S 3D 3C 5H".split() # Two Pairs
# hand = "2C 2S 2D 3C 5H".split() # Three of a Kind
# hand = "2C 3D 4H 5S 6C".split() # Straight
# hand = "3C 3D 3H 3S 10H".split() # Four of a Kind
# hand = "7H 8H 9H 10H JH".split() # Straight Flush
# hand = "10C JC QC KC AC".split() # Royal Flush
# hand = "2C 3D 4H".split() # Invalid input

value_list = []
for i in hand:
    if "10" in i:
        value_list.append("10")
    else:
        value_list.append(i[0])
suit_list = []
for i in hand:
    if "10" in i:
        suit_list.append(i[2])
    else:
        suit_list.append(i[1])

hand_values = value_list
hand_suits = suit_list

values = tuple(range(2, 15))
keys = tuple("2 3 4 5 6 7 8 9 10 J Q K A".split())
kvs = list(zip(keys, values))
values = {i[0]:i[1] for i in kvs}
hand_values = [values[i] for i in hand_values]

def calc_high_card(hand, values):
    card_values = []
    for card in hand:
        if card[0] in values.keys():
            card_values.append(values[card[0]])
    return 'High card: ' + str(max(card_values))

high_card = calc_high_card(hand, values)

def calc_one_pair(hand_values):
    for val in hand_values:
        if hand_values.count(val) == 2:
            return True

one_pair = calc_one_pair(hand_values)

def calc_two_pairs(hand_values):
    cards = []
    for val in hand_values:
        if hand_values.count(val) == 2:
            cards.append(val)
    if len(cards) == 4:
            return True

two_pairs = calc_two_pairs(hand_values)

def calc_three_of_a_kind(hand_values):
    cards = []
    for val in hand_values:
        if hand_values.count(val) == 3:
            cards.append(val)
    return len(cards) == 3

three_of_a_kind = calc_three_of_a_kind(hand_values)

def calc_straight(hand_values):
    if sorted(hand_values) == list(range(min(hand_values), max(hand_values)+1)):
        return True

straight = calc_straight(hand_values)

def calc_flush(hand_suits):
    if len(set(hand_suits)) == 1:
        return True

flush = calc_flush(hand_suits)

def calc_full_house(hand_values):
    cards = []
    for val in hand_values:
        if hand_values.count(val) == 3:
            cards.append(val)
        elif hand_values.count(val) == 2:
            cards.append(val)
    return len(cards) == 5

full_house = calc_full_house(hand_values)

def calc_four_of_a_kind(hand_values):
    for val in hand_values:
        if hand_values.count(val) == 4:
            return True

four_of_a_kind = calc_four_of_a_kind(hand_values)

def calc_straight_flush(straight, flush):
    return straight and flush

straight_flush = calc_straight_flush(straight, flush)

def calc_royal_flush(hand_values, flush):
    return [10, 11, 12, 13, 14] == sorted(hand_values) and flush

royal_flush = calc_royal_flush(hand_values, flush)

def calc_hand(hand, high_card, one_pair, two_pairs, three_of_a_kind, straight, flush, full_house, four_of_a_kind, straight_flush, royal_flush):
    if len(hand) != 5:
        return False
    else:
        if royal_flush:
            return "Royal Flush"
        elif straight_flush:
            return "Straight Flush"
        elif four_of_a_kind:
            return "Four of a Kind"
        elif full_house:
            return "Full House"
        elif flush:
            return "Flush"
        elif straight:
            return "Straight"
        elif three_of_a_kind:
            return "Three of a Kind"
        elif two_pairs:
            return "Two Pairs"
        elif one_pair:
            return "One Pair"
        elif high_card:
            return "High Card"

calc_my_hand = calc_hand(hand, high_card, one_pair, two_pairs, three_of_a_kind, straight, flush, full_house, four_of_a_kind, straight_flush, royal_flush)

print(calc_my_hand)