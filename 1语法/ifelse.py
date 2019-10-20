# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：

# -*- coding: utf-8 -*-

# height = 1.75
# weight = 80.5


print("请输入身高，单位是m")
height = input()
print("请输入体重，单位是Kg")
weight = input()

# input  返回的是字符串 要转换
height = float(height)
weight = float(weight)

a = weight / (height * height)

if a <= 18.5 :
	print("thin")
elif 18.5 < a and a < 25:   # 为什么用 & ,  但 and 可以
	print("normal")
elif 25 < a and a < 28:
    print("fat")
elif 28 < a and a <32:
    print("too fat")
else :   #注意：else 后面的没有判断条件
	print("fat serious")
