#According to a study, the approximate level of intelligence of a person can be calculated using the following formula

# i = 2 + (y +0.5x)

#Write a program that will produce a table of values of i, y and x, where y varies from 1 to 6, and, for each value of y, x varies from 5.5 to 12.5 in steps of 0.5.

print("y      x         i")

print("----------------------")

for y in range(1,7):
    x=5.5
    while x<=12.5:
        i=2+(y+ 0.5 *x)

        #print(f"{y}    {x:.1f}      {i:2f}")
        print(y,"    ",x ,"    ",    i)


        x+=0.5


