print("enter marks obtained in 4 subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
french = int(input("french :"))

sum =math+english+science+french
print("sum of math,english,science and french = ", sum)

perc = (sum/400)*100

print(end="percentage mark = ")
print(perc)

