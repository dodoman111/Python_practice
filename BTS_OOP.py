class TreeNode:

    def __init__(self,key,val,left=None, right = None, parent = None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
                
    def hasLeftChild(self):
        if self.leftChild == None:
            return False
        else:
            return True

    def hasRightChild(self):
        if self.rightChild == None:
            return False
        else:
            return True

    def isLeaf(self):
        if bool(self.hasRightChild) | bool(self.hasLeftChild):
            return False
        else:
            True

    def isRoot(self):
        if self.parent == None:
            return True
        else:
            return False

    def isRightChild(self):
        return bool(self.parent) & bool(self.parent.rightChild == self)

    def isLeftChild(self):
        return bool(self.parent) & bool(self.parent.leftChild == self)

    def hasAnyChildren(self):
        if self.isLeaf:
            return False
        else:
            return True

    def hasBothChildren(self):
        if bool(self.rightChild) & bool(self.leftChild):
            return True
        else:
            return False
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def print_all(self):
        print(self.key, self.payload,
             self.leftChild.key if self.hasLeftChild() else 'x',
             self.rightChild.key if self.hasRightChild() else 'x')
        if self.hasLeftChild():
            self.leftChild.print_all()
        if self.hasRightChild():
            self.rightChild.print_all()

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for i in self.leftChild:
                    yield i
                yield self.key
            if self.hasRightChild():
                for i in self.rightChild:
                    yield i
    def findSuccessor(self):
        return self.rightChild.findMin()

    def findMin(self):
        current = self

        while current.hasLeftChild():
            current = current.leftChild

        return current

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size 

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key,val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                return self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent = currentNode)
        else:
            if currentNode.hasRightChild():
                return self._put(key,val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val, parent = currentNode)

    def get(self,key):
        if self.root:
            res = self._get(key,self.roof)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):
        if currentNode == None:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key > key:
            return self._get(key,currentNode.leftChild)
        elif currentNode.key < key:
            return self._get(key,currentNode.rightChild)


    def __setitem__(self,k,v):
        self.put(k,v)

    def __getitem__(self, key):     
        return self.get(key)

    def __contains__(self,key):     
        if self._get(key,self.root):
            return True
        else:
            return False

    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key is not in tree')
        elif self.size == 1 & self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error,ley not in tree')

    def __delitem__(self,key):
        self.delete(key)

    def remove(self,currentNode):
        if currentNode.isLeaf():
            if currentNode ==currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:
            if currentNode.hasLeftChild():
                if currentNode ==currentNode.parent.leftChild:
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode ==currentNode.parent.rightChild:
                    currentNode.parent.rightChild = currentNode.leftChild
                else: currentNode = currentNode.leftChild
            else:
                if currentNode ==currentNode.parent.leftChild:
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode ==currentNode.parent.rightChild:
                    currentNode.parent.rightChild = currentNode.rightChild
                else: currentNode = currentNode.rightChild
                    
                    




    def to_list(self):
        if self.root:
            return [(key, self[key]) for key in self]
        else:
            return []

    def __str__(self):
        return str(self.to_list())




def main():
        nodes = [17,5,25,2,11,29,38,9,16,7,8]
        bst = BinarySearchTree()
        
        for node in nodes:
            bst[node] = node  
        print('K V L R')
        bst.root.print_all()
        bst.delete(29)
 
if __name__ == '__main__':
    main()

