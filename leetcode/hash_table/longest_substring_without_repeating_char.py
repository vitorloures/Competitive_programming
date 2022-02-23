# Leetcode: Longest Substring Without Repeating Characters (Medium)


# Time Complexity: O(N²) (Worst Case)
# Space Complexity: O(1) - Since we have a limited number of non repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_substring_without_repetition = {}
        cur_string = ''
        max_substring_size = 0

        for i, char in enumerate(s):
            if not cur_substring_without_repetition.get(char):
                cur_substring_without_repetition[char] = i
                # In python, this is O(len(cur_string)
                cur_string += char

            # There is repetition
            else:
                if len(cur_substring_without_repetition) > max_substring_size:
                    max_substring_size = len(cur_substring_without_repetition)
                init_index = cur_substring_without_repetition.get(char)
                cur_string = s[init_index:i+1]
                cur_substring_without_repetition = {}
                for j, c in enumerate(cur_string):
                    cur_substring_without_repetition[c] = j+init_index

        if len(cur_substring_without_repetition) > max_substring_size:
            max_substring_size = len(cur_substring_without_repetition)
        return max_substring_size


sol = Solution()
assert sol.lengthOfLongestSubstring("abcabcbb") == 3
assert sol.lengthOfLongestSubstring("bbbbb") == 1
assert sol.lengthOfLongestSubstring("pwwkew") == 3
assert sol.lengthOfLongestSubstring("a") == 1
assert sol.lengthOfLongestSubstring("abc") == 3
assert sol.lengthOfLongestSubstring(" ") == 1
assert sol.lengthOfLongestSubstring("tmmzuxt") == 5
assert sol.lengthOfLongestSubstring("bbtablud") == 6
assert sol.lengthOfLongestSubstring("adociccpqrtywlk") == 9

# Sliding Window Technique would improve this algorithm
