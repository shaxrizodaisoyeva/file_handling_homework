def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=data.split(",")
    c=0
    sum=0
    while c<len(data):
        if data[c].isdigit():
            sum+=int(data[c])
        c+=1
    return sum
encoding='UTF-8'
f=open('txt_file/data07.txt')
data=f.read() 
print(main(data))
# Read data from file