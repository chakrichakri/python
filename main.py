# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Chakarushipush')
# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['Policies']:
    print(i)

assert isinstance(i, object)
print(i)
print(i)
# Closing file
f.close()


print('printing just one value')
for key, value in data.items():
    print(data['Policies'])

print('printing values')
for key, value in data.items():
    print(value)

print('printing keys')
for key, value in data.items():
    print(key)

print('printing key and values')
for key, value in data.items():
    print(key, value, key)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
