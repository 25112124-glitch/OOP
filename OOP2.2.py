#1
r = 5
print ("The volume of the sphere is: ", f"{(4/3) * 3.14159 * r**3:.2f}")
#2
copies = 60
cover_price = 24.95
discount = 0.4
shipping_first = 3
additional_shipping = 0.75
total_cost = (cover_price*(1-discount)*copies+(shipping_first + additional_shipping * (copies - 1)))
print("The total wholesale cost for", copies, "copies is: $", f"{total_cost:.2f}")
#3
time_started = 6*60*60 + 52*60
easy_pace = 8*60 + 15
tempo_pace = 7*60 + 12
running_time = easy_pace*2 + tempo_pace*3
time_finished_hours = (time_started + running_time) // 3600
time_finished_minutes = ((time_started + running_time)%3600)// 60
print("The time you will comebacke for breakfast is: ", time_finished_hours, ":", time_finished_minutes)




    
