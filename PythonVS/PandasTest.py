import pandas as pd
print(pd.__version__)

population_dict = {'California': 38332521,
'Texas': 26448193,
'New York': 19651127,
'Florida': 19552860,
'Illinois': 12882135}

population = pd.Series(population_dict)
population['California':'Florida']
print(population)

pd.DataFrame(population, columns=['SN','population'])
print(population)

data = pd.read_csv('RegularSeasonCompactResults.csv')
data.head()

