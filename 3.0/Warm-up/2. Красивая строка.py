def binary_search(l, r, check, checkparams):
    while l + 1 < r:
        m = l + (r - l) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m
    return l


def valid_size(size, params):
    freq = {}
    start = 0
    maxfreq = 0
    k, beautiful_string = params
    for end in range(len(beautiful_string)):
        if beautiful_string[end] not in freq:
            freq[beautiful_string[end]] = 1
        else:
            freq[beautiful_string[end]] += 1
        if end + 1 - start > size:
            freq[beautiful_string[start]] -= 1
            start += 1
        maxfreq = max(maxfreq, freq[beautiful_string[end]])
        if size - maxfreq <= k:
            return True
    return False


k = int(input())
beautiful_string = input()
print(binary_search(1, len(beautiful_string) + 1, valid_size, (k, beautiful_string)))

"""
https://leetcode.com/problems/longest-repeating-character-replacement/solutions/2805777/longest-repeating-character-replacement/
"""
