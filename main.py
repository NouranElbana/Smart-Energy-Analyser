#Step: Ask the user for inputs

price= float(input("Price per kwh: "))
total_daily_kwh = 0
count = 0
names_of_appliances= []
kwh_daily_list= []
watts_list= []
hours_list= []
DAYS= 30
BUDGET= 50
TIER_LIMIT= 300
TIER_MULTIPLIER= 1.5

def calc_cost(monthly_kwh, price):
    if monthly_kwh <= TIER_LIMIT:
        cost = monthly_kwh * price
    else:
        cost = (TIER_LIMIT * price) + ((monthly_kwh - TIER_LIMIT) * TIER_MULTIPLIER * price)

    return cost

def search_appliance():
    name = input("Enter the name of the appliance to search for: ").strip().title()
    if name in names_of_appliances:
        index = names_of_appliances.index(name)
        print(f"Appliance found: {name}")
        print(f"Power (watts): {watts_list[index]}")
        print(f"Hours per day: {hours_list[index]}")
        print(f"Daily energy (kWh): {kwh_daily_list[index]}")
    else:
        print(f"{name} not found in the list of appliances.")

def full_report():
    if len(names_of_appliances)==0:
        print("No appliances added yet.")
        return
    else:
        print("-" * 40)
        print("Appliance Report")
        print("-" * 40)
        for i in range(len(names_of_appliances)):
            share= kwh_daily_list[i] / total_daily_kwh * 100
            print( i+1, names_of_appliances[i], "-", kwh_daily_list[i], "kWh/day,", f"{share:.2f}%", "of total daily energy")
        print("-" * 40)
        print("Total:", round(total_daily_kwh, 2), "kWh/day")
        print("Estimated monthly cost:", round(total_daily_kwh * DAYS * price, 2), "USD")
        top_i= kwh_daily_list.index(max(kwh_daily_list))
        print("Biggest energy consumer:", names_of_appliances[top_i])
        saved_kwh= watts_list[top_i] /1000 * DAYS
        print("Tip: You can save", round(saved_kwh, 2), "kWh/month by unplugging", names_of_appliances[top_i], "One hour a day.")

def remove_appliance(remove):
    if remove in names_of_appliances:
        i= names_of_appliances.index(remove)
        names_of_appliances.pop(i)
        kwh_daily_list.pop(i)
        watts_list.pop(i)
        hours_list.pop(i)
        return True
    return False

def find_appliance():
    if len(names_of_appliances) ==0:
        print("No appliances added yet.")
        return

    energy= {}
    for i in range(len(names_of_appliances)):
        energy[names_of_appliances[i]] = kwh_daily_list[i]

    wanted= set()
    for w in input("Enter appliance name (separated by comma)").split(","):
        if w.strip() != "":
            wanted.add(w.strip().title())

    found= wanted & set(energy)
    missing= wanted - set(energy)

    for name in sorted(found):
        print("Found:", name, "-", energy[name], "kWh/day")
    if len(missing) > 0:
        print("Not found:", ", ".join(missing))

#Menu to ask the user
while True:
    print()
    print("1.Add appliance")
    print("2.View total")
    print("3.Search for appliance")
    print("4.Full report")
    print("5.Exit")
    print("6.Remove Appliance")
    print("7.Find Appliance")
    choice = input("Enter your choice:")

    #The process of adding an appliance
    if choice == "1":
        name_of_appliance = input("Appliance name: ").strip().title()
        if name_of_appliance in names_of_appliances:
            print(name_of_appliance, "is already added!")
            continue

        watts = float(input("Power (watts) per day: "))
        while watts <= 0:
            print("Watts must be more than 0!")
            watts = float(input("Power (watts) per day: "))

        hours = float(input("Hours: "))
        while 0 <= hours > 24:
            print("Hours must be between 0 and 24!")
            hours = float(input("Hours: "))

        total_daily_kwh = total_daily_kwh + (watts * hours) / 1000
        count += 1

        names_of_appliances.append(name_of_appliance)
        kwh_daily_list.append(total_daily_kwh)
        watts_list.append(watts)
        hours_list.append(hours)

        print("Appliance Added:", name_of_appliance)
        print("Short Code:", name_of_appliance[:3].upper())

    # The process of viewing total
    elif choice == "2":
        monthly_kwh = (total_daily_kwh * DAYS)
        cost = calc_cost(monthly_kwh, price)

        print("Appliances",count)
        print("Monthly energy: ", monthly_kwh, "kwh")
        print("Monthly cost:", cost)

        if cost > BUDGET:
            print("Warning: Your monthly cost exceeds your budget ")

        print("Names:", names_of_appliances)
        print("Power (watts):", watts_list)
        print("Hours:", hours_list)
        print("Daily energy (kWh):", kwh_daily_list)

        if len(names_of_appliances) > 0:
            print("Max daily energy:", max(kwh_daily_list))
            print("Min hours:", min(hours_list))
            print("All names:", ", ".join(names_of_appliances))

        longest = names_of_appliances[0]
        for n in names_of_appliances:
            if len(n) > len(longest):
                longest = n
        print("Longest name:", longest, "-", len(longest), "letters")



    elif choice == "3":
        search_appliance()

    elif choice == "4":
        full_report()


    # stopping the program
    elif choice == "5":
        print("See you later!")
        break

    elif choice == "6":
        remove = input("Appliance to remove: ")
        remove = remove.strip().title()
        if remove_appliance(remove):
            total_daily_kwh = sum(kwh_daily_list)
            count = len(names_of_appliances)
            print(remove, "was removed")
        else:
            print("No appliance called", remove)

    elif choice == "7":
        find_appliance()

    else:
        print("Invalid choice. Please try again.")




