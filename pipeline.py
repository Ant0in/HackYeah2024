import networkx as nx

class Pipeline:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_module(self, module_name, dependencies=None):
        self.graph.add_node(module_name)
        if dependencies:
            for dep in dependencies:
                self.graph.add_edge(dep, module_name)
    
    def get_initial_modules(self):
        return [node for node in self.graph.nodes if self.graph.in_degree(node) == 0]

    def get_dependents(self, module_name):
        return list(self.graph.successors(module_name))
    
    def get_dependency_count(self):
        return {node: self.graph.in_degree(node) for node in self.graph.nodes}

    def get_execution_order(self):
        return list(nx.topological_sort(self.graph))