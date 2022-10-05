from tkinter import *
root=Tk()

textBox=Text(root, height=20, width=70)
textBox.pack()

string = "Nothing yet inputed"

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    global string
    string = inputValue
    # print(string)
    return string

buttonCommit=Button(root, height=1, width=10, text="Commit",
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

mainloop()

if __name__ == "__main__":
    print(string)