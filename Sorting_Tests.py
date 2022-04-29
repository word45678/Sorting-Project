import sys
import time
import bubble
import insertion
import quick
import selection
import merge
#import our various sort functions from our nearby files

def main():
    sys.setrecursionlimit(1500)
    print("\n")
    print("Please input a number to find: ")
    original = sys.stdout

    dataset = [28,83,73,63,2,40,81,41,15,84,75,5,17,93,75,40,68,6,31,24,92,26,4,37,97,1,82,88,56,86,86,27,16,1,10,74,40,10,70,47,96,56,88,34,57,13,99,7,25,11,52,19,6,15,65,19,29,64,43,55,10,77,3,86,62,22,35,98,45,38,48,20,53,55,2,50,36,100,21,57,98,15,89,44,50,69,80,56,79,48,88,3,46,42,21,42,24,84,64,99,56,89,63,74,94,20,42,32,9,14,91,90,9,87,17,70,96,85,9,40,71,92,36,37,71,10,88,60,23,17,40,26,75,47,79,31,21,58,70,38,27,18,74,42,53,30,6,27,96,70,33,83,79,78,1,82,50,17,19,1,94,52,38,53,56,63,60,13,53,60,14,82,45,78,24,15,50,12,39,91,45,2,52,56,35,18,56,86,76,95,47,56,21,48,20,13,72,50,43,8,2,45,56,9,71,55,18,66,59,52,32,19,2,25,75,60,94,72,92,77,9,50,57,75,37,99,25,78,50,49,85,11,22,68,96,73,80,59,6,19,89,53,16,54,46,80,97,2,51,18,35,98,70,14,97,77,29,28,47,95,18,33,8,38,53,39,21,25,100,63,19,81,88,76,36,73,23,93,89,57,14,7,42,67,42,89,81,32,39,45,99,92,41,79,8,62,63,79,24,48,25,48,15,57,5,72,75,21,96,75,17,95,98,85,44,22,33,87,11,23,20,56,100,64,31,69,17,60,2,26,35,82,32,81,90,57,34,80,86,3,33,69,95,87,18,37,40,75,82,81,98,34,39,80,49,69,26,35,78,83,74,85,75,37,73,69,45,34,48,17,76,16,70,62,65,11,37,21,100,9,71,10,15,11,33,46,30,18,69,64,72,38,30,73,53,91,87,63,10,85,16,9,54,79,83,30,39,96,28,3,13,50,96,21,57,36,28,49,60,55,98,21,84,29,97,84,34,76,60,2,9,19,20,75,52,71,1,23,72,41,36,13,43,21,84,69,23,99,45,73,32,72,37,60,82,27,39,51,38,34,14,11,49,28,80,67,85,69,38,39,63,6,87,87,89,33,33,22,30,30,46,99,97,13,25,89,19,43,8,54,13,8,65,85,1,25,71,60,79,56,34,96,97,61,37,37,1,35,7,29,51,90,18,79,29,39,66,92,61,96,58,100,54,98,39,34,85,9,5,1,86,23,11,63,23,7,41,71,72,14,100,2,55,47,67,93,29,43,43,55,32,22,10,48,46,16,20,44,79,67,56,56,90,93,91,13,34,70,4,55,60,18,10,64,45,2,36,24,22,58,42,3,56,27,55,2,9,91,11,67,8,48,49,69,18,77,28,2,3,5,70,16,100,24,98,51,52,8,49,65,52,8,17,8,46,75,58,33,42,20,52,90,62,94,20,34,30,42,15,17,52,11,7,75,62,16,8,21,8,4,90,66,52,59,3,22,33,60,100,9,24,100,64,16,4,96,53,44,84,41,37,67,78,15,43,86,7,42,58,48,39,5,73,29,42,76,29,56,78,63,84,32,80,50,64,10,32,84,2,4,78,61,56,35,56,4,50,6,5,95,40,8,53,85,90,35,75,72,25,29,11,68,4,65,6,68,4,25,29,7,21,48,80,31,7,53,51,84,82,7,70,31,30,68,8,60,21,54,20,6,62,45,73,38,45,75,88,90,97,68,47,48,39,37,44,68,79,55,56,8,17,5,92,2,68,72,38,5,24,38,12,81,17,96,74,36,23,49,79,27,83,75,23,63,22,38,44,62,7,58,69,34,73,17,64,8,26,42,4,65,82,32,81,77,25,19,99,44,14,42,79,11,58,63,5,11,67,55,99,64,45,33,31,2,89,71,47,97,17,12,43,40,1,3,47,46,55,45,55,2,59,65,63,7,60,22,68,64,46,90,30,5,52,18,78,74,54,72,84,38,76,26,51,74,44,81,71,72,27,79,96,84,13,99,66,4,27,35,75,56,74,15,55,59,45,50,73,54,10,85,57,25,48,27,4,65,77,83,40,22,61,59,65,61,87,91,18,39,50,89,94,92,49,95,20,42,58,40,9,90,26,14,84,23,88,97,92,42,89,2,69,63,13,38,61,51,10,49,29,1,9,78,92,70,88,69,75,16,4,15,85,65,62,91,62,92,93,36,41,1,2,98,51,77,98,50,97,77,79,82,90,79,8,71,14,23,29,88,1,29,100,50,60,80,54,86,40,88,23,52,49,20,67,9,5,68,82,64,29,80] #example dataset

    with open('output.txt', 'w') as f:
        sys.stdout = f
        print("Unsorted: " + str(dataset)) #introductory line
        print("\n")
        start = time.time() #begin timer
        for i in range(100):
            tab = dataset
            bubble.bubblesort(tab) #run the sort function
        end = time.time() #stop timer
        sorts_ranks = {'Bubblesort':end-start} #add the completed sort and time it took to our list


        start = time.time() #begin timer
        for i in range(100):
            tab = dataset
            insertion.insertionsort(tab) #run the sort function
        end = time.time() #stop timer
        sorts_ranks.update({'Insertionsort':end-start}) #update our list of sorts and times

        start = time.time() #begin timer
        for i in range(100):
            tab = dataset
            selection.selectionsort(tab) #run the sort function
        end = time.time() #stop timer
        sorts_ranks.update({'Selectionsort':end-start})
        

        start = time.time() #begin timer
        for i in range(100):
            tab = dataset
            quick.quicksort(tab, 0, len(tab)-1) #run the sort function
        end = time.time() #stop timer
        sorts_ranks.update({'Pivotsort':end-start})
        

        start = time.time() #begin timer
        for i in range(100):
            tab = dataset
            merge.mergesort(tab) #run the sort function
        end = time.time() #stop timer
        sorts_ranks.update({'Mergesort':end-start})

        
        sorts_ranks = dict(sorted(sorts_ranks.items(),key=lambda x: x[1])) #sort the set of sorts and their times
        rank = 1 #a little indicator to keep track of the ranking of the currently iterated sorts_ranks element
        for key,value in sorts_ranks.items():
            print(str(rank) + ". " + str(key)+ " took " + str(round(value,8)) + " seconds, averaging " + str(round(value/100,8)) + " seconds per sort.")#show us how long each sort took
            rank+=1
        print("\n")
        print("Sorted dataset: " + str(tab)) #display sorted data as proof of function
        sys.stdout = original
    print("Sorts completed and logged to nearby output.txt")

if __name__ == '__main__':
    main()