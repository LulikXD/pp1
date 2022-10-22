#9.	A user enters two integer numbers from the keyboard. Write a program
#  that checks if at least one of them is positive.

x = int(input("Pierwsza liczba:"))
y = int(input("Druga liczba:"))
if x >= 0 or y >= 0 :
    print ("Przynjamniej jedna liczba jest dodatnia.")
elif x < 0 and y < 0 :
    print ("Liczby są ujemne.")
else :
    print ("Liczby są dodatnie.")

