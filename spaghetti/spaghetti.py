import networkx as nx


# TODO: Extract all valid paths (check exists) from a file
# TODO: Extract all possible paths from a file and markup with validity
# TODO: Represent a file's cross references as a graph
# TODO: Iterate over discovered files
# TODO: Build a graph for a set of files


class Spaghetti:
    def __init__(self, paths):
        self.paths = paths
        self.filerefs = {k: [] for k in paths}
        self.graph = nx.DiGraph()
        self.find_file_references()
        self.build_graph()

    def find_file_references(self):
        for path in self.paths:
            with open(path, 'r') as file:
                # will update to self.filerefs
                pass

    def build_graph(self):
        for path, crossrefs in self.filerefs.items():
            # Will update self.graph
            self.graph.add_node(path)
