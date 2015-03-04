# This is a Node that allows for the parent relationship to be stored.
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    # Setting our own custom string representation for this object.
    # This allows us to print node.children (see Tree)
    def __repr__(self):
        return "<Node: %s>" % self.data

    # Add a child node to a node
    def add_child(self, child):
        child.parent = self
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

    # This is a helper function to give us a userfriendly path to the node
    def path(self):
        path = []
        to_visit = [self]

        while(len(to_visit) > 0):
            current_node = to_visit.pop(0)

            path.insert(0,current_node.data)

            if current_node.parent:
                to_visit.append(current_node.parent)
        # Returns a file path
        # e.g. "/Users/naudo/Movies/movie3.mp4"
        # Slice a duplicate / off of the beginning
        return "/".join(path)[1:]

class Tree:
    def __init__(self, root_node):
        self.root = root_node

    # Search all of the nodes to find something, otherwise return None
    def find(self, data):
        return root.find(data)

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

print "Finding Movie 3.mp4"
print "Located at %s" % tree.find('3.mp4').path()
