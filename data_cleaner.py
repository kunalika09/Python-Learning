#OUTLIER & MISSING DATA CLEANER (ML SIMULATION)
#Simulating data cleaning pre processing for Machine Learning
raw_dataset = [45, 82, -10, "missing", 91, 105, "error", 73, -5, 88]

clean_dataset = []
removed_count = 0

print("Raw Dataset:", raw_dataset)

#Data cleaning loop
for data in raw_dataset:
    #Check if the data point is a valid positive number under a threshold
    if isinstance(data, int) and 0 <= data <= 100:
        clean_dataset.append(data)
    else:
        removed_count += 1

print("\n--- Cleaning Complete ---")
print("Cleaned Dataset (Only valid scores 0-100):", clean_dataset)
print("Total anomalies/noise removed:", removed_count)
