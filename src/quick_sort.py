def quick_sort(elements):
    ''' Sort a sequence of numbers in ascending order using quick sort algorithm '''

    # A sub-list of length 0 or 1 is considered to be sorted
    
    if len(elements) < 2:
        return elements[:]

    # Select arbitrary position for pivot (the 1st element of the list)
    
    pivot = elements[0]

    # Track the index of the end of left sub-list
    
    index_of_left = 0

    # Keep dividing the list recursively in respect to the pivot value
    
    for i in range(1, len(elements)):
        if elements[i] <= pivot:
            index_of_left += 1
            elements[i], elements[index_of_left] = elements[index_of_left], elements[i]

    # Place the pivot element at the correct location (in between the left and
    # right sub-lists)
    
    elements[0], elements[index_of_left] = elements[index_of_left], elements[0]

    left = quick_sort(elements[:index_of_left])
    right = quick_sort(elements[index_of_left+1:])

    return left + [pivot] + right

