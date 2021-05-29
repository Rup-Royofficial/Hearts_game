import random


all_cards = ["Black_S2","Black_S3","Black_S4","Black_S5","Black_S6","Black_S7","Black_S8","Black_S9","Black_S10","Black_ACE(s)","Black_JACK(s)","Black_KING(s)","Black_QUEEN(s)",
              "Black_C2","Black_C3","Black_C4","Black_C5","Black_C6","Black_C7","Black_C8","Black_C9","Black_C10","Black_ACE(c)","Black_JACK(c)","Black_KING(c)","Black_QUEEN(c)",
              "Red_H2","Red_H3","Red_H4","Red_H5","Red_H6","Red_H7","Red_H8","Red_H9","Red_H10","Red_ACE(h)","Red_JACK(h)","Red_KING(h)","Red_QUEEN(h)",
              "Red_D2","Red_D3","Red_D4","Red_D5","Red_D6","Red_D7","Red_D8","Red_D9","Red_D10","Red_ACE(d)","Red_JACK(d)","Red_KING(d)","Red_QUEEN(d)"]


res_1 = random.sample(all_cards,13)
print(f"Deck of Player_1 is : {res_1}")

all_card = set(all_cards)
result_1 = set(res_1)
result_2 = all_card - result_1
res_2 = random.sample(result_2,13)
print(f"Deck of Player_2 is : {res_2}")

result_3 = set(res_2)
result_4 = all_card - (result_1|result_3)
res_3 = random.sample(result_4,13)
print(f"Deck of Player_3 is : {res_3}")


result_5 = set(res_3)
result_6 = all_card - (result_1|result_3|result_5)
res_4 = random.sample(result_6,13) 
print(f"Deck of Player_4 is : {res_4}")


