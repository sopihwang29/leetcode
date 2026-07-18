class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        answer = 0
        for i, m in enumerate(s):
            #if its not in the substring, remove it
            while m in substring:
                substring.pop(0)
            

            substring.append(m)
            answer = max(len(substring), answer)
            

        return answer
