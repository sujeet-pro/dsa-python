from typing import List

def is_palindrome(s: str, i: int, j: int) -> bool:
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def partition(s:str) -> List[List[str]]:
    res = []
    part = []

    def dfs(start_idx: int):
        if start_idx == len(s):
            res.append(part.copy())
            return
        for endIdx in range(start_idx, len(s)):
            if is_palindrome(s, start_idx, endIdx):
                part.append(s[start_idx:endIdx + 1])
                dfs(endIdx+1)
                part.pop()
    dfs(0)
    return res
