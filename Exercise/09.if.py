# -*- encoding : utf-8 -*-

# age = 10

# age = input('请输入您的年龄...') # input输入获取后的值为str

# age = int(age)

# # print(type(age))
# if age>18:
#     print('成年了哦~')
# else:
#     print('我是未成年小朋友')


# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：

print('小明身高1.75，体重80.5kg')

bmi = 80.5/(1.75*1.75)

print('经过计算得到BMI为%.1f,体态属于' % bmi)

if bmi < 18.5:
    print('过轻')
elif bmi >= 18.5 and bmi < 25:
    print('正常')
elif bmi >= 25 and bmi < 28:
    print('过重')
elif bmi >= 28 and bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
