class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        for i in range(len(temperatures)):
            t = temperatures[i]
            while len(stack)> 0  and stack[-1]['temp'] <t:
                tobj = stack.pop()
                tval = tobj['temp']
                tidx = tobj['idx']
                diff = i - tidx
                output[tidx] = diff
            
            stack.append({'temp':t,'idx':i})
        
        return output

        