import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

df = pd.read_csv(r"C:\Users\hp\OneDrive - Higher Education Commission\Desktop\DA\project2\customer_shopping_behavior_cleaned.csv")

print(f"Shape: {df.shape}")

password = quote_plus("Nom@n199")
engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/DAdb")

# ✅ Use explicit connection with context manager
with engine.begin() as conn:       # begin() auto-commits on success, rolls back on error
    df.to_sql("shopping_behavior", con=conn, if_exists="replace", index=False)
    print("Data uploaded successfully!")

    # Verify immediately inside same connection
    result = conn.execute(text("SELECT COUNT(*) as total FROM shopping_behavior"))
    print(f"Rows in MySQL: {result.fetchone()[0]}")

#df = pd.read_csv("customer_shopping_behavior.csv")
# Display the first few rows of the dataset
#print (df.head())

#df.info()

#print (df.describe(include='all'))

#print (df.isnull().sum())

# df["Review Rating"]= df.groupby("Category")["Review Rating"].transform(lambda x: x.fillna(x.mean()  ))
# #print (df.isnull().sum())

# df.columns= df.columns.str.strip().str.lower().str.replace(" ","_")
# df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'}, inplace=True)
#print (df.columns)

#feature engineering: creating age groups

# label= ['Young Adults', 'Adults', 'Middle-aged', 'Seniors']
# df['age_group']= pd.qcut(df['age'], q=4, labels=label)

#print (df[["age", "age_group"]].head(10))

#feature engineering: creating purchase frequency days
# frequency_mapping = {
#     'Daily': 1,
#     'Weekly': 7,
#     'Fortnightly': 14,
#     'Monthly': 30,
#     'Quarterly': 90,
#     'Annually': 365,
#  }
# df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
#print (df[["frequency_of_purchases", "purchase_frequency_days"]].head(10))

#print (df[['discount_applied', 'promo_code_used']].head(10))

#print((df['promo_code_used'] == df['discount_applied']).all()) 
# df.drop(columns=['promo_code_used'], axis=1, inplace=True)
# print (df.columns)

# df.to_csv("customer_shopping_behavior_cleaned.csv", index=False)