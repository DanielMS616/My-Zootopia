import json


def load_data(file_path):
    """Loads a JSON file."""

    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Converts one animal object into HTML"""

    output = ""
    output += '<li class="cards__item">\n'

    if "name" in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'

    output += '  <div class="card__text">\n'
    output += '    <ul class="card__list">\n'

    if "characteristics" in animal_obj:
        if "diet" in animal_obj["characteristics"]:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Diet:</strong> '
                f'{animal_obj["characteristics"]["diet"]}</li>\n'
            )

    if "locations" in animal_obj:
        if len(animal_obj["locations"]) > 0:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Location:</strong> '
                f'{animal_obj["locations"][0]}</li>\n'
            )

    if "characteristics" in animal_obj:
        if "type" in animal_obj["characteristics"]:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Type:</strong> '
                f'{animal_obj["characteristics"]["type"]}</li>\n'
            )

    if "characteristics" in animal_obj:
        if "lifespan" in animal_obj["characteristics"]:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Lifespan:</strong> '
                f'{animal_obj["characteristics"]["lifespan"]}</li>\n'
            )

    if "characteristics" in animal_obj:
        if "weight" in animal_obj["characteristics"]:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Weight:</strong> '
                f'{animal_obj["characteristics"]["weight"]}</li>\n'
            )

    if "characteristics" in animal_obj:
        if "top_speed" in animal_obj["characteristics"]:
            output += (
                f'      <li class="card__list-item">'
                f'<strong>Top Speed:</strong> '
                f'{animal_obj["characteristics"]["top_speed"]}</li>\n'
            )

    output += "    </ul>\n"
    output += "  </div>\n"
    output += "</li>\n"

    return output


animals_data = load_data("animals_data.json")

output = ""

for animal in animals_data:
    output += serialize_animal(animal)

with open("animals_template.html", "r", encoding="utf-8") as template_file:
    template = template_file.read()

new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as output_file:
    output_file.write(new_html)