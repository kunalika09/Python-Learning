#STUDENT GRADE ANALYZER & PERFORMANCE ANALYZER
#A project to analyze a adataset ofstudent test scores
print("--- STUDENT DATA ANALYZER ---")

scores = []
while True:
    entry = input("Enter a test score (or type 'done' to analyze): ")
    if entry.lower() == 'done' :
        break

    #Ensure input is a valid number
    if entry.isdigit():
        scores.append(int(entry))
    else:
        print("Please enter a valid numeric score.")

if len(scores) > 0:
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)

    print("\n--- Final Data Analysis ---")
    print(f"Total Students Evaluated: {len(scores)}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")
    print(f"Class Average: {average:.2f}")

else:
    print("No data points were entered.")
