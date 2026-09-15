class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Step 1: Check if the sides can actually form a valid triangle
        if (nums[0] + nums[1] <= nums[2] or 
            nums[0] + nums[2] <= nums[1] or 
            nums[1] + nums[2] <= nums[0]):
            return "none"
        
        # Step 2: Classify the triangle using control statements
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return "isosceles"
        else:
            return "scalene"