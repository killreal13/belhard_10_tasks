"""
Написать функцию max_delta, в которой будет происходить чтение csv
файла world_population.csv и функцию должна возвращать год, в котором
наибольший процент прироста населения.
"""
import csv


def max_delta(some_file: csv) -> int:
    with open(some_file, 'r') as csv_file:
        writer = csv.DictReader(csv_file)
        result_dict = dict()
        for value in writer:
            result_dict[value['Year']] = value['ChangePerc']
        max_value = max(result_dict.values())
        for year, perc in result_dict.items():
            if perc == max_value:
                return year
