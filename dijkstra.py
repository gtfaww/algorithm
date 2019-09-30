import operator

__author__ = 'guotengfei'
__time__ = 2019 / 9 / 27

"""
Module comment
"""

graph = {'start': {}, 'a': {}, 'b': {}, 'c': {}, 'd': {}, 'fin': {}}
costs = {}
parents = {}
processed = []


def get_lowest_cost_noed(costs):
    sorted_costs = get_sorted(costs)
    for cost in sorted_costs:
        if cost[0] not in processed:
            processed.append(cost[0])
            return cost


def dijkstra():
    for key, value in graph['start'].items():
        costs.setdefault(key, value)
        parents.setdefault(key, "start")
    costs.setdefault('fin', float('inf'))
    parents.setdefault('fin', None)

    # sorted_start = sorted(graph['start'].items(), key=lambda item: item[1])
    # sorted_start = sorted(graph['start'].items(), key=operator.itemgetter(1))
    cost = get_lowest_cost_noed(costs)
    while cost is not None:
        update_cost(cost)
        cost = get_lowest_cost_noed(costs)

    print(costs['fin'])
    print(parents['fin'])


def update_cost(cost):
    key, value = cost
    sorted_keys = get_sorted(graph[key])
    for a_key, a_value in sorted_keys:
        if a_key not in costs.keys():
            costs[a_key] = a_value + value
            parents[a_key] = key
        else:
            cost = costs[a_key]
            if (value + a_value) < cost:
                costs[a_key] = (value + a_value)
                parents[a_key] = key


def get_sorted(graph):
    sorted_start = sorted(graph.items(), key=operator.itemgetter(1))
    # sorted_start = sorted(zip(graph.keys(), graph.values()))
    return sorted_start


if __name__ == '__main__':
    graph['start']['a'] = 5
    graph['start']['b'] = 2
    graph['a']['d'] = 4
    graph['a']['c'] = 2
    graph['b']['a'] = 8
    graph['b']['c'] = 7
    graph['d']['c'] = 6
    graph['d']['fin'] = 3
    graph['c']['fin'] = 1

    dijkstra()
