log_file = open("um-server-01.txt") #this first line is opening the file 'um-server-01.txt' under the variable name of 'log_file' in python.


def sales_reports(log_file): #def marks the start of the function header named 'sales reports' that takes the variable 'log_file' as an argument - it's opening um-server-01.txt
    for line in log_file: #the start of a 'for in' loop of um-server-01 ~ line is an ambigous keyword that will be referenced later in the code.. like a parameter
        line = line.rstrip() # line is being redefined/re-declared with the built in .rstrip() method - no argument is given so it will remove all trailing spaces from 'um-server-01.txt
        day = line[0:3] #[0:3] is notation for a slice starting at 0 index and ending at the 2nd index being assigned to a variable 'day'
        if day == "Mon": #if the slice in day is equal to the string "Tue"... or later "Mon"
            print(line) #...it will print the entire line
#this is a function that will 'comb' through the file 'um-server-01.txt' and print out every line containting the string "Tue", case sensitive.  This does not do any thing by itself, it will need to be called in order execute.

# sales_reports(log_file) #this is calling on the sales_reports function with the argument of the log_file variable - this is making the function execute.




# Did not finish extra credit for python 
def ten_watermelons(log_file):
    for line in log_file: 
        # line = line.rstrip()
        qty = line[16:18] 
        if int(qty) >= 10:
            return line    






# sales_reports(log_file)

ten_watermelons(log_file)









#PRINTED INFORMATION FOR MONDAY
# $ python process.py 
# Mon 2014-05-19: 2 Carolina Cross 180 Watermelon delivered to User 39
# Mon 2014-05-19: 9 Tom Watson Watermelon delivered to User 39
# Mon 2014-05-19: 5 Japanese Cream Fleshed Suika Watermelon delivered to User 661
# Mon 2014-05-19: 3 Densuke delivered to User 661
# Mon 2014-05-19: 7 Navajo Winter Watermelon delivered to User 661
# Mon 2014-05-19: 8 Jubilee Watermelon delivered to User 991
# Mon 2014-05-19: 1 Moon and Stars Yellow Flesh Watermelon delivered to User 847
# Mon 2014-05-19: 7 Casaba delivered to User 142
# Mon 2014-05-19: 2 Mississippi Cobb Gem Watermelon delivered to User 142
# Mon 2014-05-19: 1 Malali Watermelon delivered to User 142
# Mon 2014-05-19: 8 Moon and Stars Watermelon delivered to User 142
# Mon 2014-05-19: 1 Montenegro Man Watermelon delivered to User 142
# Mon 2014-05-19: 10 Crenshaw delivered to User 538
# Mon 2014-05-19: 1 White Wonder Watermelon delivered to User 538
# Mon 2014-05-19: 65 Densuke delivered to User 538
# Mon 2014-05-19: 48 Irish Grey Watermelon delivered to User 538
# Mon 2014-05-19: 1 Fairfax Watermelon delivered to User 538
# Mon 2014-05-19: 18 Georgia Rattlesnake Watermelon delivered to User 254
# Mon 2014-05-19: 5 Mississippi Cobb Gem Watermelon delivered to User 254
# Mon 2014-05-19: 6 Crane delivered to User 254
# Mon 2014-05-19: 38 Navajo Winter Watermelon delivered to User 254
# Mon 2014-05-19: 7 Hopi Yellow Watermelon delivered to User 254
# Mon 2014-05-19: 1 Crenshaw delivered to User 793
# Mon 2014-05-19: 2 Hopi Yellow Watermelon delivered to User 18
# Mon 2014-05-19: 3 Texas Golden Watermelon delivered to User 18
# Mon 2014-05-19: 61 Fairfax Watermelon delivered to User 18
# Mon 2014-05-19: 5 Desert King Watermelon delivered to User 18
# Mon 2014-05-19: 2 Wilson's Sweet Watermelon delivered to User 112
# Mon 2014-05-19: 9 Moon and Stars Watermelon delivered to User 112
# Mon 2014-05-19: 67 Jubilee Watermelon delivered to User 112
# Mon 2014-05-19: 6 Jubilee Bush Watermelon delivered to User 112
# Mon 2014-05-19: 1 Jubilee Watermelon delivered to User 112
# Mon 2014-05-19: 75 Armenian Cucumber delivered to User 92
# Mon 2014-05-19: 3 Congo Watermelon delivered to User 92
# Mon 2014-05-19: 3 Kleckley's Sweet Watermelon delivered to User 92
# Mon 2014-05-19: 2 Casaba delivered to User 92
# Mon 2014-05-19: 7 Texas Golden Watermelon delivered to User 92
# Mon 2014-05-19: 7 Densuke delivered to User 3
# Mon 2014-05-19: 9 White Sugar Lump Watermelon delivered to User 3
# Mon 2014-05-19: 10 Crenshaw delivered to User 185
# Mon 2014-05-19: 7 Mountain Hoosier Watermelon delivered to User 53
# Mon 2014-05-19: 5 Texas Golden Watermelon delivered to User 53
# Mon 2014-05-19: 8 Desert King Watermelon delivered to User 53
# Mon 2014-05-19: 2 Moon and Stars Yellow Flesh Watermelon delivered to User 485
# Mon 2014-05-19: 3 Armenian Cucumber delivered to User 485
# Mon 2014-05-19: 3 Tom Watson Watermelon delivered to User 485
# Mon 2014-05-19: 5 Crenshaw delivered to User 376
# Mon 2014-05-19: 6 Crane delivered to User 376
# Mon 2014-05-19: 2 Chris Cross Watermelon delivered to User 376
# Mon 2014-05-19: 8 Winter Melon delivered to User 6
# Mon 2014-05-19: 48 Crenshaw delivered to User 6
# Mon 2014-05-19: 74 Congo Watermelon delivered to User 380
# Mon 2014-05-19: 7 Armenian Cucumber delivered to User 380
# Mon 2014-05-19: 1 Jubilee Bush Watermelon delivered to User 380
# Mon 2014-05-19: 4 Moon and Stars Watermelon delivered to User 380
# Mon 2014-05-19: 7 Texas Golden Watermelon delivered to User 390
# Mon 2014-05-19: 2 Golden Midget Watermelon delivered to User 390
# Mon 2014-05-19: 10 Sugar Baby Watermelon delivered to User 390
# Mon 2014-05-19: 2 Japanese Cream Fleshed Suika Watermelon delivered to User 728
# Mon 2014-05-19: 10 Orangeglo Watermelon delivered to User 381
# Mon 2014-05-19: 1 White Wonder Watermelon delivered to User 381
# Mon 2014-05-19: 5 Melitopolski Watermelon delivered to User 381
# Mon 2014-05-19: 3 Wilson's Sweet Watermelon delivered to User 381