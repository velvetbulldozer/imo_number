############
# packages #
############

# random integer generation
from random import randint

# type hinting
from typing import List


#############
# functions #
#############

def desired_amount(amount: int, output_as_int: bool = True) -> List[int|str]:
    """The desired amount of IMO numbers that need to be generated.
    Optional to change output to strings.

    Args:
        amount (int): Amount of IMO numbers generated.
        output_as_int (bool, optional): Option to change output to integers. 
        Defaults to True = integers.

    Returns:
        List[int]: List with IMO numbers as integers or strings.
    """
  
    number = []
    
    while len(number) < amount:
        created_number = create_number()
        
        if created_number != None:
            number.append(created_number)
    
    if output_as_int: 
        number = [int(item) for item in number] 
        return number
    
    else:
        return number
        

def create_number() -> int:
    """ Creates a seven digit valid IMO number 
    between the range 5000000 and 9999999.

    Returns:
        int: A seven digit valid IMO number.
    """
    
    number = randint(5000000,9999999)
    number = imo_number_validator(number)
    return number


def imo_number_validator(number: int, output_as_int: bool = True) -> [int|str]:
    """Validates an IMO number and returns number if valid. 
    If invalid returns None. Optional to change output to strings.
    
    Args:
        number (int): A possible IMO number.
        output_as_int (bool, optional): _description_. Defaults to True.

    Returns:
        [int|str]: An IMO number if valid.   
    """
    
    try:
        imo_int = int(number)
        imo_str = str(number)

        imo_checksum = (int(imo_str[-7]) *7) + (int(imo_str[-6]) *6) + (int(imo_str[-5]) *5) + (int(imo_str[-4]) *4) + (int(imo_str[-3]) *3) + (int(imo_str[-2]) *2)

        if str(imo_checksum)[-1] == imo_str[-1]:
            
            if output_as_int:
                return imo_int
            
            else:
                return imo_str
        
        else:
            pass
    
    except (ValueError, IndexError) as e:
        pass


#########
# USAGE #
#########

imo_numbers  = desired_amount(12, False)
print(f"list of IMO numbers: {imo_numbers}")

validated_number = imo_number_validator('9582960', False)
print(f"Valid IMO number: {validated_number}")