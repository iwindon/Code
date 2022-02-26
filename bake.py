EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(num):
    """
    Calculates the remaining bake time by subtracting the     expected bake time with how much time has already passed while in the oven.
    """
    return EXPECTED_BAKE_TIME - num

def elapased_bake_time():
    """
    Calculates how much time has passed in baking by adding the remaining bake time with the prepration time which is 2 minutes per layer.
    """
    return bake_time_remaining + PREPARATION_TIME

def preparation_time_in_minutes(num):
    """
    Function to calulate the preparation time, which is 2 minutes per layer.
    """
    return PREPARATION_TIME * num

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return number_of_layers * 2 + elapsed_bake_time