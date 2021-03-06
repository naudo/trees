class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    # Setting our own custom string representation for this object.
    # This allows us to print node.children (see Tree)
    def __repr__(self):
        return "<Node: %s>" % self.data

    # Add a child node to a node
    def add_child(self, child):
        self.children.append(child)

    def find(self, data):
        if self.data == data:
            return self

        to_visit = list(self.children)

        while(len(to_visit) != 0):

            next_node = to_visit.pop(0)

            if next_node.data == data:
                return next_node

            if len(next_node.children) != 0:
                to_visit.extend(next_node.children)

class Tree:
    def __init__(self, root_node):
        self.root = root_node

    # Search all of the nodes to find something, otherwise return None
    def find(self, data):
        return self.root.find(data)


    # Walk the tree to print out a heirarchy of nodes
    def print_tree(self):
        to_visit = [root]
        while(len(to_visit) != 0):
            current_node = to_visit.pop(0)

            if len(current_node.children) != 0:
                to_visit.extend(current_node.children)
            print "%s: " % current_node.data
            print current_node.children



print "Creating a tree and populating it"
root = Node('/')
tree = Tree(root)

tree.root.add_child(Node('Users'))
tree.root.add_child(Node('Applications'))

users = tree.find('Users')
users.add_child(Node('naudo'))
users.add_child(Node('joel'))
users.add_child(Node('cynthia'))

naudo = tree.find('naudo')
naudo.add_child(Node('Documents'))
naudo.add_child(Node('Movies'))

naudo_movies = tree.find('Movies')
naudo_movies.add_child(Node('1.mp4'))
naudo_movies.add_child(Node('2.mp4'))
naudo_movies.add_child(Node('3.mp4'))

tree.print_tree()

print "Looking for movie named 3.mp4"
print "Found! %s" % tree.find('3.mp4')
