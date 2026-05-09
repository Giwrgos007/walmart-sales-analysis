import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Φόρτωση Excel
df = pd.read_excel('Filtered_Walmart_Sales_Data.xlsx', sheet_name='Data')
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Weekly_Sales')
plt.title('Εξέλιξη Εβδομαδιαίων Πωλήσεων στο Χρόνο')
plt.xlabel('Ημερομηνία')
plt.ylabel('Εβδομαδιαίες Πωλήσεις')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('images/sales_trend.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Sales_Category', y='Weekly_Sales', errorbar=None)
plt.title('Μέσες Εβδομαδιαίες Πωλήσεις ανά Κατηγορία')
plt.xlabel('Κατηγορία Πωλήσεων')
plt.ylabel('Μέσες Εβδομαδιαίες Πωλήσεις')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('images/sales_category.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Weekly_Sales', hue='Sales_Category', kde=True, element="step", stat="count")
plt.title('Κατανομή Εβδομαδιαίων Πωλήσεων ανά Κατηγορία')
plt.xlabel('Εβδομαδιαίες Πωλήσεις')
plt.ylabel('Συχνότητα (Πλήθος)')
plt.tight_layout()
plt.savefig('images/sales_distribution.png')
plt.show()