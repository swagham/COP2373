import csv
import numpy as np
import pandas as pd

# Function to read CSV data and convert to numpy array
def read_csv_to_numpy(filename='grades.csv'):
    df = pd.read_csv(filename)
    return df.to_numpy(), df

# Read CSV and convert to numpy array
data, df = read_csv_to_numpy()

# Print the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Calculate statistics for each exam
exam_columns = ["Exam 1", "Exam 2", "Exam 3"]
stats = {}

for exam in exam_columns:
    exam_data = df[exam]
    stats[exam] = {
        "Mean": np.mean(exam_data),
        "Median": np.median(exam_data),
        "Std Dev": np.std(exam_data),
        "Min": np.min(exam_data),
        "Max": np.max(exam_data)
    }

# Print statistics for each exam
for exam, stat in stats.items():
    print(f"\nStatistics for {exam}:")
    for key, value in stat.items():
        print(f"{key}: {value:.2f}")

# Combine all exam scores into a single array
all_exam_data = df[exam_columns].to_numpy().flatten()

# Calculate overall statistics
overall_stats = {
    "Mean": np.mean(all_exam_data),
    "Median": np.median(all_exam_data),
    "Std Dev": np.std(all_exam_data),
    "Min": np.min(all_exam_data),
    "Max": np.max(all_exam_data)
}

# Print overall statistics
print("\nOverall statistics for all exams combined:")
for key, value in overall_stats.items():
    print(f"{key}: {value:.2f}")

# Determine pass/fail counts for each exam
pass_fail_counts = {}

for exam in exam_columns:
    exam_data = df[exam]
    passed = np.sum(exam_data >= 60)
    failed = np.sum(exam_data < 60)
    pass_fail_counts[exam] = {
        "Passed": passed,
        "Failed": failed
    }

# Print pass/fail counts for each exam
for exam, counts in pass_fail_counts.items():
    print(f"\nPass/Fail counts for {exam}:")
    print(f"Passed: {counts['Passed']}")
    print(f"Failed: {counts['Failed']}")

# Calculate overall pass percentage across all exams
total_students = df.shape[0]
total_exams = total_students * len(exam_columns)
total_passed = np.sum(all_exam_data >= 60)

overall_pass_percentage = (total_passed / total_exams) * 100

# Print overall pass percentage
print(f"\nOverall pass percentage across all exams: {overall_pass_percentage:.2f}%")