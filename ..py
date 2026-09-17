def activity_selection(start, end):
    # Step 1: Combine start & end into pairs
    activities = list(zip(start, end))
    
    # Step 2: Sort by end time (greedy choice)
    activities.sort(key=lambda x: x[1])
    
    # Step 3: Select first activity
    count = 1
    last_end = activities[0][1]
    
    # Step 4: Loop remaining activities
    for i in range(1, len(activities)):
        # If current start >= last selected end → select
        if activities[i][0] >= last_end:
            count += 1
            last_end = activities[i][1]
    
    return count
