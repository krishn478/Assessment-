a = input("movie name:")
b = int(input("Adult Ticket Price:"))
c = int(input("Child Ticket Price:"))
d = int(input("No of Adult Tickets Sold:"))
e = int(input("No of Child Tickets Sold:"))
f = int(input("percentage of gross amount donated:"))
k = b*d+c*e
print("Gross amount:", k)
h = k*f/100
print("amount donated to charity:", h)
s = k-h
print("Net sale amount:", s)
