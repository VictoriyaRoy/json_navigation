# JSON Navigation
This project implements navigation on json file created by Twitter API

## How to use program
1. start function *main()*
2. enter *path* to json file
3. There are 3 types of program's *behaviour*:
* item is *array*: lenght of array is displayed, user should choose index or "all" to see whole array
* item is *object*: keys are displayed, user should choose key or "all" to see whole object
* item is *string*, number, bool: this information is displayed

## Example of working program
```
Enter the path to json file: json_files\friends_list_AdamMGrant.json
This item is an object with these keys:
users
next_cursor
next_cursor_str
previous_cursor
previous_cursor_str
total_count
Enter key you want to see or "all" to see whole object: users

This item is an array with 10 elements
Enter index of element you want to see or "all" to see whole array: 6

This item is an object with these keys:
id
id_str
name
screen_name
location
description
...
blocking
blocked_by
translator_type
Enter key you want to see or "all" to see whole object: location

Paris, France
```
