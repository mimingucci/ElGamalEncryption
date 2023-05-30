import math
import tkinter as tk
from tkinter import ttk
import random
from math import pow


def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

def isPrime(n):
    if (n <= 1) :
      return False;
    if (n <= 3):
      return True;
    if (n%2 == 0 or n%3 == 0):
      return False;

    for i in range(5, int(math.sqrt(n)), 6):
        if (n%i == 0 or n%(i+2) == 0):
           return False;

    return True;


def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)


    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

def binhPhuongVaNhan(a, b, c):
    s=format(b, 'b')
    p=1;
    for i in range(0, len(s)):
      if(s[i]=='1'):
          p = p * p
          p = p % c
          p = p * a
          p = p % c
      else:
          p=p*p
          p=p%c
    return p

def ocolitMoRong(ri, ri1):
        q=[]
        s=[]
        t=[]
        for i in range(100):
            q.append(0)
            s.append(0)
            t.append(0)
        ri2 = int(-1)
        i = int(0)
        n = int(ri)
        while (ri2 != 0):
            q[i + 1] = int(int(ri) / int(ri1))
            ri2 =int(int(ri) % int(ri1))
            if (i==0):
                    s[i] = 1
                    t[i] = 0
            elif (i==1):
                    s[i] = 0
                    t[i] = 1
            else:
                    s[i] = s[i - 2] - q[i - 1] * s[i - 1]
                    t[i] = t[i - 2] - q[i - 1] * t[i - 1]
            ri = ri1
            ri1 = ri2
            i+=1
        s[i] = s[i - 2] - q[i - 1] * s[i - 1]
        t[i] = t[i - 2] - q[i - 1] * t[i - 1]
        return t[i] if t[i]>0 else (n+t[i])

def gen_key(q):
    key = random.randint(2, q-2)
    while gcd(q, key) != 1:
        key = random.randint(2, q - 2)

    return key


def encrypt(msg):
    en_msg = []
    y1 = binhPhuongVaNhan(alpha, k, p)
    j = binhPhuongVaNhan(beta, k, p)

    for i in range(0, len(msg)):
        en_msg.append(y1)
        y2=(ord(msg[i])*j)%p
        en_msg.append(y2)
    encry_msg=""
    for i in range(0, len(en_msg)):
        encry_msg+=chr(en_msg[i]%p)
    return encry_msg

def maHoa(msg, p, k, a, alpha):
    en_msg = []
    y1 = binhPhuongVaNhan(alpha, k, p)
    t=ocolitMoRong(p-1, k)
    while(t<=0):
        t+=p-1
    for i in range(0, len(msg)):
        y2=(((ord(msg[i])-a*y1)%(p-1))*t)%(p-1)
        en_msg.append(y2)
    encry_msg = ""
    for i in range(0, len(en_msg)):
        encry_msg += chr(en_msg[i])
    return encry_msg

def kiemTra(msg, y2):
    if(len(msg)!=len(y2)):
        print('No equal')
        return False
    y3=[]
    for i in range(0, len(y2)):
        y3.append(ord(y2[i]))
    isOk=True
    for i in range(0, len(y2)):
        check=((binhPhuongVaNhan(beta, y1, p))*(binhPhuongVaNhan(y1, y3[i], p)))%p
        if(check!=binhPhuongVaNhan(alpha, ord(msg[i]), p)):
            isOk=False
            break
    return isOk

def decrypt(en_msg):
    en_msg=en_msg.strip()
    dr_msg = []
    for i in range(0, len(en_msg)):
        dr_msg.append(ord(en_msg[i]))
    k=binhPhuongVaNhan(dr_msg[0], a, p)
    banRo=""
    for i in range(1, len(dr_msg), 2):
        c=chr((dr_msg[i]*ocolitMoRong(p, k))%p)
        banRo+=c
    return banRo

p =  random.randint(10000, 50000)
while(isPrime(p)==False):
    p = random.randint(10000, 50000)
alpha = random.randint(1, p-1)
a = random.randint(2, p-2)
beta = binhPhuongVaNhan(alpha, a, p)
k=random.randint(1, p-2)
while(gcd(k, p-1)!=1):
   k = random.randint(1, p - 2)
y1=0

def signFromInput():
    textOutputLeft.delete('1.0', 'end')
    x=encrypt(textInputLeft.get('1.0', 'end'))
    textOutputLeft.insert('1.0', x)
    if(decrypt(x)==textInputLeft.get('1.0', 'end')):
        print('YES')
    else:
        print('NO')

def handleChange():
    contentOfInputText=textInputLeft.get('1.0', 'end').strip()
    contentOfOutputText=textOutputLeft.get('1.0', 'end').strip()
    textInputLeft.delete('1.0', 'end')
    textOutputLeft.delete('1.0', 'end')
    checkInputFirst.delete('1.0', 'end')
    checkInputFirst.insert('1.0', contentOfInputText)
    fileTextInputSecond.delete('1.0', 'end')
    fileTextInputSecond.insert('1.0', contentOfOutputText)

