# Given a string s, find the length of the longest substring without duplicate characters.
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# Return the length of the longest substring without duplicates
def find_longest_substr(string: str) -> int:
    longest_substr_len = 0
    for outer_index in range(len(string)):
        substr_len = 1
        char_map = { string[outer_index]: True }
        inner_index = outer_index + 1
        while(inner_index < len(string)):
            print(f"Outer loop {string[outer_index]} inner loop {string[inner_index]} {char_map.get(string[inner_index])}")
            if (char_map.get(string[inner_index])) != True:
                substr_len += 1
                char_map[string[inner_index]] = True
            else:
                print(f"Breaking loop for {string[outer_index]} with value {substr_len}")
                break
            inner_index += 1
        longest_substr_len = max(longest_substr_len, substr_len)
    return longest_substr_len

print(find_longest_substr("abcabcbb"))