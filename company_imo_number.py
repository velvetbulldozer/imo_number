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


def comp_imo_number_validator(comp_imo_number: int|str, output_as_int: bool = True) -> int|str:
    """ Validates a Company IMO number and returns number if valid.
    If invalid returns None. Optional to change output to strings.

    Args:
        comp_imo_number (int|str): A possible IMO number.
        output_as_int (bool, optional): False to change output to strings. Defaults to True.

    Returns:
        [int|str]: An IMO number if valid.
    """
    try:
        comp_int = int(comp_imo_number)
        comp_str = str(comp_imo_number).strip()

        if len(comp_str) == 7:
            check_digit_temp = (11 - (int(comp_str[-7]) * 8 \
                + int(comp_str[-6]) * 6 \
                    + int(comp_str[-5]) * 4 \
                        + int(comp_str[-4]) * 2 \
                            + int(comp_str[-3]) * 9 \
                                + int(comp_str[-2]) * 7) % 11) % 10

            check_digit = 11 - check_digit_temp % 10

            if str(check_digit) == comp_str[-1]:

                if output_as_int:
                    return comp_int

                else:
                    return comp_str

            else:
                pass
        else:
            pass
    except (ValueError, IndexError) as e:
        pass


#########
# USAGE #
#########


validated_number = comp_imo_number_validator(9074729, True)
print(f"Valid company IMO number: {validated_number}")

validated_number = comp_imo_number_validator('9074729', True)
print(f"Valid company IMO number: {validated_number}")