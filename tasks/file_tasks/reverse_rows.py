"""
Написать функцию revert_rows, которая принимает путь к файлу и делает новый
файл. Создать новый файл, каждая строка которого получается из соответствующей
строки исходного файла перестановкой слов в обратном порядке.
"""


def revert_rows(file_path: str):
    with open(file_path, "r") as file:
        reverted_file = open("reverted_file.txt", "w")
        for line in file.readlines():
            new_line = list()
            new_line.append(line)
            new_line = new_line[0].split(" ")[::-1]
            new_line = ' '.join(new_line).replace("\n", "").replace(".", "") + "."
            reverted_file.write(f"{new_line}\n")
