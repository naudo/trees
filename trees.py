class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    # Setting our own custom string representation for this object.
    # This allows us to print node.children (see Tree)
    def __repr__(self):
        return self.data

    # Add a child node to a node
    def add_children(self, child):
        child.parent = self
        self.children.append(child)

    # This is a helper function to give us a userfriendly path to the file
    def path(self):
        path = []
        to_visit = [self]

        while(len(to_visit) > 0):
            current_node = to_visit.pop()

            path.insert(0,current_node.data)

            if current_node.parent is not None:
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
        to_visit = [root]
        while(len(to_visit) != 0):
            current_node = to_visit.pop()
            if current_node.data == data:
                return current_node

            if len(current_node.children) != 0:
                to_visit = to_visit + current_node.children
    # Walk the tree to print out a heirarchy of nodes
    def output(self):
        to_visit = [root]
        while(len(to_visit) != 0):
            current_node = to_visit.pop()

            if len(current_node.children) != 0:
                to_visit = to_visit + current_node.children
            print "%s: " % current_node.data
            print current_node.children





print "Creating a tree and populating it"
root = Node('/')
tree = Tree(root)

tree.root.add_children(Node('Users'))
tree.root.add_children(Node('Applications'))

users = tree.find('Users')
users.add_children(Node('naudo'))
users.add_children(Node('hb'))

naudo = tree.find('naudo')
naudo.add_children(Node('Documents'))
naudo.add_children(Node('Movies'))

naudo_movies = tree.find('Movies')
naudo_movies.add_children(Node('1.mp4'))
naudo_movies.add_children(Node('2.mp4'))
naudo_movies.add_children(Node('3.mp4'))


tree.output()

print "Finding Movie 3.mp4"
print tree.find('3.mp4').path()
