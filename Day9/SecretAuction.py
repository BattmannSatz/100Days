# This is a bidding auction app. Ask the user to enter many inputs with name and price.
# once the first user enters the name and price, ask if there are any other users. If there are any user then clear the screen and handover the computer
# to second user. Use a dictionary to compare the prices of both the user or many user and print who is the winner and their price

from turtle import clear
import art

print(art.logo)
bids = {}
bidding_finished = False

def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for key, value in bidding_record.items():
        if value > highest_bid:
            highest_bid = value
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}")



while not bidding_finished:
    name = input("Enter the Name")
    price = int(input("Enter the Bid Price $"))
    bids [name] = price
    should_continue = input("Are there any other bidders? Type Yes or no")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bid(bids)
    elif should_continue == "yes":
        clear()


