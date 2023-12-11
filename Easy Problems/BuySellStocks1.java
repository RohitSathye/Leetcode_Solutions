class Solution {
    public int maxProfit(int[] prices) {
        int b = Integer.MAX_VALUE;
        int p =0;

        for (int i =0; i < prices.length; i++){
            if(b > prices[i]){
                b = prices[i];
            }
            else if (p < prices[i] - b){
                p = prices[i] -b;
            }
        }
        return p;
    }
}

/*
This below Code is a Python version

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit,price - min_price)
            min_price = min(min_price,price)
        
        return max_profit

/*