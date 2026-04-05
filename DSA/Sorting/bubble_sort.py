# Problem: Bubble Sort
# Difficulty: Easy
# Approach: In-place comparison sort (Optimized)
# Time Complexity: O(n^2) worst/average, O(n) best
# Space Complexity: O(1)
#
# Problem Statement:
# Given an array of integers, sort the array in ascending order
# by repeatedly swapping adjacent elements if they are in the wrong order.

def bubble_sort(nums):
    """
    Sorts an array in-place using bubble sort.
    Optimized to stop early if no swaps are made during a pass.
    """
    n = len(nums)
    
    for i in range(n):
        swapped = False
        
        # The last i elements are already sorted and in place
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                # Swap elements if they are in the wrong order
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
                
        # If no elements were swapped in the inner loop, array is sorted
        if not swapped:
            break

    return nums


# ---- Test Cases ----
if __name__ == "__main__":
    print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # Expected: [11, 12, 22, 25, 34, 64, 90]
    print(bubble_sort([5, 1, 4, 2, 8]))               # Expected: [1, 2, 4, 5, 8]
    print(bubble_sort([1, 2, 3, 4, 5]))               # Expected: [1, 2, 3, 4, 5]
    print(bubble_sort([3, 3]))                        # Expected: [3, 3]
    print(bubble_sort([]))                            # Expected: []
