def mergesort(array):
    if len(array) > 1:
        divisionpoint = len(array)//2 #find middle spot of array
        front_half = array[:divisionpoint] #divide array into front and back
        back_half = array[divisionpoint:]
        mergesort(front_half) #call function to sort on front and back
        mergesort(back_half)
        #now we have to put them back together...
        i = j = k = 0 #i is the index of the front half, j is the index of the back half, and k is the index of the combined array
        while i < len(front_half) and j < len(back_half):
            if front_half[i]<back_half[j]:
                array[k] = front_half[i]
                i+=1
            else:
                array[k]=back_half[j]
                j+=1
            k+=1
        while i < len(front_half):
            array[k] = front_half[i]
            i+=1
            k+=1

        while j < len(back_half):
            array[k]=back_half[j]
            j+=1
            k+=1


        #do some stuff
    #don't do some stuff