import random
import time


def binarySearch(lst, key):
  # Initialize two pointers, 'low' and 'high', to the start and end of the list respectively
  low = 0
  high = len(lst) - 1
  
  #initialize a counter to count the number of iterations
  counter = 0

  # Start a loop that continues as long as 'low' is less than or equal to 'high'
  while high >= low:
    
    #increment the counter
    counter += 1
    
    # Calculate the middle index by taking the floor division of the sum of 'low' and 'high'
    mid = (low + high) // 2

    # If the search key is less than the element in the middle of the list,
    # it means the key if present, would be in the first half of the list.
    # So, update 'high' to 'mid - 1'
    if key < lst[mid]:
      high = mid - 1

    # If the search key is equal to the middle element, it means we've found the key.
    # So, return the 'mid' index
    elif key == lst[mid]:
      #return mid and the counter value
      return mid, counter
      # return mid

    # If the search key is greater than the middle element,
    # it means the key if present, would be in the second half of the list.
    # So, update 'low' to 'mid + 1'
    else:
      low = mid + 1

  # If the search key is not in the list, return a negative index which is a customary way
  # to indicate that the item is not in the list. '-low - 1' is chosen so that if you were
  # to negate the return value and subtract 1, you'd get the index where the key should be inserted.
  # return -low and the counter value
  return -low, counter
  # return -low - 1


timedata = open('timedataforbinarysearch2.csv', 'w')
max_number_tosearch_and_seed = 1000001 # 1 million
num_runs = 10  # Number of times to run binarySearch for each list size

for n in range(1000, 100001, 1000):
    total_time = 0
    #initialize totalCounter to 0
    totalCounter = 0
    
    for _ in range(num_runs):
        lst = [random.randint(1, max_number_tosearch_and_seed) for _ in range(n)]
        lst.sort()

        keyIndex = random.randint(0, n - 1)
        key = lst[keyIndex]

        t0 = time.perf_counter()
        #call binarySearch function and store the return value and counter value in two variables
        index, counter = binarySearch(lst, key)
        t1 = time.perf_counter()

        total_time += (t1 - t0)
        totalCounter += counter

    average_time = (total_time / num_runs) * 1000.0
    total_time_avg_str = "{:.12f}".format(average_time)
    
    #get average counter value
    average_counter = totalCounter / num_runs
    average_counter_str = "{:.2f}".format(average_counter)
    
    timedata.write(str(n) + ',' + total_time_avg_str + ',' + average_counter_str + '\n')
    print('List Size:', n)
    print('Average Time Taken:', total_time_avg_str)
    print('Average Search Loops:', average_counter)
    print('---')

timedata.close()
