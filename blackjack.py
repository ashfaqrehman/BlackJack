#!/usr/bin/env python
import random
import os

"""
Function returns randon number between 1 and 10
"""
def get_card():
    return random.randint(1, 10)  

"""
Function returns bool True/False if total goes over 21
"""
def bust(total):    
    if total > 21:
        return True
    else:
        return False

"""
Function returns bool True/False if total equals 21 ie player hits BlackJack!
"""
def blackjack(total):    
    if total == 21:
        return True
    else:
        return False

"""
Function takes int no_of_card int and dictionary object and returns dictionary object with random card number int and sum of the cards
"""
def deal_cards(no_of_cards,deal_dict):
    if no_of_cards == 2:
         deal_dict['card_A']=get_card()
         deal_dict['card_B']=get_card()
         deal_dict['total']=deal_dict['card_A']+deal_dict['card_B']
    elif no_of_cards == 1:        
        deal_dict['card_A']=get_card()         
        deal_dict['total']+=deal_dict['card_A']
    return deal_dict


"""
Function takes two dictionary objects (player and dealer) and return string 'winner' based on the greator of the total
"""
def decide_winner(dealer_dict,player_dict):
    winner='none'
    if dealer_dict['total'] >= player_dict['total']:
        winner = 'dealer'
    else:
        winner = 'player'
    return winner        


def main():
    playgame=True
    print('\033[1m' + "Welcome to Blackjack!")      
    while playgame:
        usr_input = input("Do you wish to start a new game? (y/n):  ")
        os.system('clear')
        if not usr_input or usr_input == 'n':
            playgame = False
        else:
            player_dict = {'card_A':0,'card_B':0,'total':0}
            dealer_dict = {'card_A':0,'card_B':0,'total':0}
            player_dict = deal_cards(2,player_dict)
            dealer_dict = deal_cards(2,dealer_dict)            
            print("\nYou draw a",player_dict['card_A'], ' and a',player_dict['card_B'],". Your total is",player_dict['total']) 
            print("The dealer draws a",dealer_dict['card_A'],"and a hidden card.")
            winner = 'none'
            continue_play = True            
            while continue_play:            
                usr_input = input("\nHit or stand? (h/s):  ")
                if not usr_input or usr_input == 's':
                    print("Okay, you stand")
                    print("The dealer's hidden card is a",dealer_dict['card_B'],"and has a total of", dealer_dict['total'])
                    while dealer_dict['total'] <= 16:
                        print("\nThe dealer chooses to hit!")
                        dealer_dict = deal_cards(1,dealer_dict)
                        print("The dealer draws a",dealer_dict['card_A'],"and has a total of", dealer_dict['total'])
                    if bust(dealer_dict['total']):
                        winner='player'
                        continue_play=False
                    elif blackjack(dealer_dict['total']):
                        winner='dealer'
                        continue_play=False
                    else:
                        print("\nThe dealer stands")
                        winner=decide_winner(dealer_dict,player_dict)
                        continue_play=False                    
                elif usr_input == 'h':
                    player_dict = deal_cards(1,player_dict)
                    print("The player draws a",player_dict['card_A'],"and has a total of", player_dict['total'])
                    if bust(player_dict['total']):
                        winner='dealer'
                        continue_play=False
                    elif blackjack(player_dict['total']):
                        winner='player'
                        continue_play=False
            print("\nYou have a total of", player_dict['total'], "and the dealer has", dealer_dict['total'])
            print(winner ,"wins!")
    
    

if __name__ == "__main__":
    main()

