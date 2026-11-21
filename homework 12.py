# homework completion tracker

# part 1: set today's total number of homework tasks
total_homework = 4
original_count = total_homework
print(f"you have {original_count} homework tasks to finish today!\n")

# part 2: keep a counter for completed homework and the current task number
completed_count = 0
task_num = 1

# part 3: repeat while there are still homework tasks left
while task_num <= total_homework:

    # part 4: work out the current homework task from its number
    if task_num == 1:
        next_task = "math worksheet"
    elif task_num == 2:
        next_task = "science reading"
    elif task_num == 3:
        next_task = "english writing"
    else:
        next_task = "coding practice"

    answer = input(f"have you finished: {next_task}? (yes/no): ")

    # part 5: only move on once the task is marked done
    if answer == "yes":
        completed_count += 1
        task_num += 1
        print("great job! homework task completed.")
    else:
        print("okay, finish it and check again!")

    # part 6: print how many homework tasks remain
    print("homework tasks remaining:", total_homework - completed_count)
    print()

# part 7: this only prints once every homework task is marked done
print("===== all homework complete! =====")
print("great work finishing your homework today!\n")

# part 8: a safe look at what an infinite loop would look like
print("now let's safely peek at an infinite loop...")
test_value = 0
safety_counter = 0

while test_value <= 0:
    print("this condition never changes, so this would run forever!")
    safety_counter += 1

    if safety_counter == 3:
        print("(stopping here on purpose - a real infinite loop never stops on its own!)")
        break

# part 9: print the final homework checklist summary
print("\n===== homework completion summary =====")
print("homework assigned today:", original_count)
print("homework completed:", completed_count)
print("homework remaining:", total_homework - completed_count)
print("=======================================")