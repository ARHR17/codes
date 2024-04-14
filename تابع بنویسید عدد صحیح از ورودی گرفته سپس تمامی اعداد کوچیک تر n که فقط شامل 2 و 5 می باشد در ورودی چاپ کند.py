#تابع بنویسید عدد صحیح از ورودی گرفته سپس تمامی اعداد کوچیک تر n که فقط شامل 2 و 5 می باشد در ورودی چاپ کند

def shamel2v5(L):
    while L!=0:
        k=L%10
        if k!=2 and k!=5:
          return False
        L//=10
    return True
def function2(n):
    for i in range(n):
      K = shamel2v5(i) 
      if K:
       Print(i)