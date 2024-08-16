import sys
from collections import defaultdict, deque

class TreeHeight:
    def read(self):
        # Read input
        self.n = int(sys.stdin.readline().strip())
        self.parent = list(map(int, sys.stdin.readline().strip().split()))
        
        # Initialize the adjacency list
        self.adjacency_list = defaultdict(list)
        
        # Build the tree from the parent list
        for child, par in enumerate(self.parent):
            if par != -1:
                self.adjacency_list[par].append(child)
    
    def compute_height(self):
        # To find the height of the tree, we perform a DFS or BFS.
        # Let's use BFS for this example.
        
        # Find the root (the node with parent -1)
        root = self.parent.index(-1)
        
        # Use a deque for BFS
        queue = deque([(root, 1)])  # (current_node, current_depth)
        max_height = 0
        
        while queue:
            node, depth = queue.popleft()
            max_height = max(max_height, depth)
            
            for child in self.adjacency_list[node]:
                queue.append((child, depth + 1))
        
        return max_height

def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

if __name__ == "__main__":
    main()
