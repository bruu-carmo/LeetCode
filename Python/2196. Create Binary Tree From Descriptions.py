"""2196. Create Binary Tree From Descriptions
Medium
Topics
Companies
Hint
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

 

3 Example 1:


# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]
# Explanation: The root node is the node with value 50 since it has no parent.
# The resulting binary tree is shown in the diagram.
# Example 2:


# Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
# Output: [1,2,null,null,3,4]
# Explanation: The root node is the node with value 1 since it has no parent.
# The resulting binary tree is shown in the diagram.
 

Constraints:


1 <= descriptions.length <= 104
descriptions[i].length == 3
1 <= parenti, childi <= 105
0 <= isLefti <= 1
The binary tree described by descriptions is valid."""

# PRIMEIRO TESTE
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#   def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

# To construct the binary tree from the given descriptions, we'll follow these steps:
# Create a mapping of nodes: We'll use a dictionary to store each node using its value. This way, we can efficiently access any node to attach its children.
# Track the parent-child relationships: We'll use another dictionary to keep track of which nodes are children. This helps us identify the root node later (the root node will be the one that is never a child).
# Build the tree: Using the descriptions, we'll create the tree by linking the child nodes to their respective parent nodes based on whether they should be a left or right child.
# Identify the root node: The root node will be the one that is never a child of any other node. We'll find this node by checking our child-tracking dictionary.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions):
        nodes = {}
        is_child = set()
        
        # Step 1: Create nodes and build the tree structure
        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
                
            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
                
            is_child.add(child)
        
        # Step 2: Identify the root (the node which is never a child)
        root = None
        for parent, child, isLeft in descriptions:
            if parent not in is_child:
                root = nodes[parent]
                break

     
        return root

     
# Explanation:
# Node Creation and Tree Building:
# We iterate over each description and create nodes for both the parent and child if they don't already exist.
# We then link the child node to the parent node based on the isLeft value.
# We also add the child node's value to the is_child set to keep track of nodes that are children.
# Identifying the Root Node:
# After processing all descriptions, we iterate over them once more to find a node that is a parent but not listed as a child. This node is identified as the root node.
# This approach ensures that we efficiently build the tree and correctly identify the root node.
