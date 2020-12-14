buses = []
full_data = open("input.txt", 'r')
full_text = full_data.read()
earliest, schedule = full_text.strip().split('\n')
earliest = int(earliest)
schedule = schedule.split(',')

test_time = [0 for x in shedule]
for bus in schedule:
    if bus == 'x':
        continue
    
    t = int(bus)
    catchable = 0
    while catchable < earliest:
        catchable += t
    if catchable < closest:
        closest = catchable
        closest_id = t
        print("New Closest is %s at %s minutes" % (t, closest))


print("Closest is %s at %s minutes, giving %s" % (closest_id, closest - earliest, closest_id * (closest - earliest)))
full_data.close()
