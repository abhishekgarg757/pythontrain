import random
game_over = False
while not game_open:
    game_start = input("do you want to play blackjack? type  y or n")
    if game_start == "n":
        game_over = True
    
    deck=[1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10]
        
    player_hand=[]
    player_hand.append(random.choice(deck))
    player_hand.append(random.choice(deck))
    dealer_hand =[]
    dealer_hand.append(random.choice(deck))
    sum_player = 0
    for j in player_hand :
        sum_player = j+sum_player
    print(f"your cards : {player_hand}, current_score : {sum_player}")
    print(f"dealer first card : {dealer_hand[0]}")
    player_input = input("type y to get another card , type n to pass")
    
    condition = False
    
    while not condition:
        if player_input == "n":
            sum_dealer = 0
            print(f"delar cards are : {dealer_hand}")
            for x in dealer_hand:
                sum_dealer =sum_dealer + x
            if sum_dealer <= 21 and (sum_dealer <= sum_player):
                dealer_hand.append(random.choice(deck))
                
            elif sum_dealer <= 21 and (sum_dealer > sum_player):
                print(f"Dealer won with {sum_dealer}")
                condition = True
            else:
                print(f"you won blackjack beacuse dealer have : {sum_dealer}")
                
                condition = True
        else :
            
            sum_player = 0
            player_hand.append(random.choice(deck))
            for x in player_hand:
                sum_player =sum_player + x
            print(f"your card : {player_hand} and current score : {sum_player} and dealer have first card : {dealer_hand[0]}" )
            
            if sum_player <= 21:
                player_input = input("type y to get another card , type n to pass")
            else:
                player_input = "n"
                print("you lost because your sum is more than 21")
                condition = True
            
        
