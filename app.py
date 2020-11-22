import re

from graph.graph import Graph


def generate_one_letter_differ_regex(string):
    result_regex_list = []
    for i in range(len(string) + 1):
        result_regex_list.append(re.compile(str(string[:i] + "." + string[i:])))
    return result_regex_list


def is_one_letter_differ(full_string, substring):
    one_letter_differ_regex = generate_one_letter_differ_regex(substring)
    return any([regex.search(full_string) for regex in one_letter_differ_regex])


if __name__ == '__main__':
    str_list = ["crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a"]
    str_list = sorted(str_list, key=lambda string: len(string), reverse=True)
    graph = Graph()

    for i in range(1, len(str_list)):
        prev_index = i - 1
        while prev_index >= 0 and len(str_list[prev_index]) - len(str_list[i]) <= 1:
            if is_one_letter_differ(str_list[prev_index], str_list[i]):
                graph.add_edge(str_list[prev_index], str_list[i])
            prev_index -= 1

    res = max([graph.find_longest_path_from(root) for root in graph.get_vertices_with_edge()])
    print(res)
