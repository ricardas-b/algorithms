def selection_sort(elements):
    ''' Sort in-place a sequence of numbers using selection sort algorithm '''
    
    for i in range(0, len(elements) - 1):
        # "Divide" the list of elements (at index <i>) into two parts: sorted
        # and not-yet-sorted
        
        min_index = i

        # Find the index of the smallest element in the unsorted part of the
        # list

        for j in range(i+1, len(elements)):
            if elements[j] < elements[min_index]:
                min_index = j

        # Place the smallest element of net-yet-sorted part of the list at the
        # end of the sorted part (by swapping)
        
        if min_index != i:
            elements[i], elements[min_index] = elements[min_index], elements[i]
