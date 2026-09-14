# Solution class
class Solution:
    # Function to move all zeroes to end
    def moveZeroes(self, arr):
        # Create temp array
        temp = [0] * len(arr)

        # Pointer to fill temp
        index = 0

        # Traverse input array
        for num in arr:
            # If non-zero, copy to temp
            if num != 0:
                temp[index] = num
                index += 1

         #Copy temp back to original
        for i in range(len(arr)):
            arr[i] = temp[i]

        # Return updated array
        return arr