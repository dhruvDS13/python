sub1 = int(input("Enter the marks of First subject:\n"))
sub2 = int(input("Enter the marks of Second subject:\n"))
sub3 = int(input("Enter the marks of Third subject:\n"))

if (sub1<33 or sub2<33 or sub3<33):
    print("You are Fail because you have less than 33% in one the subjects")

elif (sub1+sub2+sub3)/3 <40:
    print("You are fail due to total percentage is less than 40%")

else:
    print("Congratulation!!, You passed the exam.")