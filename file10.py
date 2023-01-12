def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    b=[]
    a=0
    for a in data:
        b.append(len(a))
        d=max(b)
    return int(d)
encoding='UTF-8'
f=open('txt_file/data10.txt')
data=f.read().split("\n")
print(main(data))
# Read data from file