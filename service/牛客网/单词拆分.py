# 第一种，回溯，递归，暴力破解
def wordbreak(s, wordDict):
    word_d = {k:True for k in wordDict}
    return word_Break(s, word_d, 0)

def word_Break(s, wordDict, start):
    if start == len(s):
        return True
    for end in range(start, len(s)+1):
        word = s[start: end]
        if word in wordDict.keys():

            if word_Break(s, wordDict, end):
                # memory[word] = True
                return True

    return False

#

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"

wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(wordbreak(s, wordDict))
