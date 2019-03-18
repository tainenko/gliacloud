'''
Integration

https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Integral_approximations-3-steps.png/320px-Integral_approximations-3-steps.png
Please try to add 1~3 line of code to finish the integration
def anonymous(x):
return x**2 + 1
def integrate(fun, start, end):
step = 0.1
intercept = start
area = 0
while intercept < end:
intercept += step
your work here
return area
print(integrate(anonymous, 0, 10))
'''

def anonymous(x):
    return x**2 + 1

def integrate(fun, start, end):
    step = 0.1
    intercept = start
    area = 0
    while intercept < end:
        intercept += step
        #your work here
        #把曲線面積視為長方形，高為fun(x)，寬為step，area=sum(所有長方形面積)
        #當step越小時，得到的結果越精確。
        area+=fun(intercept)*step
    return area

if __name__=='__main__':
    print(integrate(anonymous, 0, 10))