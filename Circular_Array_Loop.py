class Solution:
    def circularArrayLoop(self,nums):
        s, l = [], len(nums)
        for i, n in enumerate(nums):
            if i in s: continue  # check repeated i
            d = []
            while n * nums[i] > 0:  # forward or backward movements only
                if i in d:
                    if d[-1] != i:
                        return True  # the cycle's length must be greater than 1
                    else:
                        break
                d.append(i)  # store i for a cycle
                s.append(i)  # store i without checking the repetition in the following
                i = (i + nums[i]) % l
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.circularArrayLoop([1, 1, 1, 1,1, 0, 0, 1,1, 1, 1, 1]))

    #[[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1]]