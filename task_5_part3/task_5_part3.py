from pathlib import Path
from prettytable import PrettyTable
from collections import Counter
import sys

def parse_log_line(line: str) -> dict:
    values = line.strip('.\n').split(' ', 3)
    keys = ['date', 'time', 'level', 'description']
    result = dict(zip(keys, values))
    return result

def load_logs(file_path: str) -> list:          
    logs_in_list = []
    with open(Path(file_path),'r', encoding="utf-8") as fh:
        while True:
            log_line = fh.readline()
            if not log_line:                                                    # Визначення кінця файлу
                break
            logs_in_list.append(parse_log_line(log_line))
        fh.close()
        return logs_in_list

def count_logs_by_level(logs: list) -> dict:
    all_levels = []
    [all_levels.append(log_dict['level']) for log_dict in logs]                 # List comprehension
    counted_levels = Counter(all_levels)
    return counted_levels

def display_log_counts(counts: dict):
    result_table = PrettyTable(['Рівень логування', 'Кількість'])
    for count in counts:
        buffer_list = []
        buffer_list.append(count)
        buffer_list.append(counts[count])
        result_table.add_row(buffer_list)                                       # метод add_row приймає тільки list
    return result_table

def filter_logs_by_level(logs: list, level: str) -> list:
    
    for line in logs:
        if line['level'].lower() == level.lower():                              # Випадок, введення рівня логування з великими\маленькими літерами
            print(f'{line['date']} {line['time']} - {line['description']}.')

def main():
    try:
        file_path = (sys.argv[1])
        if len(sys.argv) > 2:
            log_lvl = sys.argv[2]
        else:
            log_lvl = 0                                                         # опрацювання випадку можливості використання\невикористання аргументу
        list_of_dictionaries = load_logs(file_path)
        counts = count_logs_by_level(list_of_dictionaries)
        print(display_log_counts(counts))
        if log_lvl:
            filter_logs_by_level(list_of_dictionaries, log_lvl)

    except FileNotFoundError:
        print('File does not exist')
    

if __name__ == '__main__':
    main()