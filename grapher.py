import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load data from analysis.csv
print(os.getcwd())

df_analysis = pd.read_csv('./analysis.csv')

# Raw Sentiment between languages
# Raw sentiment based on party, spanish
groupES_R = df_analysis[(df_analysis['languages'] == 'es') & (df_analysis['Affiliation'] == 'R')]['ES_sentiment']
groupES_D = df_analysis[(df_analysis['languages'] == 'es') & (df_analysis['Affiliation'] == 'D')]['ES_sentiment']

# Raw Sentiment based on party, english
groupEN_R = df_analysis[(df_analysis['languages'] == 'en') & (df_analysis['Affiliation'] == 'R')]['EN_sentiment']
groupEN_D = df_analysis[(df_analysis['languages'] == 'en') & (df_analysis['Affiliation'] == 'D')]['EN_sentiment']






# Filter data for each group
groupA_ES_EN = df_analysis[(df_analysis['languages'] == 'es') & (df_analysis['Affiliation'] == 'R')]['sentimentDiff_EN-ES']
groupB_ES_EN = df_analysis[(df_analysis['languages'] == 'es') & (df_analysis['Affiliation'] == 'D')]['sentimentDiff_EN-ES']

groupA_EN_ES = df_analysis[(df_analysis['languages'] == 'en') & (df_analysis['Affiliation'] == 'R')]['sentimentDiff_ES-EN']
groupB_EN_ES = df_analysis[(df_analysis['languages'] == 'en') & (df_analysis['Affiliation'] == 'D')]['sentimentDiff_ES-EN']



# Plotting
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# Plotting raw sentiment based on party
sns.histplot(groupES_R, kde=True, color='blue', label = "Republican Sponsore Ads")
sns.histplot(groupES_D, kde=True, color='green', label = "Democrat Sponsored Ads")

plt.legend()
plt.title('Spanish Sentiment - Republicans vs Democrats')
plt.show()



sns.histplot(groupEN_R, kde=True, color='blue', label = "Republican Sponsore Ads")
sns.histplot(groupEN_D, kde=True, color='green', label = "Democrat Sponsored Ads")

plt.legend()
plt.title('English Sentiment - Republicans vs Democrats')
plt.show()




# ES-EN Shift - Republicans
sns.histplot(groupA_ES_EN, kde=True, color='blue', label = "Republican Sponsore Ads")
# ES-EN Shift - Democrats
sns.histplot(groupB_ES_EN, kde=True, color='green', label = "Democrat Sponsored Ads")

plt.legend()
plt.title('ES-EN Shift - Republicans vs Democrats')
plt.show()



# EN-ES Shift - Republicans
sns.histplot(groupA_EN_ES, kde=True, color='blue', label="Republican Sponsored Ads")
# EN-ES Shift - Democrats
sns.histplot(groupB_EN_ES, kde=True, color='green', label="Democrat Sponsored Ads")

plt.legend()
plt.title('EN-ES Shift - Republicans vs Democrats')
plt.show()


# plotting raw sentiments for spanish vs english ads (regardless of party)


