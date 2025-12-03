import csv
import os

# List your output files here
output_files = [
    "combined_status_output.txt",
    "status_output.txt"
]

# CSV file to be created
csv_file = "Single_status_report.csv"

# Function to parse a single output file
def parse_status_file(filename):
    entries = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()

            # Skip empty and header lines
            if not line or "Deployment Status" in line:
                continue

            # Expect format: <App> : <Status>
            if ":" in line:
                parts = line.split(":")
                app = parts[0].strip()
                status = parts[1].strip()
                entries.append((app, status))

    return entries


# Write to CSV
with open(csv_file, "w", newline="") as csv_out:
    writer = csv.writer(csv_out)
    
    # CSV Header
    writer.writerow(["Filename", "Application", "Status"])
    
    # Process each file
    for file in output_files:
        if not os.path.exists(file):
            print(f"❌ File not found: {file}")
            continue
        
        app_data = parse_status_file(file)
        
        for app, status in app_data:
            writer.writerow([file, app, status])

print(f"✔ CSV file created: {csv_file}")
