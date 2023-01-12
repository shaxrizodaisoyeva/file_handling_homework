def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    list=[]
    c=0
    data=[data.rstrip() for data in data]
    for c in data:
        list.append(len(c))
        d=max(list)
    return int(d)
encoding='UTF-8'
f=open('txt_file/data10.txt')
data=f.readlines()
print(main(data))
# Read data from file