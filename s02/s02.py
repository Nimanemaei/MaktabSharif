# Question 1:
age1 = int(input("age of person1:"))
age2= int(input("age of person2:"))
age3= int(input("age of person3:"))
oldest_age = max(age1,age2,age3)
youngest_age = min(age1,age2,age3)
print("oldest age is:",oldest_age,"youngest age is:",youngest_age)

# Question 2:
# c to f
cel_temp = float(input('pleasse enter celsius temperature: '))
f_temp = (cel_temp * 1.8) + 32
print(f'temperature is {int(f_temp)} fahrenheit.')

# f to c

fah_temp = float(input('pleasse enter celsius temperature: '))
cel_temp = (fah_temp / 1.8) - 32
print(f'temperature is {cel_temp} fahrenheit.')

# Question 3:

str_1 = input('enter your first string: ')
str_2 = input('enter your seccond string: ')
print(str_2, str_1)

# Question 4:

num_1 = int(input('pleae enter first number: '))
num_2 = int(input('pleae enter seccond number: '))
sum_nums = num_1 + num_2
mult = num_1 * num_2
if mult >= 1000 :
    print(sum_nums)
else:
    print(mult)
