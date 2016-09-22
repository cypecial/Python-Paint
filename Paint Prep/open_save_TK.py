import tkFileDialog
import Tkinter

root = Tkinter.Tk()
root.withdraw()

filename = tkFileDialog.askopenfilename()
print filename

filename = tkFileDialog.asksaveasfilename()
print filename # test
