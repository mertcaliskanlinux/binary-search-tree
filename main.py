from PIL import Image
import pygraphviz as pgv

class BSTNode: # Binary Search Tree (BST) sınıfı

    def __init__(self, val=None): # yapıcı metot

        self.left = None

        self.right = None

        self.val = val

    def insert(self, val): # ekleme

        if not self.val:

            self.val = val

            return


        if self.val == val:

            return



        if val < self.val: # sol boş değilse

            if self.left:

                self.left.insert(val)

                return

            self.left = BSTNode(val)

            return



        if self.right: # sağ boş değilse

            self.right.insert(val)

            return

        self.right = BSTNode(val)



    def get_min(self): # en küçük değeri bulma
 
        current = self

        while current.left is not None:

            current = current.left

        return current.val


 
    def get_max(self): # en büyük değeri bulma

        current = self

        while current.right is not None:

            current = current.right

        return current.val



    def delete(self, val): # silme

        if self == None:

            return self

        if self.right == None:

            return self.left

        if self.left == None:

            return self.right

        if val < self.val:

            if self.left:

                self.left = self.left.delete(val)

            return self

        if val > self.val:

            if self.right:

                self.right = self.right.delete(val)

            return self

        min_larger_node = self.right

        while min_larger_node.left:

            min_larger_node = min_larger_node.left

        self.val = min_larger_node.val

        self.right = self.right.delete(min_larger_node.val)

        return self



    def exists(self, val): # arama
 
        if val == self.val:

            return True



        if val < self.val:

            if self.left == None:

                return False

            return self.left.exists(val)



        if self.right == None:

            return False

        return self.right.exists(val)



    def preorder(self, vals): # kök, sol, sağ
 
        if self.val is not None:

            vals.append(self.val)

        if self.left is not None:

            self.left.preorder(vals)

        if self.right is not None:

            self.right.preorder(vals)

        return vals



    def inorder(self, vals): # sol, kök, sağ

        if self.left is not None:

            self.left.inorder(vals)

        if self.val is not None:

            vals.append(self.val)

        if self.right is not None:

            self.right.inorder(vals)

        return vals



    def postorder(self, vals):

        if self.left is not None:

            self.left.postorder(vals)

        if self.right is not None:

            self.right.postorder(vals)

        if self.val is not None:

            vals.append(self.val)

        return vals


def draw_bst(node, graph=None):
    if graph is None:
        graph = pgv.AGraph(strict=False, directed=True)
    if node:
        graph.add_node(node.val)
        if node.left:
            graph.add_edge(node.val, node.left.val)
            draw_bst(node.left, graph)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            draw_bst(node.right, graph)
    return graph

# BST ağacını oluştur
root = BSTNode(5)
root.insert(1)
root.insert(8)
root.insert(3)
root.insert(4)
root.insert(6)
root.insert(7)

k = root.get_max()
print("En büyük değer: ", k)
k = root.get_min()
print("En küçük değer: ", k)

# BST'yi çiz
tree_graph = draw_bst(root)
tree_graph.draw('bst.png', format='png', prog='dot')

# Çizilen ağacı görüntüle
img = Image.open('bst.png')
img.show()