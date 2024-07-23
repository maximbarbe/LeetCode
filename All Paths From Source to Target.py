class Solution:

    def path(self, node, graph, cur_path, paths):
        if node == len(graph) - 1:
            paths.append(cur_path + [len(graph) - 1])
            return
        for dest in graph[node]:
            
            self.path(dest, graph, cur_path + [node], paths)

        else:
            return
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        for edge in graph[0]:
            self.path(edge, graph, [0], res)
        return res