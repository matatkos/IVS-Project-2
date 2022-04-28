import mathlib as mt
import sys
i = 0
#while arr[i] != "":
arr = sys.stdin.read().split()
    #i+=1


#average - X'
suma_x = 0
N = int(len(arr))
for i in range(N):
    arr[i] = float(arr[i])
    suma_x = float(mt.add(suma_x, arr[i]))


X_avg = suma_x / N
#1/(N-1)
calc1 = mt.sub(N,1)
calc2 = mt.div(1, calc1)


#N * (X_avg**2)
calc3 = mt.pow(X_avg,2)
calc4 = float(mt.mul(N,calc3))

#suma_x ** 2
calc5 = mt.pow(suma_x,2)

#(suma_x ** 2) - (N * (X_avg**2))
calc6 = mt.sub(calc5, calc4)

#
calc7 = mt.mul(calc2, calc6)

#s
s = mt.root(calc7,2)
print(s)
'''
print("s:", s)
print("N:", N)
print("suma_X:", suma_x)
print("avg_x:", X_avg)
'''








