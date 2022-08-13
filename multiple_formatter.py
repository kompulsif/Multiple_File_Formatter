from html5print import HTMLBeautifier, CSSBeautifier, JSBeautifier
from yapf.yapflib.yapf_api import FormatCode
from sql_formatter.core import format_sql
from os.path import getmtime, exists
from argparse import ArgumentParser
from threading import Thread
from time import sleep


FILE_EXTENSIONS = ('.sql', '.py', '.html', '.css', '.js')
ALL_FORMATTERS = {
    '.html': lambda text: HTMLBeautifier.beautify(text, 4, 'utf-8'),
    '.css': lambda text: CSSBeautifier.beautify(text, 4, 'utf-8'),
    '.js': lambda text: JSBeautifier.beautify(text, 4, 'utf-8'),
    '.py': lambda text: FormatCode(text)[0].strip(),
    '.sql': lambda text: format_sql(text).strip()
}
all_files = {}


def getArguments():
    parser = ArgumentParser()
    parser.add_argument(
        '--files', help='Write the file paths separated by commas.')
    parser.add_argument(
        '--example', help='Example, python multiple_formatter.py --files C:\Myfiles\myfile1.sql,C:\Myfiles2\myfiles\myfiles5.sql'
    )
    parser.add_argument(
        '--admin', help='Run the file with admin privileges. Give 1'
    )
    return parser.parse_args()


def writeFormattedText(file):
    with open(file, 'r+', encoding='utf-8', buffering=True) as f:
        text = f.read()
        formatted_text = ALL_FORMATTERS[all_files[file]](text.strip())
        f.seek(0)
        f.truncate()
        f.write(formatted_text)


def fileSChecker(file):
    try:
        file_changes = getmtime(file)
        while True:
            if file_changes < getmtime(file):
                writeFormattedText(file)
                file_changes = getmtime(file)
            sleep(0.05)

    except FileNotFoundError:
        pass


def fileExistsControl(files):
    for f in files:
        if (not exists(f)):
            print(f'\n[!]->{f} IS NOT EXISTS!<-[!]\n')
            quit()

        else:
            ex = f[f.rindex('.'):]
            if (ex not in FILE_EXTENSIONS):
                print('\n[!]-> Please check your files extensions <-[!]\n')
                quit()

            all_files[f] = ex


def fileAccessControl(files):
    try:
        for f in files:
            with open(f, 'a', encoding='utf-8') as file:
                file.readline()  # read test
                file.write(' ')  # write test

    except (PermissionError, IOError):
        print('[!]-> Permission Error, please try again with admin privileges <-[!]')
        quit()


def main():
    arguments = getArguments()
    if (arguments.files):
        files = arguments.files.split(',')
        fileExistsControl(files)
        fileAccessControl(files)

        for file in files:
            Thread(target=fileSChecker, args=(file,)).start()

    else:
        print("[*]-> Please try the --help parameter <-[*]")


if (__name__ == '__main__'):
    main()
