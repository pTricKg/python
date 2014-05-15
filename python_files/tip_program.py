# What should I tip

# calculate 15% and 20% tip

user = input("How much is your bill?")

tip_okay = float(user) * 0.15
tip_good = float(user) * 0.20

round_okay = round(tip_okay,2)
round_good = round(tip_good,2)

print("If you'd like to tip well, then give ", round_good,\
      "or if your money is tight, give " , round_okay)
