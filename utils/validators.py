import re

COORDINATE_PATTERN = r"^(\d+)x(\d+)$"

def validate_coordinate(text):
    return re.match(COORDINATE_PATTERN, text)