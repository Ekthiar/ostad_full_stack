#Student Grade Calculator

std_name = input("Student Name: ")

sub_1 = int(input("Enter Bangla marks: "))
sub_2 = int(input("Enter Math marks: "))
sub_3 = int(input("Enter English marks: "))
    
totl_markes = sub_1 + sub_2 + sub_3
avg_markes = totl_markes/3

if avg_markes >= 80:
    grad = "A+"
elif avg_markes >= 70:
    grad = "A"
elif avg_markes >= 60:
    grad = "B"
elif avg_markes >= 50:
    grad = "C"
else:
    grad = "F"

print(f"\nStudent Name: {std_name}")
print(f"Total Marks: {totl_markes}")
print(f"Average: {avg_markes:.2f}")
print(f"Grade: {grad}")