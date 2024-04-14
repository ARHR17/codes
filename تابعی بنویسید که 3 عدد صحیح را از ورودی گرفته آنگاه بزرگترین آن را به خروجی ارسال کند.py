#تابع بنویسید که 3 عدد صحیح را از ورودی گرفته آنگاه بزرگترین آن را به خروجی ارسال کند :
def max3 (a,b,c) :
    max=a
    if b>max:
       max=b
    if c>max:
       max=c
    return max