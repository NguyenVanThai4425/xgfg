print("Nguyen Van Thai","\nMSSV: 235752021610005")
n=input('Nhap vao danh sach: ')
n=n.replace(",","")
a=list(n)
for b in a :
    c=int(b)
    if c%2!=0:
        print(c,end=',')

