def binary_search(elements, element):
    ''' Iterative implementation of binary search on a sorted list '''

    found = False
    
    first = 0   # Indices
    last = len(elements) - 1
    
    while (first <= last) and (not found):
        middle = (first + last) // 2   # Divide the remaining unsearched part of the list in half

        if elements[middle] == element:
            found = True

        else:
            if element < elements[middle]:
                last = middle - 1

            else:
                first = middle + 1

    return found

