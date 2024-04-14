#تابع بنویسید که عدد n از ورودی گرفته کوچیک ترین عددی که مجموع ارقامش برابر n است را به خروجی تابع ارسال کنید
def majmoe(t):
    ssum = 0 
    while t!= 0:
        ssum += t%10
        t //= 10
    return ssum
def function1(n):
    for i in range(n):
      K = majmoe(i) 
      if K == n:
       return K
    return print('not found')