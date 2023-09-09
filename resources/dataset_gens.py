import json

# Initialize an empty list to store dictionaries
dialogue_list = []

# Read the text file
with open('parsed_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

with open('dataset_spanish.json', 'r', encoding='utf-8') as file2:
    data2 = json.load(file2)

# Initialize variables to store index and dialogue
index = None
dataset = []

i = 1
for d in data:
    val = {"id":f"{i}","dialogue":d["dialogue"],"summary":data2[f'{i}']}
    dataset.append(val)
    i = i + 1

with open('spanish_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(dataset, json_file, ensure_ascii=False, indent=4)

print("Data saved to 'spanish_data.json'.")

