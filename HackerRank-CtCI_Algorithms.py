
# ===== Merge Sort ========================================================== #

def mergesort(alist):
    if len(alist) <= 1:
        return alist
    else:
        mid = len(alist)/2
        left = mergesort(alist[:mid])
        right = mergesort(alist[mid:])

        return merge(left, right)

def merge(left, right):
    sorted_list = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_list.append(left[left_idx])
            left_idx += 1
        else:
            sorted_list.append(right[right_idx])
            right_idx += 1

    return sorted_list + right[right_idx:] + left[left_idx:]