"""
Write a function to find the longest common prefix
string amongst an array of strings.

If there is no common prefix, return an empty string "".

Examples:

Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def common_prefix(words):
    prev_prefix = ""
    common_prefix = ""
    for i, letter in enumerate(words[0]):
        common_prefix += words[0][i]  # n^2
        print("current common prefix ", common_prefix)
        for j in range(1, len(words)):
            # startswith method
            print("checking word ", words[j])
            print(words[j][:i + 1])
            if words[j][:i + 1] != common_prefix:
                print(common_prefix, " not common")
                return prev_prefix
        prev_prefix = common_prefix
    return common_prefix
                

if __name__ == "__main__":
    words = ["flower", "flow", "flight"]

    print(common_prefix(words))