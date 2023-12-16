def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in t:
        if char in char_count and char_count[char] > 0:
            char_count[char] -= 1
        else:
            return False

    return True


s = "anagram"
t = "nagaram1"

print(isAnagram(s, t))
