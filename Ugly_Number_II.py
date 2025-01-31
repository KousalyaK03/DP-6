# Approach:
# - We use a *min-heap* (priority queue) to generate ugly numbers in order.
# - Start with the smallest ugly number `1`.
# - Multiply each extracted number by `2, 3, and 5`, and add them to the heap if they are not already seen.
# - Use a *set* to avoid duplicates.
# - Repeat until we extract the nth ugly number.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Min-heap to store ugly numbers in ascending order
        heap = [1]
        seen = set([1])  # Set to avoid duplicate entries
        
        # Factors to generate new ugly numbers
        factors = [2, 3, 5]

        ugly_number = 1  # Variable to store the nth ugly number

        # Extract the smallest number from the heap n times
        for _ in range(n):
            ugly_number = heapq.heappop(heap)  # Get the smallest ugly number
            
            # Generate new ugly numbers by multiplying with 2, 3, and 5
            for factor in factors:
                new_ugly = ugly_number * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)  # Mark as seen
                    heapq.heappush(heap, new_ugly)  # Add to the heap
        
        return ugly_number  # The nth extracted ugly number is the answer

# Time Complexity: O(N log N)
#     - We insert and extract from a heap N times (each operation is O(log N)).
#
# Space Complexity: O(N)
#     - We store N numbers in the heap and set.
# Example usage:
sol = Solution()
print(sol.nthUglyNumber(10))  # Output: 12