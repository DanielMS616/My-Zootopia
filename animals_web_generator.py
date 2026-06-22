import json


def load_data(file_path):
    """Loads a JSON file."""

    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")

output = ""

for animal in animals_data:
    if "name" in animal:
        output += f"Name: {animal['name']}\n"

    if "characteristics" in animal:
        if "diet" in animal["characteristics"]:
            output += f"Diet: {animal['characteristics']['diet']}\n"

    if "locations" in animal:
        if len(animal["locations"]) > 0:
            output += f"Location: {animal['locations'][0]}\n"

    if "characteristics" in animal:
        if "type" in animal["characteristics"]:
            output += f"Type: {animal['characteristics']['type']}\n"

    output += "\n"


with open("animals_template.html", "r") as template_file:
    template = template_file.read()


new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w") as output_file:
    output_file.write(new_html)