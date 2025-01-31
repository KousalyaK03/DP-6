# Approach:
# - We use the **expand around center** technique to find the longest palindromic substring.
# - A palindrome can be centered at a **single character (odd-length palindrome)** or 
#   between two characters (even-length palindrome).
# - We iterate through each character in the string and expand in both directions to 
#   find the longest palindrome.
# - Keep track of the longest palindrome found.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Helper function to expand around a given center
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1  # Move left pointer outward
                right += 1  # Move right pointer outward
            return s[left + 1:right]  # Return the palindromic substring

        longest_palindrome = ""

        # Iterate over each character in the string as a center
        for i in range(len(s)):
            # Check for odd-length palindrome (single character center)
            odd_palindrome = expandAroundCenter(i, i)

            # Check for even-length palindrome (two-character center)
            even_palindrome = expandAroundCenter(i, i + 1)

            # Update longest_palindrome if a longer one is found
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome

        return longest_palindrome

# Time Complexity: O(N^2)
#     - Each character is a potential center (O(N)), and for each center, 
#       we expand in both directions (O(N)), leading to O(N^2) overall.
# Space Complexity: O(1)
#     - We only use a few extra variables (constant space).