'''
def maxSum(A, i, n, prev=float('-inf')):

	if i == n:
		return 0
	excl = maxSum(A, i + 1, n, prev)

	incl = 0

	if prev + 1 != i:
		incl = maxSum(A, i + 1, n, i) + A[i]

	return max(incl, excl)
'''

def maxSum(A):

	incl = 0
	excl = 0

	for i in (A):
		new_excl = excl if excl > incl else incl

		incl = excl +i
		excl = new_excl

	return excl if excl>incl else incl

if __name__ == '__main__':
	#A =  [5,30,99,60,5,10]  # A = [12,45,0, 87, 0, 46, 90]
	A = [5,78,90,80,10]
	#print("Maximum sum is", maxSum(A, 0, len(A)))
	print("Maximum sum is", maxSum(A))

'''



def maxSubArraySum(a, size):
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        # Do not compare for all elements. Compare only
        # when  max_ending_here > 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far


if __name__ == '__main__':
    arr = [2,-8,3,-2,4,-10]
    print(maxSubArraySum(arr,len(arr)))

'''