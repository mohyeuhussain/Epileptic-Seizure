points = 100
prize=None

if points<=50:
    prize="wooden rabbit"
elif 150<points<=180:
    prize="wafer-thin mint"
elif 181<points<=200:
    prize="penguin"

if prize:
    print("Congratulations! You won a {}".format(prize))
else:
    print("Oh dear you won nothin")