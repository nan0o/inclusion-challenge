"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice. You can return the answer in any order. 
"""

def check_pairs(array, array_size, total):
      
    #Create an empty hashmap to store the indices 
    hashmap = {}
    results = []
    for i in range(0, array_size):
        temp = total-array[i]
        if (temp in hashmap):
            results.append([hashmap[temp], i])
        hashmap[array[i]] = i
    return results

input_array = [1, 17, 45, 6, 10, 8]
sum = 18
results = check_pairs(input_array, len(input_array), sum)
for result in results:
    # Print it like so to return a list of the indices
    # as the challenge indicates
    print(result)