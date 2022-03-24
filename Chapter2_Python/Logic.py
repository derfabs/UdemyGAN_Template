# == (Equal)
# < (Less than)
# > (Greater than)
# != (Not Equal)
# <= (Less or equal than)
# >= (Greater or equal than)

i_am_broke = False

if i_am_broke:
    print("I am broke")
else:
    print("I am not broke")

my_bank_account = 1000

if my_bank_account <= 0:
    print("I am broke.")
else:
    print("I am not broke.")

my_age = 27

if my_age < 18:
    print("You are a child")
elif my_age < 67:
    print("You are an adult")
else:
    print("You are a pensioneer")
