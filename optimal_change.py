# Write your solution here!
import math
from itertools import islice

#dictionary of change and value pairs in pennies
#noramlizing everything to pennies allows us to avoid decimal math
money_dict = {
    "$100 bill": 10000,   
    "$50 bill": 5000,    
    "$20 bill": 2000,    
    "$10 bill": 1000,    
    "$5 bill": 500,
    "$1 bill": 100,
    "quarter": 25,
    "dime": 10,  
    "nickel": 5,
    "penny": 1
}

def optimal_change(item_cost, amount_paid):
    #initialize output string and change dict
    #change dict will be updated with optimal change
    answer = ""
    change_dict = {}

    # determine change as a float rounding up to avoid float error
    #we multiply by 100 to convert to pennies so we can compare to
    #our money dictionary key values
    num = round(((amount_paid - item_cost) * 100),10)

    if num == 0:
        return "You paid with exact change!"
    elif num < 0:
        return f"You still owe ${abs(num) / 100}!"

    #check each reference value in money dictionary
    for x in money_dict:
        
        #determine possible change for each reference value and convert result to int so we can iterate
        result = num / money_dict[x]
        result = math.floor(result)

        # for index in range of result -> if result is 0 it skips
        # if we have the value in our change dict then add to the counter
        # if not make a new entry
        for i in range(result):
                if x in change_dict:
                    change_dict[x] += 1
                else:
                    change_dict.update({x: 1})

        #get remainder to decrease num
        num = num % money_dict[x]

        #break inner for loop if num equals 0 and move to next money index value
        if num == 0:
            break
    
    #call string builder function to concat our answer string
    answer = output_builder(change_dict, answer, item_cost, amount_paid)

    return answer


#function to build our output string using string interpolation
def output_builder(change_dict, output, item_cost, amount_paid):
    
    #base case string to build off of
    output += f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is "
    
    #islice lets us iterate through dictionary starting and stopping
    #where we want
    #this for loop starts at beginning and ends before last key
    #build our string for single or plural denominations
    #if we only have 1 key then this is not activated
    for k in islice(change_dict, 0, len(change_dict)-1):
        output += f"{change_dict[k]} {k +'s' if change_dict[k] > 1 else k}, "
    
    #for loop for the last key only
    #if last key is penny and is > 1 output pennies else normal denomination
    #also checks if dict length is 1 and removes the "and" if true
    for k in islice(change_dict, len(change_dict) -1, None):
        if k == "penny" and change_dict[k] > 1:
            if len(change_dict) == 1:
                output += f"{change_dict[k]} pennies."
            else:
                output += f"and {change_dict[k]} pennies."
        elif len(change_dict) == 1:
            output += f"{change_dict[k]} {k +'s' if change_dict[k] > 1 else k}."
        else:
            output += f"and {change_dict[k]} {k +'s' if change_dict[k] > 1 else k}."


    return output

