import settings
from commands import *

# HOW TO CONTRIBUTE A FUNCTION
#
# Checklist:
#
# [ ] create a function definition that matches the following
#
# [ ] use the same arguments as others in the same list
#     as these are standardized for that event type
#     (all COMMANDLIST functions are for message.text events)
#
# [ ] make sure you're returning a string
#
# [ ] add the function chat name to the COMMANDLIST dictionary
#     as a key AND the function definition name as the value
#     ie "$test": test
#
# [ ] add the function chat name to the HELPLIST dictionary as
#     a key AND a string explaining how to use it as the value
#     ie "$test": "$test - returns a String yelling at dolphin"
#
# [ ] double check that the dictionaries follow the format
#     "key": value, the last k/v in a dictionary has no trailing comma


# REMINDER - make sure the commas follow every k/v pair except
#            for the last one in each dictionary!

# define all commands as functions in a global dictionary for easy comparison and use
# note the values are function objects



# define our global help list based on the function
HELPLIST = {
    "$test": "$test - No parameters requirerd, yells at dolphin.",
    "$random": "$random - No parameters required, returns number 0-100 inclusive.",
    "$echo": "$echo - N parameters accepted separated by spaces, bot echoes them back to chat.\"$echo arg1 arg2\"",
    "$commands": "$commands - No parameters required, lists all available commands.",
    "$help": "$help - 1 accepted, returns information about the use of a given function ie \"$help $echo\".",
    "$eccho": "$eccho - No parameters required, inside A E S T H E T I C joke.",
    "$contribute": "$contribute - No parameters required, links the repository url."
}
