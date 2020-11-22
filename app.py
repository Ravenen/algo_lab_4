import re

from graph.graph import Graph


def generate_one_letter_differ_regex(string):
    result_regex_list = []
    for dot_position in range(len(string) + 1):
        result_regex_list.append(re.compile(str(string[:dot_position] + "." + string[dot_position:])))
    return result_regex_list


def is_one_letter_differ(full_string, substring):
    one_letter_differ_regex = generate_one_letter_differ_regex(substring)
    return any([regex.search(full_string) for regex in one_letter_differ_regex])


def fill_in_graph_with_words(input_graph, input_words_list):
    for index in range(1, len(input_words_list)):
        prev_index = index - 1
        while prev_index >= 0 and len(input_words_list[prev_index]) - len(input_words_list[index]) <= 1:
            if is_one_letter_differ(input_words_list[prev_index], input_words_list[index]):
                input_graph.add_edge(input_words_list[prev_index], input_words_list[index])
            prev_index -= 1


if __name__ == '__main__':
    words_list = ["crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a"]
    words_list = sorted(words_list, key=lambda string: len(string), reverse=True)
    graph = Graph()
    fill_in_graph_with_words(graph, words_list)
    res = max([graph.find_longest_path_from(root) for root in graph.get_vertices_with_edge()])
    print(res)
