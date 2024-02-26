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
    table = f"<h2>{category.capitalize()}</h2>"
    table += '<div style="overflow-x: auto;">'
    table += "<table>\n"
    table += "    <thead>\n"
    table += "        <tr>\n"
    table += "            <th>Name</th>\n"
    table += "            <th>Author / Studio</th>\n"
    table += "            <th>Description</th>\n"
    table += "        </tr>\n"
    table += "    </thead>\n"
    table += "    <tbody>\n"

    for item in category_data:
        table += f"        <tr>\n"
        table += f"            <td>{item['name']}</td>\n"
        table += f"            <td><a href=\"{item['link']}\">{item['author']}</a></td>\n"
        table += f"            <td>{item['description']}</td>\n"
        table += "        </tr>\n"

    table += "    </tbody>\n"
    table += "</table>\n"
    table += '</div>'
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
