# coding: utf-8

import argparse
import locale
import csv
import sys
import os

def main():
    locale.setlocale(locale.LC_ALL, '')
    try:
        args = arguments()
        labels, data = read(args['FILE'])
        display(labels, data, args['width'])
    except BaseException as e: sys.exit(e)

def arguments():
    parser = argparse.ArgumentParser(description='draw bar graphs from CSV files in the terminal')
    parser.add_argument('FILE', nargs='?', default='-', help='the CSV file to operate on -- if omitted, will accept input on STDIN')
    parser.add_argument('-w', '--width', type=int, default=50, help='width of graph in characters (default is 50)')
    args = vars(parser.parse_args())
    if args['FILE'] == '-' and sys.stdin.isatty():
        parser.print_help(sys.stderr)
        parser.exit(1)
    return args

def read(filename):
    labels = []
    data = []
    if not os.path.isfile(filename) and filename != '-': raise Exception(filename + ': no such file')
    file = sys.stdin if filename == '-' else open(filename, 'rb')
    reader = csv.reader(file)
    headers = next(reader) # skip these
    for line in reader:
        labels.append(line[0])
        try: data.append(float(line[1]))
        except ValueError: raise Exception(line[1] + ' is not a number')
    file.close()
    return labels, data

def display(labels, data, width):
    full_tick = '█'
    half_tick = '▌'
    total = sum(data)
    step = max(data) / width
    spacing = max(len(label) for label in labels)
    print('')
    for i in range(len(data)):
        label = labels[i]
        count = data[i]
        padding = ' ' * (spacing - len(label) + 2)
        bar = half_tick if count < step else int(count / step) * full_tick
        number = locale.format('%.2f', count, grouping=True)
        percentage = locale.format('%.2f', count / total * 100, grouping=True)
        print(label + padding + bar + ' ' + number + ' (' + percentage + '%)')
    print('')
    print('Total: ' + locale.format('%.2f', total, grouping=True))

if __name__ == '__main__':
    main()
