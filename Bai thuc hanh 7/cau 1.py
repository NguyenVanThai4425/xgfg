print("Nguyen Van Thai","\nMSSV: 235752021610005")
input_file = open('vd.txt','r')
for line in input_file:
    l=len(line)
    s=' '
    while (l>=1):
        s=s+line[l-1]
        l=l-1
    print(s)
input_file.close()
