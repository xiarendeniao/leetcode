def f(nums, target):
    d = {}
    for index in range(len(nums)):
        diff = target - nums[index]
        if diff in d:
            return d[diff], index
        d[nums[index]] = index

if __name__ == '__main__':
    print f([11,21,23,12], 33)
    print f([11,22,27,21,23,12], 49)
