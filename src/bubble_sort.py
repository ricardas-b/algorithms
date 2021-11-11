def bubble_sort(elements):

    # After n-th iteration, n-th largest element is guaranteed to be in the
    # right place. So we can exclude that element from later iterations, having
    # progressively fewer element pairs to compare
    
    for i in range((len(elements) - 1), 0, -1):

        # Use flag to detect if no elements were swapped during the last
        # iteration. It indicates that the elements are already sorted so the
        # algorithm can terminate early
        
        swapped = False

        for j in range(0, i):

            # Compare element pairs and swap elements if element on the left is
            # larger than element on the right
            
            if (elements[j] > elements[j+1]):
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True

        if not swapped:
            break

    return elements
