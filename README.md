# todoist-schoology
I'm integrating the schoology calendar with todoist
This **ONLY** works with accounts that have todoist premium.

## There's more explanation to come, but here's some info:
I used [this library](https://github.com/Garee/PyTodoist) to interface with todoist; the official todoist library was acting weird.
I used the [requests](https://github.com/kennethreitz/requests) library to make http calls to the schoology api.

## Note:
The todoist api gets offended if you run the script too quickly after you just ran it. This shouldn't be an issue for normal use, however.

If you want something like this but for Apple reminders, then you should check [this](https://github.com/PostsDesert/SiRI) out.
