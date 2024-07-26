from tkinter import *

root = Tk()
root.title('Roman numerals')
root.geometry('400x300')

numRomanMap = (
('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9),
('V', 5), ('IV', 4), ('I', 1))


def roman_number():
    roman_string = ''
    n = float(eval(ent.get()))
    wrongValue = ('Number is out of range')
    if not 1 <= n <= 9999:
        return wrongValue
    for numeral, integer in numRomanMap:
        while n >= integer:
            roman_string += numeral
            n -= integer
    print(roman_string)


def decimal_number(s):
    dec_number = 0
    s = str(eval(ent.get()))
    index = []
    for i in range(len(s)):
        for numeral, integer in numRomanMap:
            if s[i] == numeral:
                index.append(integer)
    index.append(0)
    for i in range(len(s)):
        if index[i] >= index[i + 1]:
            dec_number = dec_number + index[i]
        else:
            dec_number = dec_number - index[i]
    print(dec_number)


Convertb = Button(root, text='Convert', command=roman_number)
ent = Entry(root)
ent.pack()
ent.delete(0, END)
ent.insert(0, 'Enter a number')
Convertb.pack()

root.mainloop()