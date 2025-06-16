#实现一个快速排序算法
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
# 测试快速排序算法
if __name__ == "__main__":
    test_array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quick_sort(test_array)
    print("原数组:", test_array)
    print("排序后数组:", sorted_array)