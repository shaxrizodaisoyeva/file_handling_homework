def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=data.split(",")
    b=[]
    c=0
    for c in a:
        d = int(c)
        b.append(d)
    return b
encoding='UTF-8'
f=open('txt_file/data01.txt')
data=f.read() 
print(main(data))

# Read data from file