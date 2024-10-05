import another_module
print(another_module.another_variable)

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("First Name", ["Sunil", "Shantanu", "Shanaya"])
table.add_column("Work", ["JOB", "study", "Masti"])

print(table)
