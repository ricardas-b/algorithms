def insertion_sort(elements):
    ''' Sort in-place a sequence of numbers using insertion sort algorithm '''

    # Consider the first element as 1-element sorted sub-array and start with the
    # second element
    
    for i in range(1, len(elements)):
        current = elements[i]
        j = i - 1

        # Search for the correct place to insert the current element in the
        # sorted sub-array by shifting elements in sorted sub-array by one
        # position towards the end of array

        while (j >= 0) and current < elements[j]:
            elements[j+1] = elements[j]
            j -= 1

        # Place the current element in the correct position
        
        elements[j+1] = current

