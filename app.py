import re

from graph.graph import Graph

INPUT_FILE_NAME = "wchain.in"
OUTPUT_FILE_NAME = "wchain.out"


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


def sort_words_by_length_descending(input_words_list):
    return sorted(input_words_list, key=lambda string: len(string), reverse=True)


def read_words_from_file(filename):
    output_words = []
    with open(filename, "r") as input_file:
        words_number = int(input_file.readline().strip())
        for line in input_file:
            output_words.append(line.strip())
    return output_words


def write_data_to_file(filename, data):
    with open(filename, "w") as output_file:
        output_file.write(str(data))


if __name__ == '__main__':
    graph = Graph()
    words_list = read_words_from_file(INPUT_FILE_NAME)

    words_list = sort_words_by_length_descending(words_list)
    fill_in_graph_with_words(graph, words_list)
    longest_chain = max([graph.find_longest_path_from(root) for root in graph.get_vertices_with_edge()])

    write_data_to_file(OUTPUT_FILE_NAME, longest_chain)
