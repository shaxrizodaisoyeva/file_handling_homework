def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=data.split(",")
    b=[]
    c=0
    while c<len(data):
        if data[c].isdigit()==False:
            b+=data[c]
        c+=1
    return b
encoding='UTF-8'
f=open('txt_file/data04.txt')
data=f.read() 
print(main(data))
# Read data from file