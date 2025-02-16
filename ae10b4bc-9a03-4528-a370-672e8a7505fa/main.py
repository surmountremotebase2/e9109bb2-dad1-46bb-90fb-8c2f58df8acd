from surmount.base_class import Strategy, TargetAllocation
from surmount.data import Asset
import numpy as np

class TradingStrategy(Strategy):
    def __init__(self):
        self.rebalance_interval = 30  # days
        self.last_rebalance = None
        # Assume we have a method to get top 10 Nasdaq 100 stocks by market cap
        self.top_nasdaq_100_by_market_cap = self.get_top_nasdaq_100_by_market_cap()
        
    @property
    def interval(self):
        return "1day"
        
    @property
    def assets(self):
        # The strategy focuses on the Nasdaq 100, but here we specify dynamically
        return self.top_nasdaq_100_by_market_cap
    
    def get_top_nasdaq_100_by_market_cap(self):
        # Placeholder for actual implementation
        # This method should return the symbols of the top 10 stocks by market cap
        return ["AAPL", "MSFT", "AMZN", "GOOGL", "FB", "TSLA", "NVDA", "PYPL", "INTC", "CMCSA"]
    
    def calculate_allocation(self):
        # Placeholder function - assumes a method to get market caps
        # This function should return allocations in a dictionary format for the top 10 stocks
        total_market_cap = sum([self.get_market_cap(stock) for stock in self.top_nasdaq_100_by_market_cap])
        allocation_dict = {stock: self.get_market_cap(stock) / total_market_cap for stock in self.top_nasdaq_100_by_market_cap}
        return allocation_dict
        
    def get_market_cap(self, symbol):
        # This is a placeholder for the actual market cap retrieving logic
        # Each symbol's market cap should be fetched from a data source
        return 100000000000  # Example fixed value, in reality, this should be dynamic
        
    def run(self, data):
        current_date = data["current_date"]  # Assume we have the current date in data
        if self.last_rebalance is None or (current_date - self.last_rebalance).days >= self.rebalance_interval:
            self.top_nasdaq_100_by_market_cap = self.get_top_nasdaq_100_by_market_cap()  # Update list in case of market cap changes
            allocation_dict = self.calculate_allocation()
            self.last_rebalance = current_date
        else:
            # Keep the allocation if within the rebalance interval
            allocation_dict = {stock: 1/len(self.top_nasdaq_100_by_market_cap) for stock in self.top_nasdaq_100_by_market_cap}
            
        return TargetAllocation(allocation_dict)