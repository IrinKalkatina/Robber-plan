class Solution:
    List = [2, 7, 9, 3, 1]
    oddTotalMoney = 0
    evenTotalMoney = 0
    def rob(self):
        #first we need to count money in two options: even and odd
        for i in range(0, len(self.List), 2): #for odd
            self.oddTotalMoney += self.List[i]
        for j in range(1, len(self.List), 2): #for even
            self.evenTotalMoney += self.List[j]
        #now we need to know which option we must choose to earn more money
        if self.oddTotalMoney > self.evenTotalMoney:
            return self.oddTotalMoney
        else:
            return self.evenTotalMoney #whether self.oddTotalMoney < self.evenTotalMoney or self.oddTotalMoney = self.evenTotalMoney
        
##      ##      ##      ##      ##      ##      ##      ##      ##      ##      ##      ##      ##      ##      ##      ##      ##      
newPlanForRobber = Solution()
print(newPlanForRobber.rob())
