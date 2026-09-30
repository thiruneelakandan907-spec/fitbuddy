print("💪 Welcome to FitBuddy - Your Fitness Partner!")

workouts = []

while True:
    print("\n1. Add Workout")
    print("2. View Summary")
    print("3. Exit")
    choice = input("Un choice enna (1/2/3): ")

    if choice == '1':
        name = input("Workout name (ex: Pushups): ")
        cal = int(input("Calories burned: "))
        workouts.append({"name": name, "cal": cal})
        print(f"✅ {name} added!")

    elif choice == '2':
        total = sum(w['cal'] for w in workouts)
        print(f"\n--- Today's Summary ---")
        print(f"Total Workouts: {len(workouts)}")
        print(f"Total Calories: {total}")
        for w in workouts:
            print(f"- {w['name']} : {w['cal']} cal")

    elif choice == '3':
        print("Bye da! Keep fit! 💪")
        break
    else:
        print("Wrong choice da, 1/2/3 mattum kudu")
