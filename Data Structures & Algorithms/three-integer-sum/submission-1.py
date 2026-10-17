class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zero_count = 0
        neg = {}
        pos = {}
        # freq map
        for x in nums:
            if x < 0:
                pos[x] = pos.get(x, 0) + 1
            elif x > 0:
                neg[x] = neg.get(x, 0) + 1
            else:
                zero_count += 1
        
        neg_list = list(neg.keys())
        pos_list = list(pos.keys())
        out = []
        
        # 2 neg
        for i in range(len(neg_list)):
            a = neg_list[i]
            for j in range(i + 1, len(neg_list)):
                b = neg_list[j]
                c = -(a + b)
                if c in pos:
                    out.append([a, b, c])
            if neg[a] >= 2:
                c = -(2 * a)
                if c in pos:
                    out.append([a, a, c])
        
        # 2 post
        for i in range(len(pos_list)):
            a = pos_list[i]
            for j in range(i + 1, len(pos_list)):
                b = pos_list[j]
                c = -(a + b)
                if c in neg:
                    out.append([a, b, c])
            if pos[a] >= 2:
                c = -(2 * a)
                if c in neg:
                    out.append([a, a, c])
        
        # if at least 1 zero
        if zero_count:
            for x in neg_list:
                if -x in pos:
                    out.append([x, -x, 0])
        
        # if at least 3 zero:
        if zero_count >= 3:
            out.append([0, 0, 0])
    
        return out