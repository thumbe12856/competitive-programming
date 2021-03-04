from collections import defaultdict
import itertools
import time
import math

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, S):
        # print(S)
        node = self.root
        for s in S:
            if s not in node.next:
                node.next[s] = Node()
            node = node.next[s]
        node.end = True
        node.val += 1

def prime_factors(n):
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            yield i

def prime_sieve(n):
    nroot = int(math.sqrt(n))
    sieve = list(range(n+1))
    sieve[1] = 0

    for i in range(2, nroot+1):
        if sieve[i] != 0:
            m = n//i - i
            sieve[i*i: n+1:i] = [0] * (m+1)

    return [x for x in sieve if x != 0]

def get_prime_factors(n):
    primelist = prime_sieve(n)

    fs = []
    for p in primelist:
        count = 0
        while n % p == 0:
            n /= p
            count += 1
        if count > 0:
            # fs.append((p, count))
            fs += [p] * count

    return fs


T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    t = Trie()
    # s = time.time()
    vis = {}
    for n in nums:
        if n == 1:
            continue
        # t.insert(prime_factors(n))
        if n not in vis:
            # vis[n] = get_prime_factors(n)
            vis[n] = list(prime_factors(n))
        t.insert(vis[n])
    # e = time.time()
    # print(e - s)

    max_val = 0
    s = 0
    def dfs(node, level):
        max_ret = 0
        res = 0
        for n in node.next:
            ret = dfs(node.next[n], level + 1)
            if level == 0:
                max_ret = max(max_ret, ret)
            res += ret

        if level == 0:
            return res - max_ret

        if node.end:
            return node.val + res
        return res

    # s = time.time()
    print(dfs(t.root, 0))
    # e = time.time()
    # print(e - s)
