#تابع بنویسید که 100 عدد دریافت کند و خروجی بزرگترین باشد
def max100():
    a=input() 
    a=int(a) 
    max=a
    for i in rang (0,100):
        a=int (input()) 
        if a>max:
             max=a
        return max