card_count = 0
player_1points = 0
player_2points = 0
player_3points = 0
user_points = 0


 
while not(len(res_1) == 0) or not(len(res_2) == 0) or not(len(res_3) == 0) or not(len(res_4) == 0) : 
    player_1 = random.choice(res_1)
    print(f"Card picked by player_1 is : {player_1}")
        
    player_2 = random.choice(res_2)
    print(f"Card picked by player_2 is : {player_2}")

    player_3 = random.choice(res_3)
    print(f"Card picked by player_3 is : {player_3}")

        
    print(f"Card deck for USER : {res_4}")
    user = input("Pick a card from your deck : ")
    print(f"Card picked by player_4 is : {user}")

    
    list_1 = [player_1,player_2,player_2,user]
    list_m = max(list_1)
    print(f"The highest numbered card in this lot is : {list_m}")

    if list_m == player_1:
        remove_2 = player_2
        remove_3 = player_3
        remove_4 = user 
        tobeadded_list = [player_2,player_3,user]
        print(tobeadded_list)
        pos = 1
        print(f"The original deck of PLayer_1 is : {res_1}")
        print(f"The cards to be added in the deck are : {tobeadded_list}")

        for i in range(len(tobeadded_list)):
            res_1.insert(i + pos, tobeadded_list[i])
            print(f"Updated deck of Player_1 is {res_1}")

        if remove_2 in res_2:
            res_2.pop(res_2.index(remove_2))  

        print(f"The current deck of Player_2 : {res_2}")

        if remove_3 in res_3:
            res_3.pop(res_3.index(remove_3))

        print(f"The current deck of PLayer_3 : {res_3}")    

        if remove_4 in res_4:
            res_4.pop(res_4.index(remove_4))

        print(f"The current deck of User : {res_4}")        


    else:
        print("Didn't update Player_1's  deck")

    if list_m == player_2:
        remove_1 = player_1
        remove_3 = player_3
        remove_4 = user 
        tobeadded_list = [player_1,player_3,user]
        print(tobeadded_list)
        pos = 1
        print(f"The original deck of PLayer_2 is : {res_2}")
        print(f"The cards to be added in the deck are : {tobeadded_list}")

        for i in range(len(tobeadded_list)):
            res_2.insert(i + pos, tobeadded_list[i])
            print(f"Updated deck of Player_2 is {res_2}")

        if remove_1 in res_1:
            res_1.pop(res_1.index(remove_1))  

        print(f"The current deck of Player_1 : {res_1}")

        if remove_3 in res_3:
            res_3.pop(res_3.index(remove_3))

        print(f"The current deck of PLayer_3 : {res_3}")    

        if remove_4 in res_4:
            res_4.pop(res_4.index(remove_4))

        print(f"The current deck of User : {res_4}")        


    else:
        print("Didn't update Player_2's  deck")    

    if list_m == player_3:
        remove_1 = player_1
        remove_2 = player_2
        remove_4 = user 
        tobeadded_list = [player_1,player_2,user]
        print(tobeadded_list)
        pos = 1
        print(f"The original deck of PLayer_3 is : {res_3}")
        print(f"The cards to be added in the deck are : {tobeadded_list}")

        for i in range(len(tobeadded_list)):
            res_3.insert(i + pos, tobeadded_list[i])
            print(f"Updated deck of Player_3 is {res_3}")

        if remove_1 in res_1:
            res_1.pop(res_1.index(remove_1))  

        print(f"The current deck of Player_1 : {res_1}")

        if remove_2 in res_2:
            res_2.pop(res_2.index(remove_2))

        print(f"The current deck of PLayer_2 : {res_2}")    

        if remove_4 in res_4:
            res_4.pop(res_4.index(remove_4))

        print(f"The current deck of User : {res_4}")        


    else:
        print("Didn't update Player_3's  deck")

    if list_m == user:
        remove_1 = player_1
        remove_2 = player_2
        remove_3 = player_3 
        tobeadded_list = [player_1,player_2,player_3]
        print(tobeadded_list)
        pos = 1
        print(f"The original deck of User is : {res_4}")
        print(f"The cards to be added in the deck are : {tobeadded_list}")

        for i in range(len(tobeadded_list)):
            res_4.insert(i + pos, tobeadded_list[i])
            print(f"Updated deck of User is {res_4}")

        if remove_1 in res_1:
            res_1.pop(res_1.index(remove_1))  

        print(f"The current deck of Player_1 : {res_1}")

        if remove_2 in res_2:
            res_2.pop(res_2.index(remove_2))

        print(f"The current deck of PLayer_2 : {res_2}")    

        if remove_3 in res_3:
            res_3.pop(res_3.index(remove_3))

        print(f"The current deck of Player_3 : {res_3}")        


    else:
        print("Didn't update User's  deck")         


    if list_m == player_1 :
        player_1points += 5
        print(player_1points)
        print("Player_1 gets all the cards from this round, and thus increases his points tally")
        print("Player_2,Player_3,User wins this round")
            
    else :
        print("Error PLayer_1")    
    

    if list_m == player_2 :
        player_2points += 5
        print(player_2points)
        print("Player_2 gets all the cards from this round, and thus increases his points tally")
        print("Player_1,Player_3,User wins this round")
              
        
    else :
        print("Error PLayer_2")

    if list_m == player_3 :
        player_3points += 5
        print(player_3points)
        print("Player_3 gets all the cards from this round, and thus increases his points tally")
        print("Player_2,Player_1,User wins this round")
                
    else:
        print("Error PLayer_3")
        
    if list_m ==  user :
        user_points += 5
        print(user_points)
        print("User gets all the cards from this round, and thus increases his points tally")
        print("Player_2,Player_3,Player_1 wins this round")
                 

    else :
        print("Error User")
        


    if  (len(res_1) == 0) or (len(res_2) == 0) or (len(res_3) == 0) or (len(res_4) == 0):
        print(player_1points)
        print(player_2points)
        print(player_3points)
        print(user_points)

    else :    
        print("Points yet to be shown")

     
        
#putting this in the IF statement in card count above
    list_2 = [player_1points,player_2points,player_3points,user_points]
    list_m2 = min(list_2)
    print(list_m2)

#some work needed here

    if list_m2 == player_1points:
        print("Player_1 is the winner")

    elif list_m2 == player_2points :
        print("Player_2 is the winner")
    elif list_m2 == player_3points :
        print("Player_3 is the winner")
    elif list_m2 == user_points :
        print("User is the winner")

    else :
        print("Error ,can't print winner")
    

        