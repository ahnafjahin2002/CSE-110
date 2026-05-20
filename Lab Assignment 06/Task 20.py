def cal_bonus(*args):
    # Loop through the args jumping by 4 (Name, Earning, Goals, Bonus Percent)
    for i in range(0, len(args), 4):
        name = args[i]
        earning = args[i+1]
        goals = args[i+2]
        bonus_pct = args[i+3]
        
        # Calculate standard bonus
        bonus = goals * ( (bonus_pct / 100) * earning )
        
        # Add extra bonuses based on total goals scored
        if goals > 30:
            bonus += 10000
        elif 20 <= goals <= 30:
            bonus += 5000
            
        print(f"{name} earned a bonus of {int(bonus)} Taka for {goals} goals.")

# Function Call
cal_bonus("Neymar", 1200000, 35, 5)
cal_bonus("Neymar", 1200000, 30, 10, "Jamal", 700000, 19, 5)