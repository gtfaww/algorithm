import operator

__author__ = 'guotengfei'
__time__ = 2019 / 9 / 27

"""
Module comment
"""


def dijkstra(graph):
    costs = {}
    parents = {}
    for key, value in graph['start'].items():
        costs.setdefault(key, value)
        parents.setdefault(key, "start")
    costs.setdefault('fin', None)
    parents.setdefault('fin', None)

    # sorted_start = sorted(graph['start'].items(), key=lambda item: item[1])
    # sorted_start = sorted(graph['start'].items(), key=operator.itemgetter(1))

    update_cost(costs, graph, parents)
    print(costs['fin'])
    print(parents['fin'])


def update_cost(costs, graph, parents):
    sorted_start = get_sorted(graph['start'])
    for key, value in sorted_start:
        sorted_keys = get_sorted(graph[key])
        for a_key, a_value in sorted_keys:
            cost = costs[a_key]
            cost_key = costs[key]
            if cost is None or ((cost_key + a_value) < cost):
                costs[a_key] = (cost_key + a_value)
                parents[a_key] = key
        if a_key != 'fin':
            update_cost(costs, graph[a_key], parents)


def get_sorted(graph):
    sorted_start = sorted(graph.items(), key=operator.itemgetter(1))
    # sorted_start = sorted(zip(graph.keys(), graph.values()))
    return sorted_start


if __name__ == '__main__':
    graph = {'start': {}, 'a': {}, 'b': {}}

    graph['start']['a'] = 6
    graph['start']['b'] = 2
    graph['a']['fin'] = 1
    graph['b']['a'] = 3
    graph['b']['fin'] = 5

    dijkstra(graph)
