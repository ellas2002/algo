import time
#gotta time start
start_time = time.perf_counter()

def bubble_sort(bubble_list):
    #n is the length of list
    n = len(bubble_list)
    #for lower bounds of the list
    for i in range(n):
        #loop starts at 0 and compares all adjacent pairs in
        # the list except last element (its already sorted)
        for j in range(0, n-i-1):
            # if j is less then the position j+1.
            if bubble_list[j] > bubble_list[j + 1]:
                # swap them :)
                temp = bubble_list[j]
                bubble_list[j] = bubble_list[j + 1]
                bubble_list[j + 1] = temp


list_test = [39, 14, 25, 3, 8, 7 ,6 ,4]
print("unsorted list is:")
print(list_test)

bubble_sort(list_test)
print("sorted list is:")
print(list_test)

print("how long it took: ")
print("--- %s milliseconds ---" % (time.perf_counter() - start_time)) #time difference


##################################################################
#######################optional challenge#########################
##################################################################


#############   added python multiple assignment feature
##############  added optional key arg
def bubble_feature_sort(listy, key=lambda x: x):
    n = len(listy)
    for i in range(1, n):
         for j in range(0, n - i - 1):
            if key(listy[j+1]) <= key(listy[j]):
                #pythons multiple assignment feature
                listy[j], listy[j + 1] = listy[j + 1], listy[j]


###### reversed the list in bubble_sort for test case in second_version
def bubble_reverse(listy, key=lambda x: x):
    n = len(listy)
    for i in range(1, n):
         for j in range(0, n - i - 1):
             #flipped sign for reverse
            if key(listy[j+1]) > key(listy[j]):
                listy[j+1], listy[j] = listy[j], listy[j+1]

########## able to detect if list is in reverse then fixes it :)
start_time = time.perf_counter()
def second_version(listy, key=lambda x: x):
    #scope of listy
    n = len(listy)
    # is_reverse is True
    is_reverse = True

    #i in range of list
    for i in range(n - 1):
        #check to see if list is reversed
        if key(listy[i]) < key(listy[i+1]):
            #if not, is_reversed is false
            is_reverse = False
    #if is_reverse is True
    if is_reverse:
        for i in range(0, n):
            for j in range(0, n - i - 1):
                #flipppp
                if key(listy[j+1]) < key(listy[j]):
                    listy[j+1], listy[j] = listy[j], listy[j+1]
    #incase the list is completely unsorted
    # else:
    #     for i in range(0, n):
    #         for j in range(0, n - i - 1):
    #             if key(listy[j + 1]) < key(listy[j]):
    #                 listy[j + 1], listy[j] = listy[j], listy[j + 1]



list = [39, 14, 25, 3, 8, 7 ,6 ,4]
list_forward =  [3, 4, 7, 8, 14, 25, 39]
list_reverse = [39, 25, 14, 8, 7, 4, 3]
print("\nunsorted list:")
print(list)

second_version(list)
print("\nsorted list in general:" )
print(list)

print("\nreversed list is:")
print(list_reverse)

second_version(list_reverse)
print("\nsorted list after reverse:")
print(list_reverse)

print("\nlist forward list is: ")
print(list_forward)

second_version(list_forward)
print("\nforward list after sort: ")
print(list_forward)

print("how long it took: ")
print("--- %s milliseconds ---" % (time.perf_counter() - start_time)) #time difference

