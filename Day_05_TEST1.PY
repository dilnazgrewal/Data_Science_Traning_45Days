# ans1 
print("------Answer 1------")
def student_marks(marks):
    total_marks = sum(marks)
    average_marks = total_marks/len(marks)
    count = 0
    for mark in marks:
        if mark >= 40:
            count += 1
    return total_marks, average_marks, max(marks), min(marks), count

marks = [78,45,32,91,67,39]
total_marks, average_marks, maximum, minimum, count = student_marks(marks)

print("Total Marks:", total_marks)
print("Average Marks:", round(average_marks,2))
print("Highest Marks:", maximum)
print("Lowest Marks:", minimum)
print("Passed Students:", count)

# ans2
print("\n------Answer 2------")
def discount_items(prices, discount = 10):
    total = sum(prices)
    discounted_amount = total - (total * (discount/100))
    discount_applied = discount
    if discounted_amount > 5000:
        discounted_amount = discounted_amount - (discounted_amount * (5/100))
        return total, discount_applied, "YES", discounted_amount
    return total, discount_applied, "NO", discounted_amount

prices = [1200, 800, 1500, 2500]
total, discount, extra, after_discount = discount_items(prices, 20)

print("Original Bill:", total)
print(f"Discount Applied: {discount}%")
print("Extra Discount:", extra)
print("Final Amount:", int(after_discount))

# ans3
print("\n------Answer 3------")
count = 0
def employee(**abc):
    for key,val in abc.items():
        global count 
        count += 1
        print(f"{key.capitalize()}: {val}")
    return "High Salary" if abc["salary"] > 50000 else "Normal Salary"
            
employee(name= "Rahul", age = 25, department ='IT', salary = 50000)
print("Total Entries:", count)

# ans4
print("\n------Answer 4------")
def integers(*args):
    div_list = []
    even_count = 0
    odd_count = 0
    for num in args:
        if num % 3 == 0 and num % 5 ==0:
            div_list.append(num)
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    total = sum(args)
    average = total/len(args)
    return total, average, max(args), min(args), even_count, odd_count, div_list

total, average, maximum, minimum, even_count, odd_count, div_list = integers(12,15,20,9,30,7,4)
print("Largest Numbers:", maximum)
print("Smallest Numbers:", minimum)
print("Even Numbers:", even_count)
print("Odd Numbers:", odd_count)
print("Sum:",total)
print("Average:",round(average,2))
print("Divisible by both 3 and 5:", div_list)
print("\n")