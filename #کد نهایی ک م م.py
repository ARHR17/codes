#کد نهایی ک م م
def lcm(x, y):
   if x > y:
       lcm_ = x
   else:
       lcm_ = y

   while(True):
       if((lcm_ % x == 0) and (lcm_ % y == 0)):
           break
       lcm_ += 1

   return lcm_


num1 = int(input())
num2 = int(input())
print("lcm: ", lcm(num1, num2))