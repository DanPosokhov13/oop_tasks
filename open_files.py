""" with open('read.txt') as f:
    data = f.read()
    print(data)
 """
""" with open('read.txt', 'w') as f:
    f.write('\nBonjour')  """
    
with open('read.txt') as f:
    data = f.readlines()
    print(data)

