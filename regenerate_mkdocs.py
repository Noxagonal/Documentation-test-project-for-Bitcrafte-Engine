import os
import logging
from dotenv import load_dotenv

template_file = "mkdocs_template.yml"
output_file = "mkdocs.yml"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# see if ENGINE_REPO_DIR is set, if not, load .env file
engine_repo_dir = os.getenv('ENGINE_REPO_DIR')
if engine_repo_dir is None:
	load_dotenv()
	engine_repo_dir = os.getenv('ENGINE_REPO_DIR')

if engine_repo_dir is None:
	raise Exception("ENGINE_REPO_DIR is not set anywhere")

with open(template_file, "r") as file:
	template_content = file.read()

final_content = template_content.replace("{{ENGINE_REPO_DIR}}", engine_repo_dir)

with open(output_file, "w") as file:
	file.write(final_content)

logging.info(f"Generated mkdocs.yml with ENGINE_REPO_DIR = {engine_repo_dir}")
