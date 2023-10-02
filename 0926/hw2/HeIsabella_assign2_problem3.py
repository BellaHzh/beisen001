number1 = int(input("Enter a number between 0 and 999: "))
number2 = int(input("Enter another number between 0 and 999: "))

reminder1_ones = number1 % 10
reminder1_tens = ((number1-reminder1_ones) % 100)/10
reminder1_hundreds = ((number1-reminder1_ones-10*reminder1_tens) % 1000)/100

reminder2_ones = number2 % 10
reminder2_tens = ((number2-reminder2_ones) % 100)/10
reminder2_hundreds = ((number2-reminder2_ones-10*reminder2_tens) % 1000)/100
ones_add = reminder1_ones+reminder2_ones
tens_add = reminder1_tens+reminder2_tens
hundreds_add = reminder1_hundreds+reminder2_hundreds
print("Sum of ones     = ", reminder1_ones, "+", reminder2_ones, "=", ones_add)
print("Sum of tens     = ", reminder1_tens, "+", reminder2_tens, "=", tens_add)
print("Sum of hundreds = ", reminder1_hundreds,
      "+", reminder2_hundreds, "=", hundreds_add)
