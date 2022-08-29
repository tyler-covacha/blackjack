import random
import sys

''' This version does not cover the Blackjack rules such as:
        splitting pairs
        doubling down
        insurance
        settlement
        reshuffling '''
# if player gets blackjack and dealer does not, player wins immediately
    # if dealer has blackjack as well, dealer wins
    # if dealer has blackjack and player does not,
        # dealer wins because blackjack beats 21
    


''' random card function '''
def random_card(deck):
    card, value = random.choice(list(deck.items()))
    del deck[card]

    ace_counter = 0
    if value == 11:
        ace_counter += 1
        
    return card, value, ace_counter, deck




'''player's first two cards '''
def player_two_cards(deck):
    player_deck_value = 0
    player_ace_counter = 0
    
    # first two cards
    for i in range(2):
    
        # pick random card
        card = random_card(deck)
        print("You got",card[0])
        deck = card[3]
        
        # value
        player_deck_value += card[1]
        
        # ace counter
        player_ace_counter += card[2]
        
    # checks if deck value > 21
    if player_deck_value > 21:
        
        # checks if ace counter > 21
        if player_ace_counter > 0:
        
            # convert ace value to 1 in total deck
            player_deck_value -= 10
            player_ace_counter -= 1

    print()
    print("Your hand value:",player_deck_value)
    print()

    # checks if player got blackjack
    if player_deck_value == 21:
        print("You got blackjack")

    return player_deck_value, player_ace_counter, deck




'''dealer's first two cards '''
def dealer_two_cards(deck, player, bet, name):
    dealer_deck_value = 0
    dealer_ace_counter = 0

    # dealer first card
    card = random_card(deck)
    print("Dealer got",card[0])
    deck = card[3]

    dealer_deck_value += card[1]
    dealer_ace_counter += card[2]

    #dealer second card (not shown)
    card = random_card(deck)
    dealer_2nd = card[0]
    deck = card[3]

    # if player has blackjack, dealer immediately shows 2nd card
    if player == 21:
        print("Dealer's 2nd card is",card[0])
        dealer_deck_value += int(card[1])
        blackjack(player, dealer_deck_value, bet, name)
    
    print("Dealer drew their second card")
    print()

    dealer_deck_value += card[1]
    dealer_ace_counter += card[2]
    
    if dealer_deck_value > 21:
        if dealer_ace_counter > 0:
            dealer_deck_value -= 10
            dealer_ace_counter -= 1
    
    return dealer_deck_value, dealer_ace_counter, deck, dealer_2nd



''' player's choice to hit or stay '''
def player_choice(value, ace, deck, bet, name):
    choice = input("Do you want to hit or stay? ")
    print()
    valid = ['hit','stay']
    while choice not in valid:
        choice = input("Enter a valid option. Do you want to hit or stay? ")

    # player's choice to hit
    while choice == 'hit':
        card = random_card(deck)
        value += card[1]
        ace += card[2]
        deck = card[3]
        print("You got", card[0])
        print()

        if value > 21:
            if ace > 0:
                value -= 10
                ace -= 1
                print("Your hand value:", value)
                print()
            if value > 21:
                print("Your hand value:", value)
                player_loss(bet, name)
            choice = input("Do you want to hit or stay? ")

        else:
            print("Your hand value:", value)
            print()
            choice = input("Do you want to hit or stay? ")
            
    # player's choice to stay
    if choice == 'stay':
        return value, deck
    return value, deck
        



''' dealer's choice to hit or stay '''
def dealer_choice(dealer_value, ace, deck, bet, name):
    
    # dealer always hits if their hand value is under 17
    while dealer_value < 17:
        card = random_card(deck)
        dealer_value += card[1]
        ace += card[2]
        deck = card[3]
        print("Dealer got", card[0])
        print()

        if dealer_value > 21:
            if ace > 0:
                dealer_value -= 10
                ace -= 1
                print("Dealer hand value:",dealer_value)
            elif dealer_value > 21:
                print("Dealer hand value:",dealer_value)
                dealer_loss(bet, name)

        # dealer always stays if their hand value is 17 or over
        if dealer_value >= 17:
            print("Dealer stays")
            print("Dealer hand value:",dealer_value)
            break
        else:
            print("Dealer hand value:",dealer_value)
            
    return dealer_value, deck
                

        

