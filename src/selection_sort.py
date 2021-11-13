def selection_sort(elements):
    ''' Sort a sequence of numbers in-place in ascending order using selection
        sort algorithm '''
    
    for i in range(0, len(elements) - 1):
        # "Divide" the list of elements (at index <i>) into two parts: sorted
        # and not-yet-sorted
        
        index_of_min = i

        # Find the index of the smallest element in the unsorted part of the
        # list

        for j in range(i+1, len(elements)):
            if elements[j] < elements[index_of_min]:
                index_of_min = j

        # Place the smallest element of net-yet-sorted part of the list at the
        # end of the sorted part (by swapping)
        
        if index_of_min != i:
            elements[i], elements[index_of_min] = elements[index_of_min], elements[i]
