def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # 기저 조건 (더 이상 나눌 수 없음)

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # Divide & Conquer
    right = merge_sort(arr[mid:])   # Divide & Conquer

    return merge(left, right)       # Combine

def merge(left, right):
    result = []
    i = j = 0

    # 두 배열을 병합
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result