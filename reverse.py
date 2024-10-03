'''9)Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 

program:
# Input: Read the list elements as a single line of space-separated integers
elements = list(map(int, input().split()))

# Output: Print the list in reverse order
print(" ".join(map(str, elements[::-1])))


'''