def checkSignature():
    banRo=checkInputFirst.get('1.0', 'end').strip()
    banMa=fileTextInputSecond.get('1.0', 'end').strip()
    notifyOutput.delete('1.0', 'end')
    if(str(decrypt(banMa.strip()))==str(banRo)):
        notifyOutput.insert('1.0', 'Chữ ký Đúng!!!')
    else:
        notifyOutput.insert('1.0', 'Chữ ký Sai!!!')

root = tk.Tk()
root.iconbitmap('./icon.ico')
root.title('El Gammal')
root.geometry('700x500+50+50')


label=tk.Frame(root)
label.columnconfigure(0, weight=1)
label.columnconfigure(1, weight=1)
leftLabel=ttk.Label(label, text='Phát sinh chữ ký')
leftLabel.grid(row=0, column=0)
rightLabel=ttk.Label(label, text='Kiểm tra chữ ký')
rightLabel.grid(row=0, column=1)
label.pack(ipadx=20, pady=20 ,fill=tk.BOTH)
#define left side
leftSide=tk.Frame(root)
leftSide.columnconfigure(0, weight=1)
leftSide.columnconfigure(1, weight=1)
leftSide.columnconfigure(2, weight=1)
vanbanky=ttk.Label(leftSide, text='Văn bản ký:')
vanbanky.grid(row=0, column=0, sticky=tk.W)
textInputLeft=tk.Text(leftSide, height=7, width=50)
textInputLeft.grid(row=0, column=1, pady=30)
textInputLeft.insert('1.0', "Say o ha ra")
fileInput=tk.Button(leftSide, text='File', bg='blue', fg='white', width=15, height=3)
fileInput.grid(row=0, column=2)

signButton=tk.Button(leftSide, text='Ký', bg='blue', fg='white', width=15, height=3, command=signFromInput)
signButton.grid(row=1, column=1, pady=30)

signal=ttk.Label(leftSide, text='Chữ ký:')
signal.grid(row=2, column=0, sticky=tk.W)
textOutputLeft=tk.Text(leftSide, height=7, width=50)
textOutputLeft.grid(row=2, column=1)
textOutputLeft.insert('1.0', "Say o ha ra")
changeButton=tk.Button(leftSide, text='Chuyển', bg='blue', fg='white', width=15, height=3, command=handleChange)
changeButton.grid(row=2, column=2, sticky=tk.N)
saveButton=tk.Button(leftSide, text='Lưu', bg='blue', fg='white', width=15, height=3)
saveButton.grid(row=2, column=2, sticky=tk.S)
#define right side
rightSide=ttk.Frame(root)
rightSide.columnconfigure(0, weight=1)
rightSide.columnconfigure(1, weight=1)
rightSide.columnconfigure(2, weight=1)
vanbankyLabel=ttk.Label(rightSide, text='Văn bản ký:')
vanbankyLabel.grid(row=0, column=0, sticky='w')
checkInputFirst=tk.Text(rightSide, height=7, width=50)
checkInputFirst.grid(row=0, column=1, pady=30)
fileTextButton=tk.Button(rightSide, text='File văn bản', bg='blue', fg='white',width=15, height=3)
fileTextButton.grid(row=0, column=2)

checkSignalLabel=ttk.Label(rightSide, text='Chữ ký:')
checkSignalLabel.grid(row=1, column=0, sticky='w')
fileTextInputSecond=tk.Text(rightSide, height=7, width=50)
fileTextInputSecond.grid(row=1, column=1, pady=30)
fileSignalButton=tk.Button(rightSide, text='File chữ ký', bg='blue', fg='white',width=15, height=3)
fileSignalButton.grid(row=1, column=2)

checkSignal=tk.Button(rightSide, text='Kiểm tra chữ ký', bg='blue', fg='white',width=15, height=3, command=checkSignature)
checkSignal.grid(row=2, column=1, pady=30)

notifyLabel=ttk.Label(rightSide, text='Thông báo:')
notifyLabel.grid(row=3, column=0, sticky='w')
notifyOutput=tk.Text(rightSide, height=7, width=50)
notifyOutput.grid(row=3, column=1)

leftSide.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)
rightSide.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.RIGHT)



def main():
   # p =  random.randint(10000, 50000)#p 29
   # while(isPrime(p)==False):
   #     p = random.randint(10000, 50000)
   # alpha = random.randint(1, p-1)#alpha 7
   # a = gen_key(p)  #a
   # beta = binhPhuongVaNhan(alpha, a, p)  #beta
   # k=random.randint(1, p-2)
   # while(gcd(k, p-1)!=1):
   #     k = random.randint(1, p - 2)
   root.mainloop()

if __name__ == '__main__':
    main()