# Step 3. write the logic
age = int(input("Enter the age\n").strip())

if age <= 0 or age > 130:
    print("Enter a valid age")
else:
    if age >= 21:
     print("Yes, can go club")
    else:
      print("No, can't go club")
