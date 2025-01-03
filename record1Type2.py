current_year=int(input("Enter the current year:"))
final_year = int(input("Enter the final year: "))
if final_year < current_year:
    print("Final year must be greater than or equal to the current year")
else:
    print (f"Leap years from {current_year} to {final_year}")
for i in range(current_year, final_year + 1):
  if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
   print(i)
