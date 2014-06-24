def my_own_function(milks, calories):
    print "You drank %r cups of milk. You added %r calories." % (milks, calories * milks)

my_own_function(8, 300)
 
number_milk = 10
milk_calories = 350

my_own_function(number_milk, milk_calories)

my_own_function(number_milk * 20, milk_calories + 50)

my_own_function(20 * 3, 300 + 100)

my_own_function(int(raw_input("milks:")), int(raw_input("Calories:")))

my_own_function(int(raw_input("milks:")) + 10000, int(raw_input("Calories:")) * 150)
