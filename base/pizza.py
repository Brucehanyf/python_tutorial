def pizza_factory (size,*toppings):
    print ('make a '+ str(size) +'-inch pizza The toppings is following:')
    for topping in toppings:
        print (topping)