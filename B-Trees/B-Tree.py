'''
Created on 8-Mar-2017

@author: Ayush
'''


class BTrees(object):

    class Node(object):

        def __init__(self, t):
            self.keys = []
            self.children = []
            self.leaf = True
            # t is the order of the parent B-Tree. Nodes need this value to
            # define max size and splitting
            self._t = t

        def split(self, parent, payLoad):
            newNode = self.__class__(self._t)
            midpoint = self.size // 2
            splitValue = self.keys[midpoint]
            parent.add_key(splitValue)
            newNode.children = self.children[midpoint + 1:]
            self.children = self.children[:midpoint + 1]
            newNode.keys = self.keys[midpoint + 1:]
            self.keys = self.keys[:midpoint]
            if len(newNode.children) > 0:
                newNode.leaf = False
            parent.children = parent.add_child(newNode)
            if payLoad < splitValue:
                return self
            else:
                return newNode

        @property
        def _is_full(self):
            return self.size == 2 * self._t - 1

        @property
        def size(self):
            return len(self.keys)

        def add_key(self, value):
            self.keys.append(value)
            self.keys.sort()

        def add_child(self, new_node):
            i = len(self.children) - 1
            while i >= 0 and self.children[i].keys[0] > new_node.keys[0]:
                i -= 1
            return self.children[:i + 1] + [new_node] + self.children[i + 1:]

    def __init__(self, t):
        self._t = t
        if self._t <= 1:
            raise ValueError('B-Tree must have a degree of 2 or more.')
        self.root = self.Node(t)

    def insert(self, payLoad):
        node = self.root
        if node._is_full:
            new_root = self.Node(self._t)
            new_root.children.append(self.root)
            new_root.leaf = False

            # node is being set to the node containing the ranges we want for
            # payload insertion.

            node = node.split(new_root, payLoad)
            self.root = new_root
        while not node.leaf:
            i = node.size - 1
            while i > 0 and payLoad < node.keys[i]:
                i -= 1
            if payLoad > node.keys[i]:
                i += 1

            next = node.children[i]
            if next._is_full:
                node = next.split(node, payLoad)
            else:
                node = next
        # Since we split all full nodes on the way down, we can simply insert
        # the payload in the leaf.

        node.add_key(payLoad)

    def search(self, value, node=None):
        if node is None:
            node = self.root
        if value in node.keys:
            return True
        elif node.leaf:
            return False
        else:
            i = 0
            while i < node.size and value > node.keys[i]:
                i += 1
            return self.search(value, node.children[i])

    def print_order(self):
        """
        Print an level-order representation.
        """
        this_level = [self.root]
        while this_level:
            next_level = []
            output = ""
            for node in this_level:
                if node.children:
                    next_level.extend(node.children)
                output += str(node.keys) + " "
            print(output)
            this_level = next_level

if __name__ == '__main__':
    my_btree = BTrees(2)
    alist = ['F', 'S', 'Q', 'K', 'C', 'L', 'H', 'T', 'V', 'W',
             'M', 'R', 'N', 'P', 'A', 'B', 'X', 'Y', 'D', 'Z', 'E']
    for item in alist:
        my_btree.insert(item)

    my_btree.print_order()
