import tkinter
from tkinter import filedialog
import eel
import sys


def get_file_path():
    root = tkinter.Tk()
    # topmost指定(最前面)
    root.attributes('-topmost', True)
    root.withdraw()
    root.lift()
    root.focus_force()
    file_path = tkinter.filedialog.askopenfilename(parent=root)
    eel.update_path(file_path)
    print (file_path)

def test():
    root = tkinter.Tk()
    # topmost指定(最前面)
    root.attributes('-topmost', True)
    root.withdraw()
    root.lift()
    root.focus_force()
    file_path = tkinter.filedialog.askopenfilename(parent=root)
    print(file_path)

    return 1
    



#直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    test()