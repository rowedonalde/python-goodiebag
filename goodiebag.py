import datetime
import random

def iso_to_date(date):
    """
    Take a date in ISO 8601 YYYY-MM-DD format and return the
    equivalent Python datetime.date object.
    
    Requires:
    datetime
    
    """
    date_chunks = date.split('-')
    return datetime.date(int(date_chunks[0]), int(date_chunks[1]),
                         int(date_chunks[2]))

def quicksort(unsorted):
    """Return a sorted copy of the list of integers"""
    
    # If this list has fewer than 2 elements, it doesn't need to
    # be sorted, so this is already done:
    if len(unsorted) < 2:
        return unsorted
    
    # Pick a random pivot:
    pivot_value = random.choice(unsorted)
    
    # Check each non-pivot against the pivot. Divide them into
    # the lists of values greater than and not greater than the
    # pivot value:
    greater_than_pivot = []
    less_than_pivot = []
    pivot = []
    for i in unsorted:
        if i == pivot_value:
            pivot.append(i)
        elif i > pivot_value:
            greater_than_pivot.append(i)
        else:
            less_than_pivot.append(i)
    
    return quicksort(less_than_pivot) + pivot + quicksort(greater_than_pivot)