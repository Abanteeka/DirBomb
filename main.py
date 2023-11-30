# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pyfiglet
from termcolor import colored
import argparse

def banner():
   banner = colored(pyfiglet.figlet_format('DirBomb', font='slant'), 'yellow')
   #author
   print(f"{banner}")

def arguments():
    args = argparse.ArgumentParser()
    args.add_argument("-u", "--url", help="Target URL")
    args.add_argument("-w", "--wordlist", help="Wordlist")
    arg = args.parse_args()

