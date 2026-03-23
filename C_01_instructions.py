# Check that users have entered a valid
# option based on a list


def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item
            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

def instruction():
    print('''

**** Instructions ****

There are 3 options you can choose, rock, paper, and scissors.
Each option has something it beats, and something that beats it,
the only thing that cannot beat it is itself.

-	Remember that…
    o	Paper beats rock
    o	Rock beats scissors
    o	Scissors beats paper

    ''')


# Main routine
print()
print("💎📰✂️ Rock Paper Scissors ✂️📰💎")
print()

# Loop for testing purposes
want_instructions = string_checker("Do you want to read the instructions?")

# Checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("Program continues")