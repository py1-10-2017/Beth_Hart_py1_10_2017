# class MathDojo():
#     def __init__(self):
#         self.result = 0
#     def add(self,num1,*num2):
#         self.result += num1
#         if num2:
#             for num in num2:
#                 self.result += num
#         return self
        
#     def subtract(self, num1, *num2):
#         self.result -= num1
#         if num2:
#             for num in num2:
#                 self.result -= num
#         return self
        
# md = MathDojo()
# print(md.add(2).add(3,4).subtract(10,5).result)

# class MathDojo():
#     def __init__(self):
#         self.result = 0
#     def add(self,num1,*num2):
#         if isinstance(num1, list):
#             for num in num1:
#                 self.result += num
#         else:
#             self.result += num1
#         if num2:
#             for num in num2:
#                 if isinstance (num, list):
#                     for i in num:
#                         self.result += i
#                 else:
#                     self.result += num
#         return self
        
#     def subtract(self, num1,*num2):
#         if isinstance(num1, list):
#             for num in num1:
#                 self.result -= num
#         else:
#             self.result -= num1
#         if num2:
#             for num in num2:
#                 if isinstance (num, list):
#                     for i in num:
#                         self.result -= i
#                 else:
#                     self.result -= num
#         return self
# inst = MathDojo()
# inst.add(1,2).add([3,4], 3,[5,5,5]).subtract([8],10)
# print(inst.result)


class MathDojo():
    def __init__(self):
        self.result = 0
    def add(self,num1,*num2):
        if isinstance(num1, list) or isinstance(num1, tuple):
            for num in num1:
                self.result += num
        else:
            self.result += num1
        if num2:
            for num in num2:
                if isinstance (num, list) or isinstance(num, tuple):
                    for i in num:
                        self.result += i
                else:
                    self.result += num
        return self
        
    def subtract(self, num1,*num2):
        if isinstance(num1, list) or isinstance(num1, tuple):
            for num in num1:
                self.result -= num
        else:
            self.result -= num1
        if num2:
            for num in num2:
                if isinstance (num, list) or isinstance(num, tuple):
                    for i in num:
                        self.result -= i
                else:
                    self.result -= num
        return self
inst = MathDojo()
inst.add(1,2).add([3,4], 3,(5,5,5)).subtract((8,10))
print(inst.result)