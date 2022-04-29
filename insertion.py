def insertionsort(array):
    for key_spot in range(1,len(array)):
        key = array[key_spot]
        compared_spot = key_spot-1
        while compared_spot >=0 and array[compared_spot]>key:
            array[compared_spot+1]=array[compared_spot]
            compared_spot-=1
        array[compared_spot+1]=key