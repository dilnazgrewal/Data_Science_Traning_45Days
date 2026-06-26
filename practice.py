numbers = [1,2,3,4,5]

def square(x):
    return x ** 2

squared_numbers = list(map(square, numbers))
lambda_fuc1 = list(map(lambda x: x**3, numbers))
lambda_fuc2 = list(filter(lambda x: x%2==0, numbers))
print(squared_numbers)
print(lambda_fuc1)
print(lambda_fuc2)

