def twoSum(self, nums: list[int], target: int) -> list[int]:

    hmap = {}
    for ix, data in enumerate(nums):
        if (target - data in hmap):
            return(hmap[target - data], ix)
        else:
            hmap[data] = ix
        