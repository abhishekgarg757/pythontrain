dict1 ={}
bid_list=[]
def bidgame():
    name = input("enter your name")
    bid = int(input("enter your bid value"))
    bid_list.append(bid)    
    dict1[name]=bid
    option1 = input("you want to play again : yes or no")
    if option1 == "yes":
        bidgame()
    else:
        bid_list.sort()
        biggest_bid = int(bid_list[len(bid_list)-1])
        for key,value in dict1.items():
            if value == biggest_bid:
                print(f'The winner  with the highest bid is {key}')

bidgame()
        

    

