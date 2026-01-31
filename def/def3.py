def minimal(l):
    min_number = l[0]
    for el in l:
        if el < min_number:
            min_number = el

            # print(min_number)
            return min_number

nums1 = [5, 7, 2, 9, 4]
min1 = minimal(nums1)

nums2 = [5.4, 7.2, 1.9, 2.3, 9.4, 4.2]
min2 = minimal(nums2)

if min1 < min2:
    print(min1)
else:
    print(min2)
