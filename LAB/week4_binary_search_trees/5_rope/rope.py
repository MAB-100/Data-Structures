class Rope:
    def __init__(self, s):
        self.s = s
 
    def result(self):
        return self.s
 
    def process(self, i, j, k):
        # Step 1: Cut the substring S[i..j]
        cut_substring = self.s[i:j+1]
       
        # Step 2: Remove the cut substring from the original string
        remaining_string = self.s[:i] + self.s[j+1:]
       
        # Step 3: Insert the cut substring after the k-th character
        # If k is 0, insert at the beginning.
        if k == 0:
            self.s = cut_substring + remaining_string
        else:
            self.s = remaining_string[:k] + cut_substring + remaining_string[k:]
 
# Read input
s = input().strip()
rope = Rope(s)
q = int(input().strip())
 
# Process each query
for _ in range(q):
    i, j, k = map(int, input().strip().split())
    rope.process(i, j, k)
 
# Output the final result
print(rope.result())