print("Nguyen Van Thai","\nMSSV: 235752021610005")
def file_read_from_head(fname,nline):
    from itertools import islice
    with open (fname) as f:
        for line in islice(f,nline):
            print(line)
file_read_from_head('vd.txt',2)
