import json


def load_data(file_path):
    """Loads a JSON file."""

    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")

output = ""

for animal in animals_data:
    output += '<li class="cards__item">\n'

    if "name" in animal:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    if "characteristics" in animal:
        if "diet" in animal["characteristics"]:
            output += f'    <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

    if "locations" in animal:
        if len(animal["locations"]) > 0:
            output += f'    <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    if "characteristics" in animal:
        if "type" in animal["characteristics"]:
            output += f'    <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

    output += "  </p>\n"
    output += "</li>\n"


with open("animals_template.html", "r", encoding="utf-8") as template_file:
    template = template_file.read()


new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w", encoding="utf-8") as output_file:
    output_file.write(new_html)