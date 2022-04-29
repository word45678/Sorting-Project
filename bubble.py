def bubblesort(array):
    limit = len(array) #define an end that will iterate as we place each largest value in the right place
    while(limit>0): #check to see if we've reached the beginning of the data yet
        swap = False #builds a small indicator to see if values have already been swapped, this will reduce unnecessary comparisons
        for i in range(0,limit-1): #iterate through the data set that hasn't been closed off by the limit's iterations yet
            if array[i]>array[i+1]: #detect if the current element is larger than the next
                array[i],array[i+1]=array[i+1],array[i] #swap the array spots
                swap = True #set our indicator to true, meaning that the array is not sorted yet and we still need to do more organizing
        if not swap:#check if we've already swapped this set, if we haven't then that means the array is already sorted and we can break the loop
            break
        limit -=1 #shrink the workable area of the dataset as iterations are run