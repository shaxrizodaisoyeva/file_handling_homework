def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=data.split(",")
    b=[]
    c=0
    while c<len(data):
        if data[c].isdigit():
            b+=data[c]
            d=min(b)
        c+=1
    return int(d)
encoding='UTF-8'
f=open('txt_file/data09.txt')
data=f.read() 
print(main(data))
# Read data from file