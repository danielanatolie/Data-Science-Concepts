# Condtional Probability
# Data: People's purchases based on age
# 100,000 random individuals are produced and are  randomly 
# sorted to be in their 20s, 30s, 40s and so forth

random.seed(0)
#Total number of people in each age group
totals = (20:0, 30:0, 40:0, 50:0, 60:0, 70:0)

#Total number of things purchased in each age group
purchases = (20:0, 30:0, 40:0, 50:0, 60:0, 70:0)
totalPurchases = 0 
for _ in range(100000):
    ageDecade = random.choice([20,30,40,50,60,70])
    purchaseProbability = float(ageDecade) / 100.0 #This makes age and purchase depend, you can make it constant to make both independent of each other
    totals[ageDecade] += 1
    if (random.random() < purchaseProbability):
        totalPurchases += 1
        purchases[ageDecade] +=1

print totals
print purchases 

# Probability of purchasing given that you are in your 30s
PEF = float(purchases[30]) / float(totals[30])
print "P(purchase | 30s): ", PEF

# Probability of being 30:
PF = float(totals[30]) / 100000.0
print "P(30s): ", PF

# Probablity of buying someting:
PE float(totalPurchases) / 100000.0
print "P(Purchase):", PE

print "P(30's)P(Purchase)", PE * PF