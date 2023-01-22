from Constants import *
from ServiceUtility import *

current_game_available_cards = available_cards_list
player_cards = []
dealer_cards = []
player_points = 0
dealer_points_shown = 0
dealer_points_hidden = 0

def get_card(who):
    global dealer_points_shown
    global dealer_points_hidden
    global player_points
    card_to_distribute = distribute_card(current_game_available_cards)
    current_game_available_cards.remove(card_to_distribute)
    if who == 'PLAYER':
        player_cards.append(card_to_distribute)
        player_points += cards_value[card_to_distribute]
    elif who == 'DEALER_HIDDEN':
        dealer_cards.append(card_to_distribute)
        dealer_points_hidden += cards_value[card_to_distribute]
    elif who == 'DEALER_SHOWN':
        dealer_cards.append(card_to_distribute)
        dealer_points_shown += cards_value[card_to_distribute]
    return card_to_distribute

def compare_score(player_points, dealer_points):
    print(f"Dealer's total was {dealer_points} & your total was {player_points}")
    if dealer_points > 21:
        print("PLAYER WINS!")
    elif  player_points > 21:
        print("DEALER WINS!")
    else:
        if 21-player_points > 21-dealer_points:
            print("DEALER WINS!")
        elif 21-player_points < 21-dealer_points or player_points == 21:
            print("YOU WIN!")
        else:
            print("IT's A DRAW!")

    print_cards()

def initial_setup():
    global dealer_points_shown
    global dealer_points_hidden
    global player_points

    print("Welcome to Saquib's blackjack, distributing cards!")

    card_to_distribute = get_card(who='PLAYER')
    print(f"Your first card is : {card_to_distribute}")

    card_to_distribute = get_card(who='DEALER_SHOWN')
    print(f"Dealer's first card is : {card_to_distribute}")

    card_to_distribute = get_card(who='PLAYER')
    print(f"Your second card is : {card_to_distribute}")

    card_to_distribute = get_card(who='DEALER_HIDDEN')
    print(f"Dealer's second card is : HIDDEN")

    if(player_points == 21):
        print("Congratulations, ITS A BLACKJACK, You WIN!!!")
        print_cards()
        return []

    print(f"Your current total is : {player_points}")
    return [player_points, dealer_points_shown, dealer_points_hidden]

def check_player_cards_for_ace():
    if player_cards.__contains__('Clubs-Ace') or player_cards.__contains__('Hearts-Ace') or player_cards.__contains__('Diamond-Ace') or player_cards.__contains__('Spades-Ace'):
        return True
    else:
        return False

def print_cards():
    print(f"Your cards: {player_cards}")
    print(f"Dealer's cards: {dealer_cards}")

def start_game():
    global dealer_points_shown
    global dealer_points_hidden
    global player_points

    points = initial_setup()
    if not points:
        return


    while(player_points < 21):
        user_input = input("Please enter your next action: Enter 'H' for HIT and 'S' to STAND \n")
        if user_input == 'S':
            if dealer_points_hidden+dealer_points_shown < 17:
                while dealer_points_hidden+dealer_points_shown < 17:
                    print(f"Dealer's total points : {dealer_points_hidden+dealer_points_shown}, which is less than 17, dealing another card to dealer")
                    card_to_distribute = get_card('DEALER_SHOWN')
                    print(f"Dealer's next card is: {card_to_distribute}")
            compare_score(player_points=player_points, dealer_points=dealer_points_hidden + dealer_points_shown)
            break
        elif user_input == 'H':
            card_to_distribute = get_card(who='PLAYER')
            if player_points > 21:
                is_ace_present = check_player_cards_for_ace()
                if is_ace_present:
                    player_points-=10
                    print(f"You got busted, but luckily you had an ace!, re-adjusting your score! \tYour new score is : {player_points}")
                    continue
                else:
                    print(f"Your total points have exceeded 21! Its a BUST, \nDealer WINS ")
                    print(f"Your total points: {player_points} \t Dealer's total points: {dealer_points_hidden + dealer_points_shown}")
                    print_cards()
                    break
            elif player_points == 21:
                print(f"You have 21 points, Congratulations, you win!")
                print(f"Dealer's points: {dealer_points_hidden+dealer_points_shown}")
                print_cards()
            else:
                print(f"Your next card is : {card_to_distribute}")
                print(f"Your total point is : {player_points}")
                continue

start_game()


