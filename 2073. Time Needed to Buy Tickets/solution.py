class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        target_tickets = tickets[k]
        
        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], target_tickets)
            else:
                time += min(tickets[i], target_tickets - 1)
        
        return time
        
