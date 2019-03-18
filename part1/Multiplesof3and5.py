'''
Multiples of 3 and 5.
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
• Find the sum of all the multiples of 3 or 5 below 1000.
'''

def get_multi_3(n):
    '''
    :param n:
    :return int:
    '''
    sum=0
    for num in range(n):
        if not num%3:
            sum+=num
    return sum

def get_multi_5(n):
    '''
    :param n:
    :return int:
    '''
    sum = 0
    for num in range(n):
        if not num % 5:
            sum += num
    return sum

def get_multi_15(n):
    '''
    :param n:
    :return int:
    '''
    sum = 0
    for num in range(n):
        if not num % 15:
            sum += num
    return sum

def get_multi_3_and_5(n):
    '''
    15是3和5的最小公倍數
    欲求得不大於自然數n的3,5倍數總和
    等於求3的倍數總和+5的倍數總和-15的倍數總和
    :param n:
    :return int:
    '''
    return get_multi_3(n)+get_multi_5(n)-get_multi_15(n)

if __name__=='__main__':
    print(get_multi_3_and_5(1000))