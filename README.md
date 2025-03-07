[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18581822)
# 5.03-Weekly-ToDo-List

In this lab your job is to create a week-long to-do list using a Python dictionary. Each key in the dictionary is a day of the week. Each associated value is a list of items to do that day.

The program repeatedly asks the user what action they wish to take: **add** or **get** (these will be functions).

* If the user enters **get**, the program asks for a day of the week, and then returns the to-do list for that day.
* If the user enters **add**, the program asks for a day of the week, then asks for a new item, then adds it to the specified list.
* If a user tries to **add** an item that already exists on the list for that day, the program rejects the request.
* At the start of the program the dictionary should be totally empty (containing no keys and no values).

### Example Output

```
>>>python3 daily_to_do_list.py
What would you like to do ('add' or 'get')?
>>>add
What day?
>>>Friday
What would you like to add to Friday's to-do list?
>>>practice clarinet
What would you like to do ('add' or 'get')?
>>>get
What day?
>>>Friday
You have to practice clarinet.
What would you like to do('add' or 'get')?
```

## Bonus
1. It's a bit tedious for the user to have to type in three different lines to add an item to a to-do list. Use `split()` to allow the user to input `“add Friday watch tv and relax”`.

2. Create a variation of the program that doesn't allow any duplicates across any of the days. Make sure when you add a to-do item that it doesn't exist in the to-do lists of any of the days before adding.
