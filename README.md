# Villain Password Generator
This is my first python project ever, don't hesitate to reach out if you have any advice.

The aim of the program is to generate passwords using the name of a famous villain and a random set of caracters (uppercase, lowercase, numbers and special caracters).
The program first asks the user for the length of the password, then after input filters out the villaion names that are greater than that length before returning a generated password consisting of a villain name followed by an hyphen and random caracters. 

Here are examples of how the program works :

### The user's input allows for a password to be generated:

> Enter the desired length of the password (min. 7 caracters): 17
> 
> Your new password is: Sauron-#+UL8LKLSO

In that case, the user input a number greater than the minimum length (which by default is 7), a password can be generated.

### The user's input is below the required minimum of caracters to generate a password:

> Enter the desired length of the password (min. 7 caracters): 3
>
> Invalid input. Your password must be at least 7 characters long.

> Enter the desired length of the password (min. 7 caracters):

In that case, the required password is smaller than the minimum length (which by default is 7). The program will ask the user again.

### The user's input is greater than the required minimum but doesn't allow for a suitable villain's name length to be found:

> Enter the desired length of the password (min. 2 caracters): 3
> 
> No villain names are suitable for the given password length.

> Enter the desired length of the password (min. 2 caracters): 

In that case the minimum length has been changed to 2 for demonstration purposes. The user input is greater than the required length, however no villain name is suitable for the password to be generated (along with an hyphen and at least 1 character). Since in that sample's list the smallest villain name is Scar (4 characters), the program will only allow the user to ask for a 6 characters password (Scar + hyphen + at least 1 character).
Here is what the result would be :

> Enter the desired length of the password (min. 2 caracters): 6
>
> Your new password is: Scar-9


### The user doesn't input a valid number :

> Enter the desired length of the password (min. 7 caracters): 14,5
> 
> Invalid input. Please enter a valid number.
>
> Enter the desired length of the password (min. 7 caracters): abc
>
> Invalid input. Please enter a valid number.
>
> Enter the desired length of the password (min. 7 caracters):

The program only accepts whole numbers. The user is asked to enter a number again until a valid number is entered.


