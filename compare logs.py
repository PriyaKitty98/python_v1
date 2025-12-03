import os

# -----------------------------
# CONFIGURABLE INPUT
# -----------------------------
# List all log files you want to compare
log_files = [
    "log1.txt",
    "log2.txt",
    "log3.txt"
]

# Output combined file
output_file = "combined_status_output.txt"

# Markers to identify summary area
start_marker = "Deployment Summary"
end_marker = "==================================================="

# -----------------------------
# PROCESSING
# -----------------------------
def extract_summary(filename):
    """Extract the Deployment Summary section from a single log file."""
    capturing = False
    summary = []

    try:
        with open(filename, "r") as f:
            for line in f:
                if start_marker in line:
                    capturing = True
                    continue

                if capturing and end_marker in line:
                    break

                if capturing:
                    summary.append(line.strip())

        return summary

    except FileNotFoundError:
        return [f"❌ ERROR: File not found: {filename}"]

# -----------------------------
# WRITE COMBINED OUTPUT
# -----------------------------
with open(output_file, "w") as out:
    out.write("========== Combined Deployment Status ==========\n\n")

    for log in log_files:
        out.write(f"------ Status from {log} ------\n")
        summary = extract_summary(log)
        for line in summary:
            if line:
                out.write(line + "\n")
        out.write("\n")

print(f"✔ Combined deployment status file created: {output_file}")
