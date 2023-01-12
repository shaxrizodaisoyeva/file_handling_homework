def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    encoding='UTF-8'
    f=open('txt_file/data10.txt')
    data=f.read().split("\n")
    b=[]
    a=0
    for a in data:
        b.append(len(a))
        d=max(b)
    return int(d)
a='txt_file/data10.txt'
print(main(a))
# Read data from file