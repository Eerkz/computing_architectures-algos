# Understanding the Problem:
# The distance between each tile is essentially the same as the jump strength needed to go to the next tile. If a jump strength is less than the distance between two tiles, a jump will be unsuccessful. No matter where the largest distance is to be jumped is located in the array or how many subtractions were made while getting to that point, it should ALWAYS be the case that JUMP STRENGTH >= distance between the tiles. What we need to do is to make sure that JUMP STRENGTH >= distance is always true for each pair of tile to get through all the tiles. The jump strength that satisfies all the distances will be the minimum needed k to jump through all the tiles in the array. Setting the minimum k any less than this will fail jumping between two tiles with the largest distance between them. 

# As a human:
# 1. Determine the distances between each consecutive tiles. 
# 2. Take the largest of the distances, L.
# 3. Set L as the minimum k. 

# As a computer:

# Algorithm:
# 1. Initially set the minimum k as 0.
# 2. Iterate through the array. In each iteration, compute the distance between arr[i] and arr[i+1]
# 3. In each iteration, we check if the current minimum k is enough to jump through the next tile by comparing if the minimum k (strength) is greater than or equal to the current distance that needs to be jumped, if not, we set the current distance as the minimum k. 
# 4. Return minimum k. 


#O(n) solution and no need to save the distances between arr elements

def findK(arr, n):
    neededStrength = 0
    for i in range(n - 1) :
        distance = abs(arr[i] - arr[i + 1])
        if (distance >= neededStrength):
            neededStrength = distance
       
        print(distance , end = " ")

    return neededStrength
 
# Driver Code
if __name__=="__main__":
    #test cases:
    arr = [3,9,10,14] #answer 6
    arr2 = [1,7,8,12,15,20,25] #answer 6
    arr3 = [3,6,9,10,14] #answer 4
    arr4 = [1,4,8,12,15,20,25] #answer 5
    arr5 = [1,4,8,15,17,20] #answer 7
    arr6 = [1,2,3] #answer 1
    n = len(arr6)
 
    k = findK(arr6, n)
    print("\nminimum k is:", k)
