
import networkx as nx
import graphviz


class Pipeline:

    def __init__(self):
        self.graph = nx.DiGraph()

    def add_module(self, module_name, dependencies=None):
        self.graph.add_node(module_name)
        if dependencies:
            for i, dep in enumerate(dependencies):
                self.graph.add_edge(dep, module_name, weight=i)

    def get_dependencies(self, module_name):
        deps = [(self.graph.get_edge_data(x, module_name)["weight"], x) for x in self.graph.predecessors(module_name)]

        deps.sort(key=lambda x: x[0])
        return [x[1] for x in deps]

    def get_initial_modules(self):
        return [node for node in self.graph.nodes if self.graph.in_degree(node) == 0]

    def get_dependents(self, module_name):
        return list(self.graph.successors(module_name))

    def get_dependency_count(self):
        return {node: self.graph.in_degree(node) for node in self.graph.nodes}

    def get_execution_order(self):
        return list(nx.topological_sort(self.graph))

    def to_image(self) -> None:
        nx.drawing.nx_pydot.write_dot(self.graph, r'./g.dot')
        dot = graphviz.Digraph()
        dot.render(r'./g.dot', r'./g.png')