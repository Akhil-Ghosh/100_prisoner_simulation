import numpy as np

#making simulation of 100 prisoner problem.
#can edit the number of prisoners and number of boxes here
num_trials = 10000
num_prisoners = 100
num_attempts = 50
success = 0 
failure = 0

#generate 100 prisoners

prisoners = np.arange(num_prisoners)
#generate 100 random integers 
integers = np.arange(num_prisoners)
# Generate 100 random integers without replacement excluding 0
boxes = np.random.choice(integers, size=num_prisoners, replace=False)


#prisoner goes to box corresponding to their number

num_trials = 10000
for i in range(num_trials):
    free_prisoners = 0
    boxes = np.random.choice(integers, size=num_prisoners, replace=False)
    prisoners = np.arange(num_prisoners)
    for i in range(len(prisoners)):
        new_box = boxes[prisoners[i]]
        num = 0
        while prisoners[i] != new_box and num < num_attempts:
            new_box = boxes[new_box]
            num = num + 1
        if prisoners[i] == new_box:
            #print("prisoner is free", num)
            free_prisoners = free_prisoners + 1
#        else:  # debugging statements
#           print("prisoner is not free", num)
    if free_prisoners == 100: # threshold for success
        success = success + 1
    else:
        failure = failure + 1



print("Success rate:", success / num_trials)
print("Failure rate:", failure / num_trials)
