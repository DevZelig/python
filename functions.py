# # Write a function that takes two numbers – height and base of a triangle – as parameters and
# # returns the area of the triangle.
# # Formula for area of a triangle: A = 0.5*height*base\
# # def area_triangle(height, base):
# #     area = 0.5*height*base
# #     return area

# # a = area_triangle(6,9)
# # print(a)

# def get_factors(n):
#     factors = []
#     for i in range(1,n+1):
#         if n%i == 0:
#             factors.append(i)
#     return factors
# # n = 30572
# # f = get_factors(n) 
# # print(f)
# def check_prime(m):
#     f = get_factors(m)
#     if len(f) >2:
#         return False
#     else:
#         return True 
# m = 23
# p = check_prime(m)
# print(p)

def fact (num):
    f = 1
    for x in range(num):
        f = f*(x+1)
        
    return f

xyz = fact(5)

print(xyz)