class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fake = {}
        result = []
        fake = fake.fromkeys(nums,0)
        for number in nums:
            if number in fake:
                fake[number] += 1

        sorted_dict = dict(sorted(fake.items(), key=lambda item: item[1]))

        result = list(sorted_dict)
        return (result[-k:])
        # print(fake)
        #     if fake[number] >= k:
        #         result.append(number)
        # return list(set(result))