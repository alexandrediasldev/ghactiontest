from simple import say
import os
def main():
    with open(os.path.realpath(os.path.dirname(__file__))+'/package_data.dat') as f:
        say(f.read())