"""
BEFORE WE BEGIN LOOKING AT THE FUNCTIONS:
-> what is time complexity
-> what is space complexity

ANSWER - How the execution time or additional memory changes in relation to the
input size changing

N == the input size
"""


def removeDuplicates(input):
    inputSet = set()
    for i in input:
        inputSet.add(i)
    print(inputSet)


removeDuplicates([1, 5, 5, 3, 2, 1])
# O(N) Time, O(N) Space
# [1,1,1,1] => O(1)
# Time: worst case scenario, all unique numbers -> O(N)
# Space: as N increases, we're adding more to a new variable


def sumOfAllValues(input):
    for i in input:
        for j in input:
            print(i + j)


sumOfAllValues([1, 5, 5, 3, 2, 1])
# O(N^2) Time, O(1) Space


def findSumRemoveDuplicatesThenPrintsAllThenFirstTen(input):
    inputSet = set()

    for i in input:
        for j in input:
            inputSet.add(i+j)
    for i in input:
        print(i)
    for i in range(10):
        print(inputSet[i])

# N^2 + N + 10
# O(N^2) Time, O(N) Space

"""

TIME/SPACE COMPLEXITY GENERAL RULES
1. See if new memory is created and what the size of that could be relative to the input
(space complexity)
2. How is the time impacted if the input size increases (e.g. are there more recursive calls,
loop passes etc.)
3. Add complexities if they are separate blocks (not indented)
4. Multiply complexities if they are indented logic
5. Discard constants and insignificance: 2N -> N, N/2 -> N, N^2 + N + 10 -> N^2
(always focus on the biggest effect)

"""