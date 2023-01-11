def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=len(data)
    return a 
encoding='UTF-8'
f=open('txt_file/data02.txt')
data=f.read() 
print(main(data))

# Read data from file