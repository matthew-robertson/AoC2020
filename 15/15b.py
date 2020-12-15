from collections import defaultdict
real_input = [9,6,0,10,18,2,1]

def play_game(inputs):
    spoken_numbers = defaultdict(list)
    for (i, v) in enumerate(inputs):
        spoken_numbers[v].append(i)
        last_spoken = v

    for x in range(len(inputs), 30000000):
        if len(spoken_numbers[last_spoken]) == 1:
            spoken_numbers[0].append(x)
            last_spoken = 0
        else:
           to_speak = spoken_numbers[last_spoken][-1] - spoken_numbers[last_spoken][-2]
           spoken_numbers[to_speak].append(x)
           last_spoken = to_speak
    return last_spoken

print("Final answer is %s" % play_game(real_input))
