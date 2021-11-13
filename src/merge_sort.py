def _merge(left, right):
    ''' Helper function to merge two sorted lists into one '''

    result = []
    i, j = 0, 0

    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(elements):
    ''' Sort a sequence of numbers in ascending order using merge sort algorithm '''

    # A sub-list of length 0 or 1 is considered to be sorted
    
    if len(elements) < 2:
        return elements[:]

    # Keep dividing the list recursively in half until the base case of
    # sub-list length of 0 or 1 is reached. Such sublists are considered to be
    # sorted and can be merged back into one list

    else:
        middle = len(elements) // 2
        left = merge_sort(elements[:middle])
        right = merge_sort(elements[middle:])
        return _merge(left, right)

