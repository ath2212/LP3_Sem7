import heapq

from numpy import chararray


class Node:
    def __init__(self, frequency:int, symbol:chararray, left=None, right=None) -> None:
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right
        self.val = ''
    
    def __lt__(self, nxt):
        return self.frequency < nxt.frequency

def printNodes(root, val=''):
    val += root.val
    if root.left:
        printNodes(root.left, val)
    if root.right:
        printNodes(root.right, val)

    if(not root.left and not root.right):
        print(f"{root.symbol} -> {val}")

charachters = ['a', 'b', 'c', 'd', 'e', 'f']
frequencies = [ 5, 9, 12, 13, 16, 45]

nodes = []
for x in range(len(charachters)):
    heapq.heappush(nodes, Node(frequencies[x], charachters[x]))

while len(nodes)>1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.val = '0'
    right.val = '1'
    newNode = Node(left.frequency+right.frequency, left.symbol+right.symbol, left, right)

    heapq.heappush(nodes, newNode)

printNodes(nodes[0])