str = input()
new_str = ""
for alp in str:
    if ord(alp) >= ord('a'):
        new_str += alp.upper()
    else:
        new_str += alp.lower()
        
print(new_str)
    
