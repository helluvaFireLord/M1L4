import random
import discord
from discord.ext import commands

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
def coin():
    flip = random.randint(0, 1)
    if (flip == 0):
        print("Орел")
    else:
        print("Решка")
