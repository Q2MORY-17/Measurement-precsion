import math
import time
import colorama
from colorama import Fore,Back,Style
colorama.init()

x=int(input("\nHow many readings have you taken: "))
k=[0, 0, 12.71, 4.3, 3.18, 2.78, 2.57, 2.45, 2.37, 2.31]
df=x-1
z=[]
s=[]
R=100           #Don't forget to change these values if needed
DR=0.5          #Don't forget to change these values if needed
g=3.85e-3       #Don't forget to change these values if needed        
Dg=0.01e-3      #Don't forget to change these values if needed

for y in range(0, x):
    print("#",y+1)
    i=float(input("Reading please: "))
    z.append(i)
print("\nreadings: ",z)

X=sum(z)/x
print("estimated value: X = %.3f"%X)

for y in range(0, x):
    a=(z[y]-X)**2
    s.append(a)
S=math.sqrt(sum(s)/df)
print("estimated standard deviation: S = %.3f"%S,"\n")

Ua=S/math.sqrt(x)
print("Ua = %.4f"%Ua)

Dr=0.002/100*X+0.0005/100*1000
Ub=Dr/math.sqrt(3)
print("Ub = %.4f"%Ub)

Ur=math.sqrt(Ua**2+Ub**2)
print("Ur = %.4f"%Ur,"\n")

A=X-k[df]*Ua
B=X+k[df]*Ua
print(Fore.GREEN+"95% confidence interval: ",A,", ",B)

T=(X/R-1)*1/g
UR=DR/math.sqrt(3)
Ug=Dg/math.sqrt(3)
Cr=1/(R*g)
CR=-X/(g*R**2)
Cg=(X/R-1)*(-1/g**2)
Dt=math.sqrt((Cr*Ur)**2+(CR*UR)**2+(Cg*Ug)**2)
print(Fore.GREEN+Style.BRIGHT+"TOTAL TEMPERATURE: %.3f"%T," +/- %.3f"%Dt,"\n")
