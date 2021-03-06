from collections import defaultdict

test_inputs = [
    [1,3,2],
    [2,1,3],
    [1,2,3],
    [2,3,1],
    [3,2,1],
    [3,1,2]
]
test_answers = [1,10,27,78,438,1836]
real_input = [9,6,0,10,18,2,1]

def play_game(inputs):
    spoken_numbers = defaultdict(list)
    for (i, v) in enumerate(inputs):
        spoken_numbers[v].append(i)
        last_spoken = v

    for x in range(len(inputs), 2020):
        if len(spoken_numbers[last_spoken]) == 1:
            spoken_numbers[0].append(x)
            last_spoken = 0
        else:
           to_speak = spoken_numbers[last_spoken][-1] - spoken_numbers[last_spoken][-2]
           spoken_numbers[to_speak].append(x)
           last_spoken = to_speak
    return last_spoken

for (i, test) in enumerate(test_inputs):
    last_spoken = play_game(test)
    if test_answers[i] == last_spoken:
        print("Expected the answer %s and found it!" % test_answers[i])
    else:
        print("Expected to see %s, but saw %s" % (test_answers[i], last_spoken))

print("Final answer is %s" % play_game(real_input))
