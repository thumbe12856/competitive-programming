class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        import bisect
        count = {
            "a": a,
            "b": b,
            "c": c
        }
        
        sorted_key = sorted(list(count.keys()), key=lambda k: -count[k])
        ans = ""
        while sorted_key:
            idx = 0
            if len(ans) >= 2 and sorted_key[idx] == ans[-1] and sorted_key[idx] == ans[-2]:
                idx = 1

            if idx >= len(sorted_key):
                break

            letter = sorted_key.pop(idx)
            if idx == 0:
                if count[letter] >= 2:
                    count[letter] -= 2
                    ans += letter + letter
                    sorted_key.append(letter)
                    sorted_key = sorted(sorted_key, key=lambda k: -count[k])
                elif count[letter] == 1:
                    count[letter] -= 1
                    ans += letter
                else:
                    break
            elif idx == 1:
                if count[letter] >= 1:
                    count[letter] -= 1
                    ans += letter
                    sorted_key.append(letter)
                    sorted_key = sorted(sorted_key, key=lambda k: -count[k])
                else:
                    break
            else:
                break            
        
        return ans
    

s = Solution()
print(s.longestDiverseString(1, 1, 7))
print(s.longestDiverseString(2, 2, 1))
print(s.longestDiverseString(7, 1, 0))
print(s.longestDiverseString(0, 8, 11))
