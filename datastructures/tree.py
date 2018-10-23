

class TreeNode: 
    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value
    
    
class AVLTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        inserts a new value to this tree
            :param self: reference to this tree instance
            :param value: the new value to be inserted
        """   
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_helper(self.root, value)
        self.balance_tree()

    def delete(self, value):
        """
        removes a value from the tree
            :param self:  reference to this tree instance
            :param value: the value to be deleted

        """   
        if self.root is None:
            return False
        self.balance_tree()
        return self._delete_helper(None, self.root, value)


    def balance_factor(self):
        return self.height('right') - self.height('left')


    def _right_left_rotate(self):
        old_root = self.root
        self.root = old_root.left
        self._left_rotate()
        old_root.left = self.root
        self.root = old_root
        self._right_rotate()

    def _left_right_rotate(self):
        old_root = self.root
        self.root = old_root.right
        self._right_rotate()
        old_root.right = self.root
        self.root = old_root
        self._left_rotate()



    def _right_rotate(self):
        old_root = self.root
        new_root = old_root.left
        old_root.left = new_root.right
        new_root.right =  old_root
        self.root = new_root

    def _left_rotate(self):
        old_root = self.root
        new_root = old_root.right
        old_root.right = new_root.left
        new_root.left =  old_root
        self.root = new_root

    def balance_tree(self):
        

        state = self.state

        if state == 'balanced':
            return
        
        old_root = self.root
        if state == 'left-heavy':
            self.root = old_root.left
            left_child_state = self.state()

            if left_child_state == 'right-heavy':
                self.root = old_root
                self._right_left_rotate()
            else:
                self._right_rotate
        elif state == 'right-heavy':
            self.root = old_root.right
            right_child_state = self.state()

            if right_child_state == 'left-heavy':
                self.root = old_root
                self._left_right_rotate()
            else:
                self._left_rotate()
    
    def state(self):
        if self.balance_factor() > 1:
            return 'right-heavy'
        if self.balance_factor() < -1:
            return 'left-heavy'
        return 'balanced'
 
    def height(self, side=None):
        if self.root is not None and side == 'right':
            return 1 + self._max_child_height(self.root.right)
        if self.root is not None and side == 'left':
            return 1 + self._max_child_height(self.root.left)

        return self._max_child_height(self.root)



    def _max_child_height(self, node):
       
        if node is None:
           return 0
        
        return 1 + max(self._max_child_height(node.left), self._max_child_height(node.right))

    def _delete_helper(self, parent, node, value):
       
        if node is None:
            return False
        
        is_leaf = node.left is None and node.right is None
        if value == node.value:
          

            if parent is None:
                self.root = None
                return True

            temp_node = None
            
            if node.right is None and node.left is not None:
                temp_node = node.left
            elif  not is_leaf:
                temp_node = node.right
                temp_node.left = node.left

            if parent.right is node:
                parent.right = temp_node
            elif parent.left is node:
                parent.left = temp_node
            return True

        
        
        if is_leaf:
            return False
        if value > node.value:
            return self._delete_helper(node, node.right, value)
        
        if value < node.value:
            return self._delete_helper(node, node.left, value)
        
    def _insert_helper(self, node, value):

        """
        this is a recursive method searches for the correct leaf node of this Tree and 
        insert the value the value.

            :param self: reference to this instance
            :param node: the current node in this recursive step
            :param value: the new value
        """   
        if value >= node.value:
            if node.right is None:
                node.right = TreeNode(value)
                node.right.parent = node
            else:
                self._insert_helper(node.right, value)
        else: 
            if node.left is None:
                node.left = TreeNode(value)
                node.left.parent = node
            else:
                self._insert_helper(node.left, value)
    
    
    def get_traversal_list(self,type="pre"):
       
        items = []

        if type == 'post':
            self._post_order_traversal_helper(self.root, items)
        elif type == 'in':
            self._in_order_traversal_helper(self.root, items)
        else:
            self._preorder_traversal_helper(self.root, items)
        
        return items
    

    def _preorder_traversal_helper(self, node, items):
        if node is None:
            return
        
        items.append(node.value)
        self._preorder_traversal_helper(node.left, items)
        self._preorder_traversal_helper(node.right, items)


    def _post_order_traversal_helper(self, node, items):
        if node is None:
            return
        
        self._post_order_traversal_helper(node.left, items)
        self._post_order_traversal_helper(node.right, items)
        items.append(node.value)

    def _in_order_traversal_helper(self, node, items):

        if node is None:
            return

       
        self._in_order_traversal_helper(node.left, items)
        items.append(node.value)
        self._in_order_traversal_helper(node.right, items)
        


if __name__ == '__main__':
    main_tree = AVLTree()
    items = [3,1,2]
    for number in items:
        main_tree.insert(number)
    
    print(main_tree.get_traversal_list('in'))
    print(main_tree.get_traversal_list())
    print(main_tree.get_traversal_list('post'))

    input_next_value = str(input('What do you want to do (Enter an cancel value to quit)? ')).lower()

    while input_next_value != 'cancel':
        if input_next_value == 'pre':
           print(main_tree.get_traversal_list())
        elif  input_next_value == 'post':
            print(main_tree.get_traversal_list('post'))
        elif  input_next_value == 'in':
            print(main_tree.get_traversal_list('in'))
        elif  input_next_value == 'left-depth':
            print(main_tree.height('left'))
        elif  input_next_value == 'right-depth':
            print(main_tree.height('right'))
        elif  input_next_value == 'tree-depth':
            print(main_tree.height())
        elif  input_next_value == 'state':
            print(main_tree.state())
        elif  input_next_value == 'right-rotate':
            print(main_tree._right_rotate())
        elif  input_next_value == 'right-left-rotate':
            print(main_tree._right_left_rotate())
        elif  input_next_value == 'left-right-rotate':
            print(main_tree._left_right_rotate())
        elif  input_next_value == 'left-rotate':
            print(main_tree._left_rotate())
        elif  input_next_value == 'insert':
            value = int(input('Enter number you want to insert '))
            main_tree.insert(value)
        

        elif  input_next_value == 'remove':
        
            value = int(input('Enter number you want to remove '))
            if main_tree.delete(value):
                print('Successfully Deleted {}'.format(value))
            else:
                print('The number {} was not found'.format(value))
        
        input_next_value = str(input('Input next action  or "cancel"? ')).lower()
