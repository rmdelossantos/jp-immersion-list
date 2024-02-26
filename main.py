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

def generate_table(item):
    table = f"| {item['name']} | {item['author']} | {item['description']} |\n"
    return table

def generate_accordion(category, category_data):
    accordion = f"\n## {category.capitalize()} \n\n"
    accordion += f'<div class="accordion" id="{category}Accordion">\n'

    accordion += f'  <div class="accordion-item">\n'
    accordion += f'    <h2 class="accordion-header" id="{category}Heading">\n'
    accordion += f'      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#{category}Collapse" aria-expanded="true" aria-controls="{category}Collapse">\n'
    accordion += f'        {category.capitalize()}\n'
    accordion += f'      </button>\n'
    accordion += f'    </h2>\n'
    accordion += f'    <div id="{category}Collapse" class="accordion-collapse collapse show" aria-labelledby="{category}Heading" data-bs-parent="#{category}Accordion">\n'
    accordion += f'      <div class="accordion-body">\n'
    accordion += f'        <table>\n'
    accordion += f'          <thead>\n'
    accordion += f'            <tr>\n'
    accordion += f'              <th>Name</th>\n'
    accordion += f'              <th>Author / Studio</th>\n'
    accordion += f'              <th>Description</th>\n'
    accordion += f'            </tr>\n'
    accordion += f'          </thead>\n'
    accordion += f'          <tbody>\n'

    for idx, item in enumerate(category_data):
        accordion += f'            <tr>\n'
        accordion += f'              <td>{item["name"]}</td>\n'
        accordion += f'              <td><a href="{item["link"]}">{item["author"]}</a></td>\n'
        accordion += f'              <td>{item["description"]}</td>\n'
        accordion += f'            </tr>\n'

    accordion += f'          </tbody>\n'
    accordion += f'        </table>\n'
    accordion += f'      </div>\n'
    accordion += f'    </div>\n'
    accordion += f'  </div>\n'

    accordion += '</div>\n'
    return accordion



intro_paragraph = (
    "Welcome to my Japanese Immersion List – a curated collection of resources that accompany my language learning journey. "
    "Embarking on the path of mastering Japanese, I've gathered an assortment of books, manga, anime, and more, "
    "to aid in my immersion experience!\n\n"
)
readme_content = f"# Japanese Immersion List\n\n{intro_paragraph}"
folders = get_all_folders()
for category in folders:
    if json_file_exists(category):
        category_data = read_json_file(category)
        readme_content += generate_accordion(category, category_data)

# Add Bootstrap CDN links for the accordion to the README content
readme_content += """
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-eMhCn3h/5pdmx1XQjDEtWsdI9Pq8Erdzgqy5U9XfRfOWd51t6Q6FvJgDR6YFy7bp" crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" integrity="sha384-GLhlTQ8iK7t5Lbr5NrZ5YgzHA5ekPSSWx1+evLhFhS6z4M5b83L2KfGiJdA2Q8D" crossorigin="anonymous">
"""

with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)

print("README.md generated successfully!")
