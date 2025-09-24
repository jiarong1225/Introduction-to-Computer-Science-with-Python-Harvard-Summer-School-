
def number_triangle(height):
     for i in range(height):
         print (height*100+(height-1)*2*i,end=" ")



rows=1
while rows<=9:
    number_triangle(rows)
    print("\n")
    rows+=1
