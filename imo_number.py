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
    """ The desired amount of IMO numbers to be generated.
    Optional to change output to strings.

    Args:
        amount (int): Amount of IMO numbers generated.
        output_as_int (bool, optional): Option to change output to integers. 
        Defaults to True = integers.

    Returns:
        List[int|str]: List with IMO numbers as integers or strings.
    """

    imo_number = []
    
    while len(imo_number) < amount:
        created_imo_number = create_imo_number()
        
        if created_imo_number is not None:
            imo_number.append(created_imo_number)
            
    if output_as_int:
        return [int(item) for item in imo_number] 
    
    else:
        return [str(item) for item in imo_number]
  

def create_imo_number() -> int:
    """ Creates a seven digit valid IMO number.
    Between range 5000000 and 9999999.

    Returns:
        int: A seven digit valid IMO number.
    """
    number = randint(5000000,9999999)
    return imo_number_validator(number)


def imo_number_validator_short(imo_number: int|str, output_as_int: bool = True) -> int|str:
    """ Validates an IMO number and returns number if valid. 
    If invalid returns None. Optional to change output to strings.
    
    Args:
        imo_number (int|str): A possible IMO number.
        output_as_int (bool, optional): False to change output to strings. Defaults to True.

    Returns:
        [int|str]: An IMO number if valid. 
    """
    imo_int = int(imo_number)
    imo_str = str(imo_number).strip()
    weights = [7, 6, 5, 4, 3, 2]
    
    try:
        if len(imo_str) != 7 or not imo_str.isdigit():
            return False
        
        total = sum(int(imo_str[i]) * weights[i] for i in range(6))
        
        if total % 10 == int(imo_str[-1]):
            return imo_int if output_as_int else imo_str
        
    except (ValueError, IndexError):
        pass


def imo_number_validator(imo_number: int|str, output_as_int: bool = True) -> int|str:
    """ Validates an IMO number and returns number if valid. 
    If invalid returns None. Optional to change output to strings.
    
    Args:
        imo_number (int|str): A possible IMO number.
        output_as_int (bool, optional): False to change output to strings. Defaults to True.

    Returns:
        [int|str]: An IMO number if valid.   
    """
    
    try:
        imo_int = int(imo_number)
        imo_str = str(imo_number).strip()
        
        if len(imo_str) == 7:
            imo_checksum = (int(imo_str[-7]) * 7) + \
                (int(imo_str[-6]) * 6) + \
                    (int(imo_str[-5]) * 5) + \
                        (int(imo_str[-4]) * 4) + \
                        (int(imo_str[-3]) * 3) + \
                            (int(imo_str[-2]) * 2)

            if str(imo_checksum)[-1] == imo_str[-1]:
                 return imo_int if output_as_int else imo_str
            
            else:
                pass
    
    except (ValueError, IndexError):
        pass


#########
# USAGE #
#########


imo_numbers = desired_amount(12, False)
print(imo_numbers)

imo_numbers = desired_amount(12, True)
print(imo_numbers)

validated_number = imo_number_validator('9582960', True)
print(f"Valid IMO number: {validated_number}")
print(f"Valid IMO number: {type(validated_number)}")

validated_number = imo_number_validator(9582960, False)
print(f"Valid IMO number: {validated_number}")
print(f"Valid IMO number: {type(validated_number)}")

validated_number = imo_number_validator_short(9582960, True)
print(f'Short validation {validated_number}')
print(f"Valid IMO number: {type(validated_number)}")