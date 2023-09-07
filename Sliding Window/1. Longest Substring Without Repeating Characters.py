class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        try:
            count = 0
            counts = []
            st = ""
            for i in range(len(s)): # count FINAL LETTER 
                if s[i] not in st:
                    count += 1
                    st += s[i]
                else:
                    counts.append(count)
                    st = st[st.index(s[i])+1:]
                    st += s[i]
                    count = len(st)
            counts.append(count)
            return max(counts)
        except:
            return 0