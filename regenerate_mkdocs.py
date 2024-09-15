import logging

template_file = "mkdocs_template.yml"
output_file = "mkdocs.yml"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

with open(template_file, "r") as file:
	template_content = file.read()

# We can automate the generation of mkdocs.yml content here as needed.
final_content = template_content

with open(output_file, "w") as file:
	file.write(final_content)

logging.info("Generated mkdocs.yml")
