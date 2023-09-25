import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--name', type=str, default='Lee', help='Name (default: Lee)')
parser.add_argument('--age', type=int, default=5, help='Age (default: 5)')
parser.add_argument('--height', type=float, default=6.0, help='Height in feet (default: 6.0)')

args = parser.parse_args()

name = args.name
age = args.age
height = args.height

print(f'Name: {name}')
print(f'Age: {age}')
print(f'Height: {height}')

# python main.py --name Lee --age 5 --height 6.0

