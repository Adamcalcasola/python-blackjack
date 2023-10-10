from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = True

def score(p_cards, h_cards):
    print(f"   Your cards: {p_cards}, current score: {sum(p_cards)}")
    print(f"   Computer's first card: {h_cards[0]}")

def final_score(p_cards, h_cards):
    print(f"   Your final hand: {p_cards}, final score: {sum(p_cards)}")
    print(f"   Computer's final hand: {h_cards} final_score: {sum(h_cards)}")

def hit(x_cards):
    new_card = random.choice(cards)
    if new_card == 11:
        total = sum(x_cards) + new_card
        if total > 21:
            return 1
        else:
            return 11
    else:
        return new_card


while play:
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == 'y':
        player_cards = []
        house_cards = []
        bidding = True

        for i in range(2):
            player_cards.append(random.choice(cards))
            house_cards.append(random.choice(cards))

        print(logo)
        score(player_cards, house_cards)

        while bidding:
            hit_me = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()
            if hit_me == 'y':
                player_cards.append(hit(player_cards))
                if sum(player_cards) > 21:
                    bidding = False
                else:
                    score(player_cards, house_cards)
            elif hit_me == 'n':
                bidding = False

        if sum(player_cards) > 21:
            final_score(player_cards, house_cards)
            print("You went over. You lose. ")
        elif sum(house_cards) > sum(player_cards):
            final_score(player_cards, house_cards)
            print("You lose.")
        elif sum(house_cards) == sum(player_cards):
            final_score(player_cards, house_cards)
            print("Draw.")
        else:
            while sum(house_cards) < sum(player_cards):
                house_cards.append(hit(house_cards))
                if sum(house_cards) > 21:
                    final_score(player_cards, house_cards)
                    print(f"You win!")
                elif sum(house_cards) == sum(player_cards):
                    final_score(player_cards, house_cards)
                    print(f"Draw.")
                elif sum(house_cards) > sum(player_cards):
                    final_score(player_cards, house_cards)
                    print(f"You lose.") 
                    
    elif start == 'n':
        play = False


