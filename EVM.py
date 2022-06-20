count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
parties = {1: "YSRCP",
           2: "BJP",
           3: "TRS",
           4: "TDP",
           5: "Congress"}
i = 1
while (i != 0):
    vote = int(input("Enter the Party number:\t"))
    if vote == 1:
        print("\nYour vote for the YSRCP party has been registerd")
        count1 = count1 + 1
    elif vote == 2:
        print("\nYour vote for the BJP party has been registered")
        count2 += 1
    elif vote == 3:
        print("\nYour vote for the TRS party has been registered")
        count3 += 1
    elif vote == 4:
        print("\nYour vote for the TDP party has been registered")
        count4 += 1
    elif vote == 5:
        print("\nYour vote for the Congress party has been registered")
        count5 += 1
    i = int(input("\nEnter 0 if you want to stop the EVM and know the results(or else press 1)"))

print("\nThe total number of votes given are", count1 + count2 + count3 + count4 + count5, "\n")
print("Number of votes partywise are as follows\n")
print("\nYSRCP", count1, "\nBJP", count2, "\nTRS", count3, "\nTDP", count4, "\nCongress", count5)





