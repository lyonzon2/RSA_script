import random 
import os

class pgcd:
    def __init__(self,a,b,name):
        self.a = a 
        self.b = b 
        self.name = name 
    def calcul(self):
        while self.a != self.b :
            if self.a > self.b :
                 self.a = self.a - self.b 
            else :
                 self.b = self.b - self.a 
        return self.a
    
    def get_name(self):
        return self.name
    
def mod(a,b):
       
        if a > b :
            #THE RULE x mod b = n ==> x/b = c ==> c - int(c) without points * b 
            # example 15 mod 7 = 15/7 = 2.142 ==> 2.142 - 2 = 0.141 * 7 = 0.986 = 1 is n 
            # another rule a mod b ==> a/b = c ==> a - (c*b)
            #example 15 mod 7 ==> 15/7 = 2.142 ==> 15 - (2 * 7) = 1 is n 
            if a < 0 :
                while a < 0 :
                    a += abs(b)
                return a 
            else : 
                x = int((a//b))
                p = x * b
                modulo = a - p 
                return modulo
        if a < b :
            if a < 0 :
                while a < 0 :
                    a += abs(b)
                return a 
            if a > 0  : 
                return a 
        if a == b :
            return 0
        
        
def exp_mod(a,exp,b):
    a = int(a)**int(exp)
    result = mod(a,b)
    return result

def mod_inverse(x,y):
    for d in range(3,y):
            b = x * d 
            if mod(b,y) == 1 :
                return d
    raise ValueError('No inverse exists')
            
prime_numbers = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
    127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
    179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
    233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
    283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
    353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
    419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
    467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
    547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
    607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
    661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
    739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
    811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
    877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
    947, 953, 967, 971, 977, 983, 991, 997
]

if __name__ == "__main__":
    op=__file__.split("\\")
    ko = ""
    
    for i in op[1:-1] :
        ko+= str("\\")+str(i)
    

    print("select p and q  ...")
    path = r"c:"+ko+"\\"+"rsa_info.txt"
    p = random.choice(prime_numbers)
    q = random.choice(prime_numbers)
    file = open(path,"w")
    file.write(f"p = {p}, q = {q}")
    file.close()
    print(f"p = {p}, q = {q}")

    if (p == 0) or (q==0):
        print("Invalid Input")

    n = p * q 
    file = open(path,"a")
    print(f'n = {n}') 
    file.write(f'\nn = {n}')  
    Qn = (p -1) * (q - 1)
    file.write(f"\nQ(n) = {Qn}")
    print(f"Q(n) = {Qn}")

    for i in range(2,1000):
        b = pgcd(Qn,i,"calcul")
        if 1<=i<=Qn and b.calcul() == 1 :
            e = i 
            print("the variable e =",e)
            break
            
    file.write(f'\ne={e}')     
    print("Public key :",e,',',n)
    file.write(f"\nPublic key : [{e},{n}]")
    d = mod_inverse(e,Qn)
    print("the varibale d =",d)
    file.write(f"\nd={d}")
    print("Private key :",d,',',n)
    file.write(f"\nPrivat key : [{d},{n}]")
    file.close()
    print("Path of generated rsa infos in :","c:"+ko+"\\"+"rsa_info.txt")
    os.startfile(path)
    

