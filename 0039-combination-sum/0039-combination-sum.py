class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        original_list = sol(candidates, target)
        
        seen = set()
        ans = []
        
        for arr in original_list:
            
            sorted_tuple = tuple(sorted(arr))
            
            if sorted_tuple not in seen:
                seen.add(sorted_tuple)
                ans.append(arr)
                
        return ans
    

def sol(nums, target):

	if target == 0:
		return [[]]
	if target < 0:
		return []

	ans = []

	for n in nums:

		new_target = target - n

		v = sol(nums, new_target)

		for x in v:
			x.insert(0, n)
			ans.append(x)

	return ans

