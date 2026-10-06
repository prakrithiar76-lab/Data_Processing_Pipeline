import pandas as pd
import logging
import os
import json

# Load configuration
with open("config.json", "r") as file:
    config = json.load(file)

input_file = config["input_file"]
output_file = config["output_file"]
log_file = config["log_file"]

# Create folders if they don't exist
os.makedirs("output", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    # Step 1: Read the CSV file
    logging.info("Pipeline started")
    df = pd.read_csv(input_file)

    print("Original Data:")
    print(df)

    # Step 2: Check missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    logging.info("Missing values checked")

    # Step 3: Fill missing values
    df["marks"] = df["marks"].fillna(df["marks"].median())
    df["attendance"] = df["attendance"].fillna(df["attendance"].median())

    # Step 4: Convert data types
    df["student_id"] = df["student_id"].astype(int)
    df["age"] = df["age"].astype(int)
    df["marks"] = df["marks"].astype(float)
    df["attendance"] = df["attendance"].astype(float)

    # Step 5: Create performance status
    df["status"] = df["marks"].apply(
        lambda x: "Pass" if x >= 50 else "Fail"
    )

    # Step 6: Save processed data
    df.to_csv(output_file, index=False)

    logging.info("Processed data saved successfully")
    logging.info("Pipeline completed successfully")

    print("\nProcessed Data:")
    print(df)

    print("\nPipeline completed successfully!")
    print("Output saved to:", output_file)

except Exception as e:
    logging.error(f"Pipeline failed: {e}")
    print("Error:", e)