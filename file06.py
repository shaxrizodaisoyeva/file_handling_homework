def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    b=[]
    c=0
    data=[data.rstrip() for data in data]
    for c in data:
        b.append(len(c))
    return list(b)
encoding='UTF-8'
f=open('txt_file/data06.txt')
data=f.readlines()
print(main(data))
# Read data from file