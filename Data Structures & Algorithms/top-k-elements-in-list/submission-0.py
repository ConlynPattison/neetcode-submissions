class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Find and return the k most frequent integer elements in nums.

        Could count in (count, num) pair, sort the pairs by count, return list of top k.

        Max heap -> pop off the top k elements
        """

        counts = Counter(nums)
        heap = []
        heapq.heapify(heap)
        for num, count in counts.items():
            heapq.heappush(heap, tuple([-count, num]))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result