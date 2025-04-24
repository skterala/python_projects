print("Welcome to the secret auction program.")


#Create an empty dictionary
secret_auction_dict = {}

have_other_bidders = True

while have_other_bidders == True:
    name = input("What is your name?: ")
    bid_amt = float(input("What's your bid?: $"))

    secret_auction_dict[name] = bid_amt

    yes_no = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if yes_no.lower() == 'no':
        have_other_bidders = False

# print(secret_auction_dict)

# You can also create a function for the below logic.

max_bid = 0
max_bidder_name = ''
for key in secret_auction_dict:
    # print(secret_auction_dict[key])
    if secret_auction_dict[key] > max_bid:
        max_bid = secret_auction_dict[key]
        max_bidder_name = key

print(f"The winner is {max_bidder_name} with a bid of ${max_bid}.")