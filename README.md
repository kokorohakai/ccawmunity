# CCAWMUNITY
## Computer Club Community project
### HOW TO CONTRIBUTE A FUNCTION

### Checklist:

- [ ] create a function definition that matches the following

- [ ] add the command to the above list,
      then create a matching .py file.
      then create a matching function within that file.
      all of these should be named the exact same.

- [ ] use the same arguments as the other commands,
      as these are standardized for that event type
      (all COMMANDLIST functions are for message.text events)

- [ ] make sure you're returning a string

- [ ] add the function chat name to the COMMANDLIST dictionary
      as a key AND the function definition name as the value
      ie COMMANDLIST["$test"] = test

- [ ] add the function chat name to the HELPLIST dictionary as
      a key AND a string explaining how to use it as the value
      ie HELPLIST["$test"] = "$test - returns a String yelling at dolphin"

To start your own instance of this server, copy config.dist.py to config.py
and fill in your credentials for your bot.
