
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

#--- WRITE YOUR CODE FOR TASK 3 ---

# Group data in 'filtered_df' by 'customer_id'
grouped = filtered_df.groupby('customer_id')

# Find the earliest 'transaction_month_index' for each customer using 'min()'
earliest_cohort_month = grouped['transaction_month_index'].min()

# Create a new DataFrame named 'cohort_month' to store this information
cohort_month = earliest_cohort_month.reset_index()

# Rename the 'transaction_month_index' column to 'cohort_month' for clarity
cohort_month.rename(
    columns={'transaction_month_index': 'cohort_month'}, inplace=True)
# --- Inspect data ---
cohort_month

# ...WRITE YOUR CODE FOR TASK 4 ...
data = filtered_df.join(cohort_month.set_index(
    'customer_id'), on='customer_id')

# --- Inspect data ---
data


# --- WRITE YOUR CODE FOR TASK 5 ---
data['cohort_index'] = data['transaction_month_index'] - data['cohort_month']

# --- Inspect data ---
data

#--- WRITE YOUR CODE FOR TASK 6 ---
#Create 'df1' by selecting specific columns ('customer_id,' 'cohort_month,' and 'cohort_index') from the 'data'.
df1 = data[['customer_id', 'cohort_month', 'cohort_index']]

#In 'df1', remove duplicate rows based on 'customer_id,' 'cohort_month,' and 'cohort_index' columns using the 'drop_duplicates()' function. Keep only the first occurrence of each unique combination. Assign this filtered DataFrame to 'df2'.
df2 = df1.drop_duplicates(subset=['customer_id', 'cohort_month', 'cohort_index'])

#Generate 'final_df' by grouping the unique rows in 'df2' using the 'groupby()' function with columns 'cohort_month' and 'cohort_index.' Then, count the number of unique customers within each cohort group using the 'count()' function.
final_df = df2.groupby(['cohort_month', 'cohort_index']
                       ).agg({'customer_id': 'count'})

#Reset the index of 'final_df' using the 'reset_index()' function to ensure a structured format.
final_df = final_df.reset_index()

#Rename the 'customer_id' column in 'final_df' to 'customer_count' for clarity.
final_df.rename(columns={'customer_id': 'customer_count'}, inplace=True)
#---Inspect data---
final_df

# --- WRITE YOUR CODE FOR TASK 7 ---
cohort_data = final_df.pivot_table(
    index='cohort_month', columns='cohort_index', values='customer_count')

# ---Inspect data---
cohort_data



# Calculate 'cohort_percentage' by dividing each value by the values in the first column
cohort_percentage = cohort_data.divide(cohort_data.iloc[:, 0], axis=0)

# Round the resulting values to three decimal places and multiply by 100 to get percentages
cohort_percentage = cohort_percentage = (cohort_percentage.round(3)) * 100

# ---Inspect data---
cohort_percentage








