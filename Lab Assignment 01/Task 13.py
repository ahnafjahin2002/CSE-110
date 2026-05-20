total_seconds = int(input("Input: "))

# Calculate hours, minutes, and remaining seconds
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("Output: Hours:", hours, " Minutes:", minutes, " Seconds:", seconds)