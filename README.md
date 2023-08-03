# Python_Project_Banking_System
This is a simple python project on Banking System created as a part of my course Data Science and Machine Learning by Entri Elevate.


# Introduction
This project replicates a banking system with basic features that help users to perform action related to their bank accounts>
If the user already has a bank account then he/she can perform the following activities: DEPOSIT MONEY,WITHDRAW MONEY,CHECK ACCOUNT BALANCE,
CHECK NUMBER OF TRANSACTIONS,ACCOUNT HOLDER DETAILS.
For new user ,they can create a new account by giving the following details: NAME ,AGE ,PLACE and PASSWORD.
After the account is succesfully completed they can perform the banking activities.

# Features Used
 
We have made use of the Python functions ,list, iterative statements as well as datetime module to do necessary activities.

# Working

#(1) The details such as username,password,place age,year of account opening,balance,transactions made are all given as seperate list.

#(2) In the beginning of the program excecution we call the userdefined function start() and it prints a welcome message.

#(3) Next the Function login() is called.This allows the user to choose from 3 different options either to login to an already existing        account or to create a new account or to exit .

  If the user choose account login then the program ask the user to input their username and password.
  After that using iterative statements are used to check if the username/password exist in the given list .If so ,it check if the index    of the username and password in the respective list matches or not. If it matches, Log in is succesful and the services offered are 
  show on screen defined by function services(), if not ,it show an error message .
  
  If the user choose new account creation then they have to enter their name ,age,place,password.These values then gets appended to the     corresponding list.The year of opening account is found by importing datetime module and using date() and today() and gets appendend to   the list that corresponds to year.Now account balance and number of transactions are set to zero.Thus the account is created .
  
  If the user choose exit option then the text "Thank you vist again " message is printed

#(4) When the login is successful, services() is excecuted.
    In this program the banking system offers the following services:

  a) Deposit money : If the user choose this option then the Depositmoney() function is called and excecuted
     In Depositmoney() the amount to be deposited is asked from user .If the money is less than 100 it shows an error else deposited 
     money gets added to the corresponding balance and the number of transactions is updated.Now we can again choose wheteher to take any 
    other service or to exit
 
 b) Withdraw money : If the user choose this option then the Withdrawmoney() function is called and excecuted
    In Withdrawmoney() the amount to be withdrawn is asked from user .If the money is greater than the account balance it shows an error 
    else withdrawn money gets subtracted from the corresponding balance and the number of transactions is updated.Now we can again choose 
    wheteher to take any other service or to exit
 
 c) Number of transcations : If the user choose this option then the nooftranscations() is excecuted and it prints the result
    Now again the user can choose whether to take any other service or to exit
 
 d) Check account balance :if the user choose this option then Checkaccountbalance() is excecuted and the result is printed
    Now again the user can  choose whteher to take any other service or to exit
 
 e) Account holder details:If the user choose this  it prints the necessary details of account holder
    Now again the user can  choose whteher to take any other service or to exit
  
 