''' determines who is winner and loser '''
def blackjack(player, dealer, bet, name):
    name_balance = load_money()
    
    if player == 21 and dealer == 21:
        print("It's a Tie!")
        name_balance[name] = int(name_balance[name])
        name_balance[name] += bet
        print("You have: $",name_balance[name])
        save_money(name_balance)

    elif player > dealer:
        print(player,"vs",dealer)
        print("You Win!") # you get 1.5 times your bet if you get blackjack
        name_balance[name] = int(name_balance[name])
        name_balance[name] += int((bet * 1.5 + bet))
        print()
        print("You have: $",name_balance[name])
        save_money(name_balance)
        
    
    elif dealer > player:
        print(player,"vs",dealer)
        print("You Lose")
        print("You have: $",name_balance[name])
    play_again()

def player_loss(bet, name):
    name_balance = load_money()
    
    print("Bust!")
    print("Your hand value over 21")
    print("You Lose")
    print("You have: $",name_balance[name])
    save_money(name_balance)
    print()
    play_again()

def dealer_loss(bet, name):
    name_balance = load_money()
    
    print("Dealer hand value over 21")
    print("You Win")
    name_balance[name] = int(name_balance[name])
    name_balance[name] += bet * 2
    print("You have: $",name_balance[name])
    save_money(name_balance)
    print()
    play_again()

def winner(player, dealer, name, bet, name_balance):
    if dealer > player:
        print(player,"vs",dealer)
        print("You Lose")
        print("You have: $",name_balance[name])
        print()
    if player > dealer:
        print(player,"vs",dealer)
        print("You Win")
        name_balance[name] = int(name_balance[name])
        name_balance[name] += bet * 2
        print("You have: $",name_balance[name])
        save_money(name_balance)
        print()
    if dealer == player:
        print(player,'vs',dealer)
        print("It's a Tie!")
        name_balance[name] = int(name_balance[name])
        name_balance[name] += bet
        print("You have: $",name_balance[name])
        save_money(name_balance)
        print()
    play_again()
    

    

''' choice to play again '''
def play_again():
    option = input("Do you want to play again? Input yes or no ")
    valid = ['yes','no']
    while option not in valid:
        option = input("Enter a valid option. Enter yes or no ")
    if option == 'yes':
        print()
        play()
    elif option == 'no':
        main()




def menu():
    ''' prints menu '''
    
    print("Menu")
    print("------------------------------------")
    print("1. Play Blackjack")
    print("2. Look up name and account balance")
    print("3. Add name")
    print("4. Add balance")
    print("5. Quit program")
    print()

