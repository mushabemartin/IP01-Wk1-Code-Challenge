def convert_to_24_hour(hour, minute, period):
    # Check if it's morning (AM)
    if period.lower() == "am":
        # If it's 12:00 AM, convert to 00:00
        if hour == 12:
            hour = 0
    else:
        # If it's PM and not 12:00 PM, add 12 to the hour
        if hour != 12:
            hour += 12
    
    # Return the result in 24-hour format with leading zeros
    return f"{hour:02d}{minute:02d}"

# Test cases
print(convert_to_24_hour(8, 30, "am"))  # Output: 0830
print(convert_to_24_hour(8, 30, "pm"))  # Output: 2030
