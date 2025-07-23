from collections import Counter

def check_inclusion(p, s):
    if len(p) > len(s):
        return False

    p_count = Counter(p)
    window_count = Counter()

    for i in range(len(s)):
        window_count[s[i]] += 1
        if i >= len(p):
            if window_count[s[i - len(p)]] == 1:
                del window_count[s[i - len(p)]]
            else:
                window_count[s[i - len(p)]] -= 1
        if window_count == p_count:
            return True
    return False

# Test cases
print(check_inclusion("ab", "eidbaooo"))  # Output: True ("ba" is a permutation)
print(check_inclusion("ab", "eidboaoo"))  # Output: False
print(check_inclusion("adc", "dcda"))     # Output: True ("dca")