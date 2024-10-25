import time

blocks = int(input("Enter the number of blocks: "))

layer = 1
height = 0

while (blocks >= layer):

    blocks -= layer
    layer += 1
    height += 1
    
print("The height of the pyramid:", height)

time.sleep(2)
