num1 = input ("Enter a number: ")
num2 = input ("Enter a second number: ")
print (num1, num2)
#while you can use a temporary variable to swap some variables around,
#it's not always necessary
num1, num2 = num2, num1
print (num1, num2)
#but sometimes, if you would need to trace back to old values anyway, it's not necessary