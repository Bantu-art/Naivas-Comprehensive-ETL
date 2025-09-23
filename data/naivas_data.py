import pandas as pd
import random
from datetime import datetime, timedelta
import boto3

# Branches of Naivas
branches = [
    "Naivas Nairobi CBD", "Naivas Westlands", "Naivas Thika Road", "Naivas Kisumu",
    "Naivas Eldoret", "Naivas Nakuru", "Naivas Mombasa", "Naivas Machakos",
    "Naivas Kitale", "Naivas Nyeri", "Naivas Nairobi CBD", "naivas nairobi cbd", "nairobi cbd", "CBD", "  naivas cbd ",
    "nairob cbd", "NAIVAS NAIROBI CENTRAL", "naivas kisumu", "kisumu", "Naivas Kisum", "KSM",  
    "naivas-kisumu",
]

# Categories with foodstuff dominating
categories = {
    "Foodstuff": ["Maize Flour 2kg", "Bread", "Milk 1L", "Rice 5kg", "Sugar 2kg", "Cooking Oil 1L", "Eggs Tray", "Vegetables", "Fruits"],
    "Electronics": ["Headphones", "Smartphone", "Laptop", "Charger", "Television"],
    "Liquor": ["Beer 500ml", "Whiskey 750ml", "Wine 1L", "Vodka 500ml"],
    "Baby Products": ["Diapers", "Baby Oil", "Baby Food", "Baby Wipes"],
    "Household": ["Detergent", "Toilet Paper", "Broom", "Mop", "Dish Soap"]
}

# Generate synthetic dataset (30,000 rows)
data = []
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)
date_range = (end_date - start_date).days

for i in range(30000):  
    date = start_date + timedelta(days=random.randint(0, date_range))
    branch = random.choice(branches)
    category = random.choices(list(categories.keys()), weights=[0.5, 0.15, 0.1, 0.1, 0.15])[0]  # Foodstuff dominates
    product_name = random.choice(categories[category])
    product_id = f"P{random.randint(1,200):03d}"
    quantity = random.randint(1, 5)
    unit_price = random.randint(100, 25000) if category != "Foodstuff" else random.randint(50, 1000)
    total_amount = quantity * unit_price
    customer_id = random.choice([f"CUST{random.randint(1000,9999)}", "ANON"])
    
    data.append([date.date(), branch, product_id, product_name, quantity, unit_price, total_amount, customer_id])

# Create DataFrame
full_df = pd.DataFrame(data, columns=[
    "date", "branch", "product_id", "product_name", "quantity", "unit_price", "total_amount", "customer_id"
])

# Replace ANON customer IDs with Guest
full_df['customer_id'] = full_df['customer_id'].replace('ANON', 'Guest')

full_df.to_csv("raw_data.csv", index=False)
print(f"Transformed data saved to raw_data.csv")

# # Upload to S3 with partitioned structure
# current_date = datetime.now()
# year = current_date.year
# month = f"{current_date.month:02d}"

# s3_key = f"raw/year={year}/month={month}/naivas_sales_{current_date.strftime('%B').lower()}.csv"
# bucket_name = "naivas-raw-data-bbantu-2025"

# # Convert to CSV in memory
# csv_buffer = full_df.to_csv(index=False)

# # Upload to S3
# s3_client = boto3.client('s3')
# s3_client.put_object(
#     Bucket=bucket_name,
#     Key=s3_key,
#     Body=csv_buffer
# )

# print(f"✅ Dataset uploaded to s3://{bucket_name}/{s3_key} with 30,000 rows")
