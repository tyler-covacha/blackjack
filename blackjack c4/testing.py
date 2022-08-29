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
        print("Your total balance is:",name_balance[name])
        balance = int(input("How much money will you bet?"))
        name_balance[name] = int(name_balance[name]) - balance
        print(name_balance[name])
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
    
    # player's first two cards
    player = player_two_cards(deck)
    player_deck_value = player[0]
    player_ace_counter = player[1]
    deck = player[2]
    
    # dealer's first two cards but 2nd one not shown
    dealer = dealer_two_cards(deck, player_deck_value)
    dealer_deck_value = dealer[0]
    dealer_ace_counter = dealer[1]
    deck = dealer[2]
    
    # player's choice to hit or stay
    player = player_choice(player_deck_value, player_ace_counter, deck)
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
        blackjack(player_deck_value, dealer_deck_value)

    # dealer's choice to hit or stay
    dealer = dealer_choice(dealer_deck_value, dealer_ace_counter, deck)
    dealer_deck_value = dealer[0]
    deck = dealer[1]
    
    # determines if you win or lose
    winner(player_deck_value, dealer_deck_value)


    
    
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
        print("Your total balnce is: $",balance)
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



def main():
    
    menu()

    user_input = input("Enter your choice: ")

    while user_input not in "12345":
        user_input = input("Enter a valid choice: ")

    while user_input in "1234":

        if user_input == '1':
            name = input('Enter a name')
            black_jack(name)
            
        if user_input == '2':
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

main()
