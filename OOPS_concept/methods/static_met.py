class Myclass:
    @staticmethod
    def mul(a,b):
        print(a*b)
    @staticmethod
    def is_even(number):
        if number%2==0:
            print("even number")
        else:
            print("odd number")

Myclass.mul(2,5)
Myclass.is_even(5)


# class Add_Mul:
#     @staticmethod
#     def add_numbers(a, b):
#         return a + b
#
#     @staticmethod
#     def multiply_numbers(a, b):
#         return a * b
#
#
# # Calling the static methods
# result1 = Add_Mul.add_numbers(5, 3)
# print("Result of adding numbers:", result1)
#
# result2 = Add_Mul.multiply_numbers(5, 3)
# print("Result of multiplying numbers:", result2)