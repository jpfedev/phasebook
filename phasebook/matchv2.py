import time
import random
from flask import Blueprint

bp = Blueprint("matchv2", __name__, url_prefix="/matchv2")
matched = []

@bp.route("<int:match_id>")
def match(match_id):
    numbers_2 = []
    for i in range(5):
        numberr = random.randint(1,15)
        while numberr in numbers_2:
            numberr = random.randint(1,15)
        numbers_2.append(numberr)
    if match_id < 0 or match_id > 15:
        return "Invalid match id", 404

    start = time.time()
    msg = f"Matched found! Favorite number list are: {numbers_2}, Your favorite number is: [{match_id}]" if (is_match(numbers_2,[match_id])) else f"Did not matched! Your number was [{match_id}], The favorite number list was {numbers_2}"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    for number in fave_numbers_1:
        if number in fave_numbers_2:
            matched.append(number)
            return True
