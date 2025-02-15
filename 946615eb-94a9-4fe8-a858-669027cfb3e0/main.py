from surmount.base_class import Strategy, TargetAllocation
from surmount.data import Asset, FinancialStatement

class TradingStrategy(Strategy):
    def __init__(self):
        # Assuming these are the top 10 QQQ components by market cap
        self.tickers = ["AAPL", "MSFT", "AMZN", "FB", "GOOGL", "GOOG", "INTC", "CMCSA", "NVDA", "PEP"]
        # Placeholder for market caps, should be dynamic or updated regularly
        self.market_caps = {
            "AAPL": 2500e9, 
            "MSFT": 2200e9, 
            "AMZN": 1600e9, 
            "FB": 900e9, 
            "GOOGL": 1500e9, 
            "GOOG": 1500e9, 
            "INTC": 250e9, 
            "CMCSA": 240e9, 
            "NVDA": 800e9, 
            "PEP": 200e9
        }
        self.data_list = [FinancialStatement(i) for i in self.tickers]

    @property
    def interval(self):
        # Rebalance monthly
        return "1month"

    @property
    def assets(self):
        return self.tickers

    @property
    def data(self):
        return self.data_list

    def run(self, data):
        # Calculate total market cap sum of the top 10 components
        total_market_cap = sum(self.market_caps.values())
        # Calculate weight for each stock based on market cap
        allocation_dict = {ticker: self.market_caps[ticker] / total_market_cap for ticker in self.tickers}
        
        return TargetAllocation(allocation_dict)