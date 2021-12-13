from collections import defaultdict
import re
def solution(s):
    dict = defaultdict(int)
    numbers = re.findall(r'\d+', s)
    for n in numbers :
        dict[int(n)] += 1
    return [ key for key, value in sorted(dict.items(), key = lambda kv: kv[1], reverse=True) ]
