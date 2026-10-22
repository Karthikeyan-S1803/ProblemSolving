# HackerRank
'''
Given an array of integers, find the sum of its elements.For example, if the array , , so return .

Function Description --> Complete the  function with the following 

parameter(s):
ar[n]: an array of integers

Returns
int: the sum of the array elements

Input Format
The first line contains an integer denoting the size of the array.
The second line contains  space-separated integers representing the array's elements.

Constraints --> 0<n,ar[i]<=1000

Sample Input
STDIN           Function
-----           --------
6               ar[] size n = 6
1 2 3 4 10 11   ar = [1, 2, 3, 4, 10, 11]

Sample Output: 31
'''

def simpleArraySum(ar):
    sum=0
    for i in range(len(ar)):
        sum+=ar[i]  #NOTE: need to access the element in that index not the index
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
