def find_missing(list_one, list_two):
    # check if both lists are empty
    if len(list_one) == len(list_two) == 0:
        return 0
    
	# check if both lists are similar
    if not set(list_one).symmetric_difference(set(list_two)):
        return 0
    elif list_one != list_two:
        x = list(set(list_one) - set(list_two))
        y = list(set(list_two) - set(list_one))

        if x != []:
            return x[0]
        else:
            return y[0]
    else:
        return list(set(list_one).symmetric_difference(set(list_two)))