def black_jack(name):

    name_balance = load_money()

    if name in name_balance:
        print("Your total balance is: $",name_balance[name])
        bet = int(input("How much money will you bet? "))
        while bet > int(name_balance[name]):
            print("Invalid bet. You bet more than your balance")
            bet = int(input("How much money will you bet? "))
        print()
        name_balance[name] = int(name_balance[name]) - bet
        save_money(name_balance)

        deck = {'King of Diamonds':10,
            'King of Hearts':10,
            'King of Clubs':10,
            'King of Spades':10,
            'Queen of Diamonds':10,
            'Queen of Hearts':10,
            'Queen of Clubs':10,
            'Queen of Spades':10,
            'Jack of Diamonds':10,
            'Jack of Hearts':10,
            'Jack of Clubs':10,
            'Jack of Spades':10,
            '10 of Diamonds':10,
            '10 of Hearts':10,
            '10 of Clubs':10,
            '10 of Spades':10,
            '9 of Diamonds':9,
            '9 of Hearts':9,
            '9 of Clubs':9,
            '9 of Spades':9,
            '8 of Diamonds':8,
            '8 of Hearts':8,
            '8 of Clubs':8,
            '8 of Spades':8,
            '7 of Diamonds':7,
            '7 of Hearts':7,
            '7 of Clubs':7,
            '7 of Spades':7,
            '6 of Diamonds':6,
            '6 of Hearts':6,
            '6 of Clubs':6,
            '6 of Spades':6,
            '5 of Diamonds':5,
            '5 of Hearts':5,
            '5 of Clubs':5,
            '5 of Spades':5,
            '4 of Diamonds':4,
            '4 of Hearts':4,
            '4 of Clubs':4,
            '4 of Spades':4,
            '3 of Diamonds':3,
            '3 of Hearts':3,
            '3 of Clubs':3,
            '3 of Spades':3,
            '2 of Diamonds':2,
            '2 of Hearts':2,
            '2 of Clubs':2,
            '2 of Spades':2,
            'Ace of Diamonds':11,
            'Ace of Hearts':11,
            'Ace of Clubs':11,
            'Ace of Spades':11}
    else:
        print('Invalid name')
        main()
    
    
    # player's first two cards
    player = player_two_cards(deck)
    player_deck_value = player[0]
    player_ace_counter = player[1]
    deck = player[2]
    
    # dealer's first two cards but 2nd one not shown
    dealer = dealer_two_cards(deck, player_deck_value, bet, name)
    dealer_deck_value = dealer[0]
    dealer_ace_counter = dealer[1]
    deck = dealer[2]
    
    # player's choice to hit or stay
    player = player_choice(player_deck_value, player_ace_counter, deck, bet, name)
    player_deck_value = player[0]
    deck = player[1]

    #dealer's 2nd card is revealed
    print("Dealer flips their 2nd card")
    print("Dealer got",dealer[3])
    print()
    print("Dealer hand value:",dealer_deck_value)
    print()

    # if dealer got blackjack
    if dealer_deck_value == 21:
        blackjack(player_deck_value, dealer_deck_value, bet, name)

    # dealer's choice to hit or stay
    dealer = dealer_choice(dealer_deck_value, dealer_ace_counter, deck, bet, name)
    dealer_deck_value = dealer[0]
    deck = dealer[1]
    
    # determines if you win or lose
    winner(player_deck_value, dealer_deck_value, name, bet, name_balance)


    
    
def find_account(name):
    ''' finds if name is in the file '''

    name_balance = load_money()
    
    # asks for name 
    if name in name_balance:
        
        # shows balance
        print("Name:", name)
        print("Balance: $", name_balance[name])

    # if name is not in file
    else:
        print("The specified name was not found")

    
def add_name(name, balance):
    ''' adds name and balance '''

    name_balance = load_money()
    
    # enter name - while loop if name exists
    if name in name_balance:
        return print("That name already exists")
    
    # enter amount of money
    name_balance[name] = balance
    save_money(name_balance)
    print("Name and balance have been added to the system")
    


def add_money(name):
    ''' adds money to name '''
    
    name_balance = load_money()

    # asks for name
    if name in name_balance:
        print("How much money will be added?", end='')
        money = int(input())
        balance = int(name_balance[name])
        balance += money
        print("Your total balnce is:",balance)
        name_balance[name] = balance
        save_money(name_balance)

    else:
        print("The specified name was not found")



def load_money():
    ''' writes each name and its balance into a dictionary '''

    name_balance = {}
    f = open("money.txt", 'r')
    for line in f:
        line = line.split()
        name_balance[line[0]] = line[1]
    f.close()
    return name_balance

def save_money(name_balance):
    ''' takes each name and its balance and writes it into the file '''

    f = open("money.txt", 'w')
    for key,value in name_balance.items():
        f.write("{0} {1} \n".format(key,value))
    f.close()

def play():
    name_balance = load_money()
    
    name = input('Enter a name ')
    while int(name_balance[name]) <= 0:
        print("You have no money")
        main()
    black_jack(name)


''' main function '''

def main():
    
    menu()

    user_input = input("Enter your choice: ")

    while user_input not in "12345":
        user_input = input("Enter a valid choice: ")

    while user_input in "1234":

        if user_input == '1':
            play()
            
        elif user_input == '2':
            name = input('Enter a name: ')
            find_account(name)
            
        elif user_input == '3':
            name = input("Enter name: ")
            balance = int(input("Enter balance: "))
            add_name(name, balance)


        elif user_input == '4':
            name = input("Enter name: ")
            add_money(name)
        print()

        menu()
        user_input = input("Enter your choice: ")

        while user_input not in "12345":
            user_input = input("Enter a valid choice: ")

    if user_input == '5':
        print("Have a good day!")
        sys.exit()

main()
