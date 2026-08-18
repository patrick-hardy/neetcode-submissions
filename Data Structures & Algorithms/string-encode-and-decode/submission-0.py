class Solution:

    def encode(self, strs: List[str]) -> str:
        str1 = ""
        for strings in strs:
            strLen = len(strings)
            intTS = str(strLen)
            str1 += intTS + '#' + strings
        print(str1)
        return str1

    def decode(self, s: str) -> List[str]:
# look at str
# divide by 5#'s for len of individual str


        list2 = []
        i = 0
        while (i < len(s)):
            j = i
            while (s[j] != '#'):
                j += 1
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            list2.append(word)
            i = j + 1 + length

        
        return list2