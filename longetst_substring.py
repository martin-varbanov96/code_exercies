# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
# longest_substring.py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(s == ""):
            return 0
        str_len = len(s)
        longest_string_len = 1
        for i in range(str_len):
            covered_dict = {}
            for end in range(i+1, str_len+1):
                current_letter = s[end-1]
                if(current_letter in covered_dict):
                    break
                else:
                    covered_dict[current_letter] = 1
                current_substring = s[i:end]
                longest_string_len = len(current_substring) if len(current_substring) > longest_string_len else longest_string_len
        return longest_string_len


if __name__ == "__main__":
    input_str = "pwwkew"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(input_str))