# HackerRank
'''
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.
The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).
The task is to calculate their comparison points by comparing each category:

If a[i] > b[i], then Alice is awarded 1 point.
If a[i] < b[i], then Bob is awarded 1 point.
If a[i] = b[i], then neither person receives a point.

Example
a = [1, 2, 3]
b = [3, 2, 1]

For element 0, Bob is awarded a point because a[0] < b[0].
For the equal elements a[1] and b[1], no points are earned.
Finally, for element 2, a[2] > b[2], so Alice receives a point.
The return array is [1, 1], with Alice's score first and Bob's second.

Function Description
Complete the function compareTriplets with the following parameter(s):

int a[3]: Alice's challenge rating.
int b[3]: Bob's challenge rating.

Returns
- int[2]: The first element is Alice's score, and the second is Bob's score.

Input Format
The first line contains 3 space-separated integers, a[0], a[1], and a[2], representing Alice's ratings.
The second line contains 3 space-separated integers, b[0], b[1], and b[2], representing Bob's ratings.

Constraints
1≤a[i]≤100
1≤b[i]≤100

Sample Input 0
5 6 7
3 6 10

Sample Output 0 --> 1 1

Explanation 0
Comparing each individual score:
*5 > 3, so Alice receives 1 point.
*6 = 6, so nobody receives a point.
*7 < 10, so Bob receives 1 point.

Alice's comparison score is 1, and Bob's comparison score is 1. Thus, we return the array [1, 1].

Sample Input 1
17 28 30
99 16 8

Sample Output 1 --> 2 1

Explanation 1
Comparing the elements:
*17 < 99, so Bob receives a point.
*28 > 16, so Alice receives a point.
*30 > 8, so Alice receives a point.

The return array is [2, 1].
'''

def compareTriplets(a, b):
    a1=b1=0
    for i in range(len(a)):   # one loop is enough for comparison with the same index
      if a[i]>b[i]:
        a1+=1
      elif b[i]>a[i]:
        b1+=1
      else:
        continue   # dont use 'break' it completely comes out of the loop
          
    return [a1,b1]
