"""
Supposed to read content from each file with a specific extension of a directory and store the same in to a common file
"""
from threading import Thread
import os


def accumulate_files(fp, file_name, ext='.txt'):
    if file_name[-len(ext):] != ext:
        return
    with open(file_name) as f:
        fp.write(f.read())
    print(f'finished writing content of {file_name}')


def main():
    with open('all_file_content.txt', 'wt') as out_file:
        threads = []
        for each_entry in os.listdir():
            # accumulate_files(out_file, each_entry, '.py')
            t1 = Thread(target=accumulate_files, args=(out_file, each_entry, '.py'))
            threads.append(t1)
            t1.start()

        [t.join() for t in threads]
    # at this time out_file is already closed


if __name__ == '__main__':
    main()

