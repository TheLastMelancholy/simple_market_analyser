import os
import argparse
import json

def parse_arguments():
    parser = argparse.ArgumentParser(description='Create folders layout for some asset.')

    parser.add_argument('token', metavar='T', type=str, nargs='+',
                    help='token to make directories layout')

    args = parser.parse_args()
    # print(args.token)
    return args.token[0]

def create_init_json(dir_path, token):
    token_descriptor_path = os.path.join(dir_path, token+".json")
    with open(token_descriptor_path, "w") as tokenfile:
        json.dump({"TOKEN":token, "LAST_UPDATED":None}, tokenfile)


token = parse_arguments()
root_directory = os.getcwd()
target_directory = os.path.join(root_directory, token)

if os.path.isdir(target_directory):
    print("Asset already registered")
else:
    os.mkdir(target_directory)
    create_init_json(target_directory, token)
