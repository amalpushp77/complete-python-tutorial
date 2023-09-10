def isAnagram( s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hashS, hashT = {}, {}

    for i in range(len(s)):
        hashS[s[i]] = 1 + hashS.get(s[i], 0)
        hashT[t[i]] = 1 + hashT.get(t[i], 0)

    for k in hashS:
        if hashS[k] != hashT.get(k, 0):
            return False
    # print(hashS, hashT)
    return True

print(isAnagram("rat", "car"))