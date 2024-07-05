# YOU ONLY HAVE TO SUBMIT FUNCTIONS FOR WHICH
# YOU ARE THE DRIVER IN PAIR PROGRAMMING


# Here are some history variables to test your code on. Feel free to create your own.
hist1 = []
hist2 = [("split","steal")]
hist3 = [("split","split"),("steal","split"),("split","steal"),("split","split"),("steal","split")]
hist4 = [("split","steal"),("steal","steal"),("split","steal"),("steal","split"),("split","split"),("steal","split")]

# Your team's 1st strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 2nd strategy (leave blank if you are not the driver)
# Explanation of Strategy: output is the opposite of the last choice of the opponent
# 
def turingcompetestrategy2(hist):
    try:
        last = hist[len(hist) - 1]
        if last[1] == "split":
            return "steal"
        else:
            return "split"
    except IndexError:
        return "split"



# Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 
print(turingcompetestrategy2(hist1))