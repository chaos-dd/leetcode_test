#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class TreeNode:
    def __init__(self):
        self.children = [None]*26
        self.is_leaf = False
class Trie:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        node=self.root
        for c in word:
            idx = ord(c)-ord('a')
            if not node.children[idx]:
                node.children[idx]=TreeNode()
            node=node.children[idx]
        node.is_leaf=True

    def search(self, word: str) -> bool:
        node=self.root
        for c in word:
            idx = ord(c)-ord('a')
            if not node.children[idx]:
                return False
            node=node.children[idx]
        return bool(node.is_leaf)

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for c in prefix:
            idx = ord(c)-ord('a')
            if not node.children[idx]:
                return False
            node=node.children[idx]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

