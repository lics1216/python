# L = [x*x for x in [1,2,3,4,5]]
# print(L)


# x = range(10)

# print(list(x))

# g = (x*x for x in [1,2,3,4,5,6])

# print(next(g))

# ####斐波那契数列输出前 n 项
# 数列： 1 1 2 3 5 8 13 21 34 
def lcs(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b  # a, a+b 先运行产生一个 tuple 元组 类型，复制给a, b
        n = n + 1
# #########  改成一个 generator

def lcs2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b  # a, a+b 先运行产生一个 tuple 元组 类型，复制给a, b
        n = n + 1       
    return "lcs2"    

# 这 迭代 无法获取 generator 的 return的值 

l = lcs2(9)

for x in l:
    print(x)

