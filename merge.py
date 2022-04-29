def mergesort(array):
    if len(array) > 1:
        divisionpoint = len(array)//2 #find middle spot of array
        front_half = array[:divisionpoint] #divide array into front and back
        back_half = array[divisionpoint:]
        mergesort(front_half) #call function to sort on front and back
        mergesort(back_half)
        #now we have to put them back together...
        i = j = k = 0 #i is the index of the front half, j is the index of the back half, and k is the index of the combined array
        while i < len(front_half) and j < len(back_half):#keeps track of if we've iterated through the shorter of the two halves yet
            if front_half[i]<back_half[j]:#checks if the current front element is less than the current back element
                array[k] = front_half[i]#adds the smaller front element
                i+=1#increments our front position marker
            else:
                array[k]=back_half[j]#adds the smaller back element
                j+=1#increments our back position marker
            k+=1#increments our combined position marker
        while i < len(front_half):#finish off adding the remaining elements from the front_half array to the combined arrays, one of these two while statements will not run at all, thus only adding the remainder of the other half that hasn't finished iterating
            array[k] = front_half[i]#adds the current front element
            i+=1
            k+=1

        while j < len(back_half):#finish off adding the remaining elements from the back_half array to the combined arrays
            array[k]=back_half[j]#adds the current back elements
            j+=1
            k+=1


        #do some stuff
    #don't do some stuff