
def intersection(nums1, nums2):
    res = [i for i in nums1 if i in nums2]
    return list(set(res))


if __name__ == '__main__':
    nums1 = [1, 2, 2, 3]
    nums2 = [2, 2]
    print(intersection(nums1, nums2))

