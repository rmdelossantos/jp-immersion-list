import os
import json

def get_all_folders():
    return [folder for folder in os.listdir('.') if os.path.isdir(folder)]

def json_file_exists(category):
    file_path = os.path.join(category, f'{category}.json')
    return os.path.exists(file_path)

def read_json_file(category):
    file_path = os.path.join(category, f'{category}.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
    else:
        return []

def generate_table(category, category_data):
    table = f"\n## {category.capitalize()}\n\n"
    table += "| Name | Author / Studio | Link | Description |\n"
    table += "|------|------------------|------|-------------|\n"

    for item in category_data:
        table += f"| {item['name']} | {item['author']} | {item['link']} | {item['description']} |\n"

    return table


intro_paragraph = (
    "Welcome to my Japanese Immersion List – a curated collection of resources that accompany my language learning journey. "
    "Embarking on the path of mastering Japanese, I've gathered an assortment of books, manga, anime, and more, "
    "to aid in my immersion experience.!\n\n"
)
readme_content = f"# Japanese Immersion List\n\n{intro_paragraph}"
folders = get_all_folders()
for category in folders:
    if json_file_exists(category):
        category_data = read_json_file(category)
        readme_content += generate_table(category, category_data)

with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)

print("README.md generated successfully!")
