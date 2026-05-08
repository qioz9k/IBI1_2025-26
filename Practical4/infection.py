"""
Pseudocode (Lab Document Requirement):
1. Define initial parameters:
   - initial infected = 5
   - daily growth rate = 40% (0.4)
   - total students in class = 91
   - current infected = initial infected
   - days = 1 (Day 1 is the initial state)
2. Print initial infection information (for verification)
3. Start while loop: continue calculating while current infected < 91
   - days +1
   - current infected = previous day infected × (1 + growth rate)
   - print current day and infected count (1 decimal place for clarity)
4. After loop ends, print total days for full infection
"""

initial_infected = 5       # Initial infected population
growth_rate = 0.4          # Daily growth rate 40%
total_students = 91        # Total number of students in the class
current_infected = initial_infected  # Daily infected population
days = 1                   # Initial day count (Day 1)

print("=== Class Infection Spread Simulation ===")
print(f"Initial infected: {initial_infected} people")
print(f"Daily growth rate: {growth_rate*100}%")
print(f"Total class size: {total_students} people")
print("-" * 30)
print(f"Day {days}, Infected: {current_infected} people") 
# Loop condition: continue as long as current infected < total students
while current_infected < total_students:
    days += 1  # Increment day count (move to next day)
    # Calculate current infected: previous day × (1 + growth rate)
    current_infected = current_infected * (1 + growth_rate)
    # Print daily data (1 decimal place to avoid excessive decimal digits)
    print(f"Day {days}, Infected: {current_infected:.1f} people")

print("-" * 30)
print(f"Simulation complete. All {total_students} students infected. Total days: {days}")