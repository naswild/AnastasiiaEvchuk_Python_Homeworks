class Calculator:

    def sum(self, a, b):
        result = a + b
        return result

    def sub(self, a,b):
        result = a - b
        return result

    def mul(self, a,b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ArithmeticError('На ноль делить нельзя')
        return a / b

    def pow(self, a, b = 2):
        return a ** b

    def avg(self, nums):
        len_of_nums = len(nums)
        if len_of_nums == 0:
            return 0

        s = 0
        for num in nums:
            s = self.sum(s, num)

        return self.div(s, len_of_nums)