from tkinter import *

window = Tk()

def get_data():
    file = open('passwords.txt', 'r')
    lines = file.readlines()
    lines = [lines[i].split() for i in range(len(lines))]

    output = ''
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            output += decrypter(lines[i][j]) + ' '
        output += '\n'
    return output

def add_record():
    file = open('passwords.txt', 'a')
    file.write(encrypter(mailBox.get()) + ' ')
    file.write(encrypter(loginBox.get()) + ' ')
    file.write(encrypter(passwordBox.get()) + '\n')
    file.close()
    Label(window, text = get_data(), bg = 'white', fg = 'black', font = 'note 12 bold').grid(row = 3, column = 0, columnspan = 2, pady = 5)


def encrypter(data):
        return ''.join([chr(ord(data[i])+5) for i in range(len(data))])[::-1]

def decrypter(data):
    return ''.join([chr(ord(data[i])-5) for i in range(len(str(data)))])[::-1]

window.title('Password keeper')
window.configure(background = 'white')

Label (window, text = 'Give site name:', bg = 'white', fg = 'black', font = 'none 12 bold').grid(row = 0, column = 0, sticky = W)
Label (window, text = 'Give login:', bg = 'white', fg = 'black', font = 'none 12 bold').grid(row = 0, column = 1, sticky = W)
Label (window, text = 'Give password:', bg = 'white', fg = 'black', font = 'none 12 bold').grid(row = 0, column = 2, sticky = W)

mailBox = Entry(window, bg = 'white')
loginBox = Entry(window, bg = 'white')
passwordBox = Entry(window, bg = 'white')

mailBox.grid(row = 1, column = 0, sticky = W)
loginBox.grid(row = 1, column = 1, sticky = W)
passwordBox.grid(row = 1, column = 2, sticky = W)


Button(window, text = 'Add', width = 10, command=add_record).grid(row = 2, column = 0)

Label(window, text = get_data(), bg = 'white', fg = 'black', font = 'note 12 bold').grid(row = 3, column = 0, columnspan = 2, pady = 5,)
window.mainloop()
