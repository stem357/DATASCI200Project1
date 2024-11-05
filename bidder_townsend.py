"""
This module defines the Bidder class, which participates in the auction simulation.
"""
import random
class Bidder:
    """Class to represent a bidder in an online second-price ad auction."""
    def __init__(self, num_users, num_rounds):
        """Initialize the bidder with user count, round count, and round counter."""
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.balance = 0  # Starting balance for each bidder
        self.bid_strategy = {}  # Placeholder for bidding strategy based on users
    def bid(self, user_id):
        """
        Return a non-negative bid amount based on the user_id.
        Here, implement a random bid strategy as an example.
        """
        bid_amount = round(random.uniform(0.1, 2.0), 3)  # Random bid between 0.1 and 2.0 dollars
        self.bid_strategy[user_id] = bid_amount  # Record bid strategy for analysis
        return bid_amount
    def notify(self, auction_winner, price, clicked):
        """Update bidder attributes based on auction results.
        Adjust balance if won, otherwise observe outcome.
        """
        if auction_winner:
            # Adjust balance based on winning price and click result
            self.balance += 1 if clicked else 0
            self.balance -= price
    def __repr__(self):
        """Return representation of the Bidder object."""
        return f"Bidder(balance={self.balance})"
    def __str__(self):
        """Return string representation of the Bidder object."""
        return f"Bidder with balance {self.balance}"

