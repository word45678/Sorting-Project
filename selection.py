def selectionsort(array):
    for spot in range (len(array)): #iterate through the entire list a number of times equal to the size of the list
        min = spot #set the minimum value location that will be updated as smaller values are found
        for i in range(spot+1, len(array)): #iterate through the data not confined by the minimum's that have already been set
            if(array[min]>array[i]): #check if the current minimum is bigger than the current data point being checked
                min = i #set the minimum to the new value that was found to be smaller
        array[min],array[spot]=array[spot],array[min] #swap the found minimum and the limitation spot by the iteration of first for loop