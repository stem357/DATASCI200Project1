"""
This module defines the User and Auction classes for a second-price ad auction simulation.
"""
import random
class User:
    """Class to represent a user with a hidden probability of clicking an ad."""
    def __init__(self):
        """Generate a probability between 0 and 1 from a uniform distribution."""
        self.__probability = random.uniform(0, 1)  # Hidden float probability
    def show_ad(self):
        """
        Simulate showing an ad to the user.
        Returns:
            bool: True if the user clicks on the ad, False otherwise.
        """
        return random.random() < self.__probability
    def __repr__(self):
        """Return a representation of the User object with hidden probability."""
        return f"User(click_probability={self.__probability:.3f})"
    def __str__(self):
        """Return a string representation of the User object."""
        return f"User with click probability {self.__probability:.3f}"
class Auction:
    """Class to represent an online second-price ad auction."""
    def __init__(self, users, bidders):
        """
        Initialize the Auction with a list of users and bidders.
        Args:
            users (list of User): List of users participating in the auction.
            bidders (list): List of bidders participating in the auction.
        """
        self.users = users
        self.bidders = bidders
        self.balances = {bidder: 0 for bidder in bidders}
        self.history = {bidder: [] for bidder in bidders}  # Track balance over time
    def execute_round(self):
        """
        Execute a single round of the auction with the following steps:
        - Select a random user
        - Collect bids from each bidder
        - Determine the winner and second-highest bid price
        - Display ad to user and update balances based on result
        """
        # Select a random user
        selected_user = random.choice(self.users)
        # Collect bids from each bidder
        bids = {bidder: bidder.bid(self.users.index(selected_user)) for bidder in self.bidders}
        # Determine the winning bidder and the second-highest bid
        sorted_bids = sorted(bids.items(), key=lambda x: x[1], reverse=True)
        winner, highest_bid = sorted_bids[0]
        second_price = sorted_bids[1][1] if len(sorted_bids) > 1 else highest_bid
        # Show ad to the selected user and check for a click
        ad_clicked = selected_user.show_ad()
        # Update winner's balance
        self.balances[winner] += 1 if ad_clicked else 0
        self.balances[winner] -= second_price
        # Notify each bidder about the auction result
        for bidder in self.bidders:
            if bidder == winner:
                bidder.notify(True, second_price, ad_clicked)
            else:
                bidder.notify(False, second_price, None)
    def __repr__(self):
        """Return a representation of the Auction object with users and qualified bidders."""
        return f"Auction with {len(self.users)} users and {len(self.bidders)} bidders"
    def __str__(self):
        """Return a string representation of the Auction object."""
        return f"Auction involving {len(self.users)} users and {len(self.bidders)} bidders"
