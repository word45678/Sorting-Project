def quicksort(array, low, high): #the first method, called recursively that calls the partition method that sorts around the pivot and returns its index
    if low < high: #check if we've iterated through the whole array yet
        p = pivotspot(array, low, high) #call the partition method to get the correct index of our chosen pivot and place all values less than the pivot before it in the list
        quicksort(array, low, p-1) #sort the half below the pivot
        quicksort(array, p+1, high) #sort the half above the pivot
def pivotspot(array, low, high): #the partition method that returns the int index of the pivot spot and also places all values less than the pivot before it
    pivot = array[high] #creates our pivot value
    first = low-1 #creates our first comparator that will be checked against our iterated second value which is eventually the spot before the appropriate index for the pivot value
    for second in range(low,high): #iterates our second comparator through the array
        if(array[second]<=pivot): #checks if the currently checked iteration second value is less than our pivot
            first +=1 #increments the first comparator to put it in the right place as a marker for the next value 
            array[first],array[second]=array[second],array[first] #swaps first and second values to place the value at second which is less than the pivot in front of first marker
    array[first+1],array[high]=array[high],array[first+1] #do the final swap to move the pivot to its correct location after all lesser values
    return first+1 #return the index of the pivot value after sorting