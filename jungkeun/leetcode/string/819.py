class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^a-z]', ' ', paragraph.lower())             
        for_count = []
        for p in paragraph.split() :
            if banned.count(p) == 0 :
                for_count.append(p)
        cnt = Counter(for_count).most_common()
        result, max_cnt = cnt[0]
        return result
