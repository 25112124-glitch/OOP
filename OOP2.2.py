#1
r = int(input("Enter the radius of the sphere: "))
print ("The volume of the sphere is: ", f"{(4/3) * 3.14159 * r**3:.2f}")
#2
copies = int(input("Enter the number of copies: "))
cover_price = 24.95
discount = 0.4
shipping_first = 3
additional_shipping = 0.75
total_cost = (cover_price*(1-discount)*copies+(shipping_first + additional_shipping * (copies - 1)))
print("The total wholesale cost for", copies, "copies is: $", f"{total_cost:.2f}")
#3
easy_pace = 8*60 + 15
tempo_pace = 7*60 + 12
easy_pace_miles = int(input("Enter the distance in miles for the easy pace: "))
tempo_pace_miles = int(input("Enter the distance in miles for the tempo pace: "))
total_running_time = (easy_pace * easy_pace_miles) + (tempo_pace * tempo_pace_miles)
total_running_time_minutes = total_running_time // 60
time_leaving_in_hours = 6
time_leaving_in_minutes = 52
if (time_leaving_in_minutes + total_running_time_minutes >=60):
    time_leaving_in_hours = time_leaving_in_hours + 1
    time_leaving_in_minutes = (time_leaving_in_minutes + total_running_time_minutes) - 60
    print("You comeback for breakfast at: ", time_leaving_in_hours, ":", time_leaving_in_minutes)
else: 
    print("You comeback for breakfast at: ", time_leaving_in_hours, ":", time_leaving_in_minutes + total_running_time_minutes)

    
