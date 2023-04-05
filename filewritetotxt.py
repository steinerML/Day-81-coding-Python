
import math

numb = int(input("Enter range: "))
 
with open("wortels.txt", "w") as f:
    for i in range(numb+1):
        print("Number:",i," √",math.sqrt(i)) #Preview result.
        f.write("\n" + "Number:"+str(i))
        f.write(" √")
        f.write(str(math.sqrt(i)))