class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)  # sorts by position descending    
        stack = []
        fleet = 0
        timetoreach = []
        for car in cars:
            timetoreach.append((target - car[0])/car[1])
        
        stack = []
        for time  in timetoreach:
            if stack:
                if stack[-1] <  time:
                    stack.append(time)
            else:
                stack.append(time)
        
        print(stack)
        print(timetoreach)
        return(len(stack))