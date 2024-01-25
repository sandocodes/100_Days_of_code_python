# PROGRAM REQUIREMENTS:
# 1. Print report
# 2. Check resources sufficient?
# 3. Process coins
# 4. Check transaction successful?
# 5. Make Coffee
from typing import Dict

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    """Resources measured in ml"""
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

espresso_water = MENU["espresso"]["ingredients"]["water"]
latte_water = MENU["latte"]["ingredients"]["water"]
cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]

print(espresso_water + latte_water + cappuccino_water)
