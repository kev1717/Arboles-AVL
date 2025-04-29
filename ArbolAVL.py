import sys 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 


def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node 
        
        updateHeight(node)
        
        balance = getBalance(node)
        #Rotaciones
        if balance > 1 and value < node.left.value:  # Caso Izquierda-Izquierda
            return rotate_right(node)
        if balance < -1 and value > node.right.value:  # Caso Derecha-Derecha
            return rotate_left(node)
        if balance > 1 and value > node.left.value:  # Caso Izquierda-Derecha
            node.left = rotate_left(node.left)
            return rotate_right(node)
        if balance < -1 and value < node.right.value:  # Caso Derecha-Izquierda
            node.right = rotate_right(node.right)
            return rotate_left(node)
        
        return node
    def delete (self, value):
        """Eliminar un valor del arbol"""
        self.root= self._delete_recursive(self.root, value)
    def _delete_recursive(self, node, value):
        """Eliminación recursiva"""
        if not node:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Nodo con un solo hijo o sin hijos
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
        # Nodo con dos hijos: Obtener el sucesor en in-order (el más pequeño del subárbol derecho)
            temp = self._get_min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)

        updateHeight(node)
        
        # Balanceo
        balance = getBalance(node)

        # Rotaciones para balancear el árbol
        if balance > 1 and getBalance(node.left) >= 0:  # Caso Izquierda-Izquierda
            return rotate_right(node)
        if balance > 1 and getBalance(node.left) < 0:  # Caso Izquierda-Derecha
            node.left = rotate_left(node.left)
            return rotate_right(node)
        if balance < -1 and getBalance(node.right) <= 0:  # Caso Derecha-Derecha
            return rotate_left(node)
        if balance < -1 and getBalance(node.right) > 0:  # Caso Derecha-Izquierda
            node.right = rotate_right(node.right)
            return rotate_left(node)

        return node
    def _get_min_value_node(self, node):
        """Obtiene el nodo con el valor mínimo en un árbol/subárbol"""
        current = node
        while current.left:
            current = current.left
        return current

    def in_order_traversal(self):
        """Recorrido in-order del árbol"""
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        """Recorrido in-order recursivo"""
        if not node:
            return
        self._in_order_recursive(node.left, result)
        result.append(node.value)
        self._in_order_recursive(node.right, result)

    def visualize(self, node=None, level=0, prefix="Root: "):
        """Visualización del árbol AVL"""
        if not node:
            node = self.root
        if node:
            print(" " * (level * 4) + prefix + f"({node.value}, h={node.height}, b={getBalance(node)})")
            if node.left or node.right:
                if node.left:
                    self.visualize(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.visualize(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")


# Ejemplo de uso
if __name__ == "__main__":
    avl = AVLTree()
    values_to_insert = [10, 20, 30, 40, 50, 25]
    print("Insertando valores:", values_to_insert)
    for val in values_to_insert:
        avl.insert(val)

    print("\n--- Después de inserciones ---")
    avl.visualize()

    print("\nRecorrido in-order:", avl.in_order_traversal())

    print("\nEliminando valor 30")
    avl.delete(30)
    avl.visualize()

    print("\nRecorrido in-order después de eliminar 30:", avl.in_order_traversal())


avl = AVLTree()
values_to_insert = [10, 20, 30, 40, 50, 25]

avl2=AVLTree()


print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insert(val)

print("\n--- Después de inserciones ---")
avl.visualize()

print("\nRecorrido in-order:", avl.in_order_traversal())

print("\nEliminando valor 30")
avl.delete(30)
avl.visualize()

print("\nRecorrido in-order después de eliminar 30:", avl.in_order_traversal())