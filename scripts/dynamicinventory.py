#!/usr/bin/python3

#accept command from the cli
import argparse

#we want to work with JSON
import json

def main():
    inventory = {} #creating a dictionary called inventory
    if args.list: #if a user pass --list to our script
        inventory = example_inventory() #run the function example_inventory
    elif args.host: #not implemented, if a user passes --host to our script
        inventory = empty_inventory()
    else:
        inventory = empty_inventory()

    print(json.dumps(inventory))


#this would actually be our auditing logic
def example_inventory():
    return {
        'group': {
            'hosts': ['centurylink-webservers']
            },
        '_meta': {
            'hostvars': {
                'centurylink-webservers': {
                    'ansible_connection': 'local',
                    'ansible_host': 'localhost'
                        }
                    }
                }
            }

def empty_inventory():
    return {}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action = 'store_true')
    parser.add_argument('--host', action = 'store')
    args = parser.parse_args()
    main() 
