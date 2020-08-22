def binary(number):
   result=[]
   a = number
   if a <= 0:
       return(str(a))
   if a == 1:
       return(str(a))
   elif a>0 and a != 1:
      while a>0:
         a = number//2
         modulo=number%2
         number = a
         result.append(str(modulo))
         if a<=0:
            g =list(reversed(result))
            myString = ''.join(g)
            return(myString)