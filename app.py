import re
from collections import defaultdict


def generate_one_letter_differ_regex(string):
    result_regex_list = []
    for i in range(len(string) + 1):
        result_regex_list.append(re.compile(str(string[:i] + "." + string[i:])))
    return result_regex_list


def is_one_letter_differ(full_string, substring):
    one_letter_differ_regex = generate_one_letter_differ_regex(substring)
    return any([regex.search(full_string) for regex in one_letter_differ_regex])


def dfs(graph_input, start_node, max_value):
    result = max_value
    if start_node not in graph_input.keys():
        return result
    for neighbour in graph_input[start_node]:
        result = max(result, dfs(graph_input, neighbour, max_value + 1))
    return result


if __name__ == '__main__':
    # str_list = ["b", "bcad", "bca", "bad", "bd", "aaaa", "a", "bbbbbb"]
    str_list = ["crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a"]
    str_list = sorted(str_list, key=lambda string: len(string), reverse=True)
    print(str_list)
    graph = defaultdict(list)

    for i in range(1, len(str_list)):
        prev_index = i - 1
        while prev_index >= 0 and len(str_list[prev_index]) - len(str_list[i]) <= 1:
            if is_one_letter_differ(str_list[prev_index], str_list[i]):
                graph[str_list[prev_index]].append(str_list[i])
                print(str_list[prev_index] + " -> " + str_list[i])
            prev_index -= 1

    res = max([dfs(graph, root, 1) for root in graph.keys()])
    print(res)
