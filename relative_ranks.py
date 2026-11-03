from typing import List         

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)

        ranks = {
            value: str(i + 1)
            for i, value in enumerate(sorted_scores)
        }

        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        answer = []

        for s in score:
            rank = int(ranks[s])

            if rank <= 3:
                answer.append(medals[rank - 1])
            else:
                answer.append(str(rank))

        return answer