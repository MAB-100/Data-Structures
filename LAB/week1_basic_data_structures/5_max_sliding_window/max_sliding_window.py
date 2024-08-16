from collections import deque
import sys
input = sys.stdin.read

def max_sliding_window(sequence, m):
    n = len(sequence)
    if n == 0 or m == 0:
        return []
    
    # This will store indices of sequence elements
    deq = deque()
    result = []
    
    for i in range(n):
        # Remove elements from deque that are out of the current window
        if deq and deq[0] < i - m + 1:
            deq.popleft()
        
        # Remove elements from the back of deque while they are less than
        # the current element because they are not useful for max calculation
        while deq and sequence[deq[-1]] <= sequence[i]:
            deq.pop()
        
        # Add current element's index to the deque
        deq.append(i)
        
        # If the current index is large enough to form a complete window, append result
        if i >= m - 1:
            result.append(sequence[deq[0]])
    
    return result

if __name__ == '__main__':
    data = input().split()
    n = int(data[0])
    sequence = list(map(int, data[1:n+1]))
    m = int(data[n+1])
    
    max_values = max_sliding_window(sequence, m)
    print(*max_values)
