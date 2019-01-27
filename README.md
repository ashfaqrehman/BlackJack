# Blackjack / Twenty-one


Blackjack is a popular card game. The objective of the game is to draw cards and obtain the highest total not exceeding 21.
1.1	Simplified game requirements
•	The possible card values range from 1 to 10 and, unlike a real deck, the probability of drawing a card is equal
•	The game begins by dealing two visible cards to the player (face up), and two cards to the dealer. However, in the case of the dealer, one card is visible to other players while the other is hidden.
•	The player decides whether to "hit" (draw another card), or "stand" which ends their turn.
•	The player may hit any number of times. Should the total of the cards exceed 21, the player "busts" and loses the game to the dealer.
•	If the player reaches 21, the player stands
•	The dealer's turn begins by revealing the hidden card
•	The dealer must hit if the total is 16 or less, and must stand if the value is 17 or more
•	The dealer wins all ties (i.e. if both the dealer and the player reach 21, the dealer wins)
•	The program indicates who the winner is and asks to play again

Below is an example of the game flow, but you are free to develop you own interface and formatting. The objective is to meet the outlined requirements, but there is no limit to creativity: ascii art or emoji for cards for example.
Welcome to Blackjack.
------------------------------------------------------------------

Do you wish to start a new game? (y/n):  y

You draw a 4 and a 5. Your total is 9. 

The dealer draws a 10 and a hidden card.

Hit or stand? (h/s): h

Hit! You draw a 5. Your total is 14. Hit or stand? (h/s): h

Hit! You draw 7. Your total is 21.

The dealer reveals the hidden card of 5 and has a total of 15.

Hit! The dealer draws 6. The dealer's total is 21.

Your total is 21 and the dealer's total is 21.

The dealer wins!

------------------------------------------------------------------

Do you wish start a new game? (y/n): y

You are dealt a 9 and a 10. Your total is 19.

The dealer has ben dealt a 10 and a hidden card.

Hit or stand? (h/s): h

Hit or stand? (h/s): s

You stand.

The dealer's hidden card is a 7 and has a total of 17.

The dealer stands.

You have a total of 19 and the dealer has 17.

You win!

------------------------------------------------------------------

Do you wish start a new game? (y/n): y

You are dealt an 8 and a 9. Your total is 17.

The dealer has been dealt a 4 and a hidden card.

Hit or stand? (h/s): s

You stand.

The dealer's hidden card is a 10 and has a total of 14.

The dealer hits.

The dealer is dealt a 5. The dealer's total is 19.

The dealer stands.

You have a total of 17 and the dealer has 19.

Dealer wins!
1.2.1	Bonus / Extra
•	Introduce face cards (king, queen, jack) to the card deck
•	Introduce the Ace which can either take the value of 1 or 11. Let's say the user is dealt a 10 and an ace, that would equal 21. If the user has 3, gets an ace, the total is 14. If the user hits and busts, then the ace is considered to have the value of 1.
•	Graphical representation of cards
This assignment is inspired and modified from:
https://programmingbydoing.com/a/project-blackjack.html

