#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''


def quicksort(numbers_in_a_list):

    elements = len(numbers_in_a_list)
    #Base case
    if elements < 2:
        return numbers_in_a_list
    
    current_position = 0 #Position of the partitioning element

    for i in range(1, elements): #Partitioning loop
         if numbers_in_a_list[i] <= numbers_in_a_list[0]:
              current_position += 1
              temp = numbers_in_a_list[i]
              numbers_in_a_list[i] = numbers_in_a_list[current_position]
              numbers_in_a_list[current_position] = temp

    temp = numbers_in_a_list[0]
    numbers_in_a_list[0] = numbers_in_a_list[current_position] 
    numbers_in_a_list[current_position] = temp #Brings pivot to it's appropriate position
    
    left = quicksort(numbers_in_a_list[0:current_position]) #Sorts the elements to the left of pivot
    right = quicksort(numbers_in_a_list[current_position+1:elements]) #sorts the elements to the right of pivot

    numbers_in_a_list = left + [numbers_in_a_list[current_position]] + right #Merging everything together
    
    return numbers_in_a_list


def main():

    with open('numbers.txt') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        my_list = lines.split(", ")
        print(my_list)
           
        
   # sorted = open("sorted.txt", "a")
   # sorted.write(quicksort(lines))
   # sorted.close()
        

    return sorted


if __name__ == "__main__":
    main()
