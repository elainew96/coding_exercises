'''
Exercise: the lion and the unicorn
Objective: use a generate-and-test pattern to write a loop with changing behavior.

Write a program that counts from 1 to 20 and along with each number prints “Lion” if the number is odd and prints “Unicorn” if the number 
is even. The first four lines of output should be:

1 Lion
2 Unicorn
3 Lion
4 Unicorn
'''
i = 1

while (i<=20):
  if (i%2==0):
    print(str(i) + " Unicorn")
  else:
    print(str(i) + " Lion")
  
  i += 1
