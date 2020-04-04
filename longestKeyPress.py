import collections
def longestKeyPress(keys_and_times):
    time_for_longest_keypress = -1
    temp_key = 0
    time_for_previous_keypress = 0

    for i in range(len(keys_and_times)):
        key_press_time = keys_and_times[i][1] - time_for_previous_keypress
        if key_press_time > time_for_longest_keypress:
            time_for_longest_keypress = key_press_time
            temp_key = keys_and_times[i][0]
        time_for_previous_keypress = keys_and_times[i][1]
    return chr(ord('a') + temp_key)



def segment(x,arr):
    maxElement = -float("inf")
    n = len(arr)
    Qi = collections.deque()
    for i in range(x):
        while Qi and arr[i] < arr[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    for i in range(x, n):
        if arr[Qi[0]] > maxElement:
            maxElement = arr[Qi[0]]
        while Qi and Qi[0] <= i - x:
            Qi.popleft()

        while Qi and arr[i] < arr[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    if arr[Qi[0]] > maxElement:
        maxElement = arr[Qi[0]]

    return maxElement

if __name__ == '__main__':
    print(longestKeyPress([[0,2],[1,3],[0,7]]))
    print(longestKeyPress([[0, 1], [0, 3], [4, 5],[5,6],[4,10]]))
    print(longestKeyPress([[0, 3], [20, 5], [2, 6],[15,7],[9,8],[19,9],[24,10],[4,12],[3,13]]))

    print(segment(1,[1000000000]))