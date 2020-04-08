# 验证码

import random


class Yanzheng(object):

    def __init__(self,n, alpha):
        self.n = n
        self.alpha = alpha

    def code(self):
        s = ''  # 创建字符串变量,存储生成的验证码
        for i in range(self.n):  # 通过for循环控制验证码位数
            num = random.randint(0, 9)  # 生成随机数字0-9
            if self.alpha:  # 需要字母验证码,不用传参,如果不需要字母的,关键字alpha=False
                upper_alpha = chr(random.randint(65, 90))
                lower_alpha = chr(random.randint(97, 122))
                # 从列表中 [], 返回一个随机元素
                num = random.choice([num, upper_alpha, lower_alpha])
            s = s + str(num)
        print(s)
        return s

if __name__ == "__main__":
    yanzhengma = Yanzheng(6,False)
    yanzhengma.code()
