print("Hello World")


def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  


def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
print(remove_duplicates(["apple", "banana", "apple", "orange"])) 






a=list(map(int,input().split()))
t=int(input())
def two_sum(nums,target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum(a,t))
   


num1 = 9087904750397309573
num2 = 98989080898009808
print(num1 + num2)


def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0

    for c in s[::-1]:
        curr = roman[c]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
    return total

print(roman_to_int("X"))  
