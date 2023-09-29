
# --- WRITE YOUR CODE FOR MODULE 2 TASK 1 ---

approved_df = df[df['order_status']=="Approved"]
approved_df

#--- Inspect data ---

# Import the 'datetime' class from the 'datetime' module.
from datetime import datetime
# --- WRITE YOUR CODE FOR TASK 2 ---

# Create a new dataframe called 'filtered_df' by selecting only the 'customer_id' and 'transaction_date' columns from the 'approved_df.'
filtered_df = approved_df[['customer_id', 'transaction_date']].copy()

# Convert the 'transaction_date' column to datetime using 'pd.to_datetime()'.
filtered_df['transaction_date'] = pd.to_datetime(
    filtered_df['transaction_date'])

# Create a new 'YM' column in a DataFrame with a lambda function to represent the year and month in the "%Y%m" format, and ensure the datatype of the 'YM' column is integer.
filtered_df['YM'] = filtered_df['transaction_date'].apply(
    lambda x: int(x.strftime("%Y%m")))

# Determine the start month using the 'min()' function on the 'YM' column.
start_month = filtered_df['YM'].min()

# Calculate a new column 'transaction_month_index' by subtracting the start month value from each 'YM'.
filtered_df['transaction_month_index'] = filtered_df['YM'] - start_month

# --- Inspect data ---
filtered_df

