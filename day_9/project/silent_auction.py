from art import logo
import os


# Display Project Logo
print(logo)

# Is there more bid?
more_bid = True

# Empty bids list
bids = []

# Highest bid and bidder
highest_bid = 0
highest_bidder = ""

while more_bid:
    # Ask for Name and Bidding inputs
    user_name = str(input("What is your name?: "))
    user_bid = int(input("What's your bid?: $"))

    def silent_auction(username, userbid):
        # Add name and bid into the bids dictionary as key and value
        new_bid = {}
        new_bid["name"] = username
        new_bid["bid_amount"] = userbid

        bids.append(new_bid)

    silent_auction(userbid=user_bid, username=user_name)

    # Is there more bidders?
    should_continue = str(input("Are there any other bidders? Type 'yes' or 'no'.\n")).lower()
    if should_continue != 'no':
        # Clear the screen
        os.system("clear")
    else:
        more_bid = False
        for bid in bids:
            if bid["bid_amount"] > highest_bid:
                highest_bid = bid["bid_amount"]
                highest_bidder = bid["name"]
        
        # Clear the screen
        os.system("clear")

        # Print the bid winner and their bid amount
        print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")