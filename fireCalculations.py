import pandas as pd
import numpy as py
import matplotlib.pyplot as plt

# Initial Variables
# Ages
currentAge = 30
retirementAge = 45
# workPensionAge = 58
# statePensionAge = 68
endAge = 67

# Money Values
preTaxSalary = 100000
postTaxSalary = 80000
currentAnnualSpending = 40000
retirementAnnualSpending = 40000
currentNetWorth = 100000
pensionContribution = 0

# Allocation
allocationType = {
    "stocks": {"allocationPct": 0.9, "return": 0.08},
    "bonds": {"allocationPct": 0, "return": 0},
    "cash": {"allocationPct": 0.1, "return": 0.005},
    "others": {"allocationPct": 0, "return": 0},
}

# rates
safeWithdrawRate = 0.04
inflationRate = 0.03
incomeGrowthRate = 0.03


fireNumber = retirementAnnualSpending / safeWithdrawRate


def getWeightedRates(allocations: dict) -> int:
    weightedRate = 0
    for key, value in allocations.items():
        weightedRate += value["allocationPct"] * value["return"]
    return weightedRate


weightedRate = getWeightedRates(allocationType) - inflationRate


def getNetWorthWithIncome(prevNetWorth, rate, takeHome, spending, pension):
    return prevNetWorth * (1 + rate) + (takeHome - spending) + (pension)


def getNetWorthNoIncome(prevNetWorth, rate, retirementAnnualSpending):
    return prevNetWorth * (1 + rate) - retirementAnnualSpending


netWorth = [0] * ((endAge - currentAge) + 1)
# initial Year0
netWorth[0] = currentNetWorth
for i in range(1, len(netWorth)):
    if i <= 15:
        netWorth[i] = round(
            getNetWorthWithIncome(
                netWorth[i - 1],
                weightedRate,
                postTaxSalary,
                currentAnnualSpending,
                pensionContribution,
            )
        )
    else:
        netWorth[i] = round(
            getNetWorthNoIncome(netWorth[i - 1], weightedRate, retirementAnnualSpending)
        )

# plot
xaxis = list(range(currentAge, endAge + 1))
yaxis = netWorth

# Fire Line
plt.axhline(y=fireNumber, color="r", linestyle="-")

plt.plot(xaxis, yaxis)
plt.show()
# Make sure to close the plt object once done
plt.close()
