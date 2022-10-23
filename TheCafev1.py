#The Cafe v1
#by Truth Fernsword, 2022
#this is meant to be a coffee shop-esque experience, where you can make a drink that one might find in a coffee shop. .

#testing diff

import data_type_test_functions

bases = {
	"coffee" : {
		"Description" : "Dirty bean juice. Gotta love it.",
		"Cost" : 2,
		"Name" : "Coffee"
	},

	"tea" : {
		"Description" : "Dirty leaf juice. It's okay.",
		"Cost" : 2,
		"Name" : "Tea"
	},
	
	"milk" : {
		"Description" : "Moo juice.",
		"Cost" : 2,
		"Name" : "Milk"
	}
}

additives = {
	"cinnamon" : {
		"Name" : "Cinnamon",
		"Description" : "Who knew this was tree bark?",
		"Cost" : 2
	},

	"sugar" : {
		"Name" : "Sugar",
		"Description" : "Sweet crystals",
		"Cost" : 1
	},

	"cocoa powder" : {
		"Name" : "Cocoa Powder",
		"Description" : "Surprisingly bitter on its own",
		"Cost" : 2
	}
}

def cost_format(cost):
	return "${:,.2f}".format(cost)

cost = 0

base_names = []

for key, inner_dict in bases.items():
	base_names.append(str(inner_dict["Name"]))

additives_names = []

for key, inner_dict in additives.items():
	additives_names.append(str(inner_dict["Name"]))

print("Welcome to The Cafe! In order to brew a drink, you need to choose one base, and two additives. Your choices for bases are as follows: " + ", ".join(base_names))
print("Your choices for additives are as follows: " + ", ".join(additives_names))

base_chosen = False

while base_chosen == False:
	base_choice = input("Which base would you like to use? ").lower()

	if data_type_test_functions.IsFloat(base_choice) == True:
		print("Please enter text.")
	elif data_type_test_functions.IsString(base_choice) == True:
		base_chosen = True

if base_choice in bases:
	print(bases[base_choice]["Description"])
	print("The cost of this is: {0}".format(cost_format(bases[base_choice]["Cost"])))
	cost += bases[base_choice]["Cost"]
else:
	print("Invalid base")
	exit()

reset_additive1 = 1

while reset_additive1 == 1:
	additive1_choice = input("Choose your first additive ").lower()
	if additive1_choice in additives:
		print(additives[additive1_choice]["Description"])
		print("The cost of this is: {0}".format(cost_format(additives[additive1_choice]["Cost"])))
		cost += additives[additive1_choice]["Cost"]
		reset_additive1 = 0
	else:
		print("Invalid Additive")
		reset_additive2 == 1

reset_additive2 = 1

while reset_additive2 == 1:
	additive2_choice = input("Now your second additive ").lower()
	if additive2_choice in additives:
		print(additives[additive2_choice]["Description"])
		print("The cost of this is: {0}".format(cost_format(additives[additive2_choice]["Cost"])))
		cost += additives[additive2_choice]["Cost"]
		reset_additive2 = 0
	else:
		print("Invalid Additive")
		reset_additive2 == 1

finished_cup = base_choice + " with " + additive1_choice + " and " + additive2_choice

if additive1_choice == additive2_choice:
	finished_cup = base_choice + " with double " + additive1_choice

print("You brewed", str(finished_cup))
print("The cost of this drink is ${:,.2f}".format(cost))

payment = float(input("Please enter your payment now. $ "))
remainder_payment = 0

while payment < cost:
	remainder_balance = cost-payment
	remainder_payment = float(input("You have a remaining balance. Please pay ${:,.2f}".format(remainder_balance)))
	payment = payment+remainder_payment

while payment > cost:
	change = payment-cost
	print("Your change is ${:,.2f}".format(change))
	payment = payment-change


print("Enjoy your drink!")