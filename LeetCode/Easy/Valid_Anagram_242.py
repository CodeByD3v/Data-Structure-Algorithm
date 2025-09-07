"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        st = {}

        for ch in set(list(s)):
            st[ch] = s.count(ch)
        
        for ch in t:
            if ch not in st:
                return False
            st[ch]-=1
            if st[ch] < 0:
                return False
        
        for count in st.values():
            if count!=0:
                return False

        return True
