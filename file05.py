def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=data.split(",")
    b=[]
    c=0
    d=0
    while c<len(data):
        if data[c].isdigit():
            d+=1
        c+=1
    f=len(data)-d
    b.append(d) 
    b.append(f)
    return b
encoding='UTF-8'
f=open('txt_file/data05.txt')
data=f.read() 
print(main(data))
# Read data from file