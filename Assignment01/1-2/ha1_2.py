#AI-Generated Code
def min_postage_stamps(target, stamp_denominations):
    total_stamps_needed = 0
    stamps_used = {}
    
    for stamp in stamp_denominations:
        if target == 0:
            break
            
        if target >= stamp:
            # Calculate how many of this specific stamp we can use
            count = target // stamp
            total_stamps_needed += count
            
            # Reduce the target by the total value of these stamps
            target %= stamp
            stamps_used[stamp] = count
            
    return total_stamps_needed, stamps_used

# Testing the algorithm
stamps = [1500, 1225, 350, 100, 70, 34, 21, 10, 1]
target_cost = 140

count, breakdown = min_postage_stamps(target_cost, stamps)
print(f"Q2 Minimum stamps needed: {count}")
print(f"Q2 Stamp breakdown: {breakdown}")