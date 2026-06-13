class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #an empyt set() is named hashset here (assigned)
        hashset=set()
        #now run n over all nums values
        for n in nums:
            #check if someone is already sitting in nums
            if n in hashset:
                return True
            hashset.add(n)
        return False       