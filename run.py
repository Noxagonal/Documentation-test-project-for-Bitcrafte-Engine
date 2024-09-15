import sys
import logging
import asyncio
import subprocess
import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Path to the mkdocs_template.yml and scripts
template_file = "mkdocs_template.yml"
regenerate_script = "regenerate_mkdocs.py"
mkdocs_serve_command = ["mkdocs", "serve"]

# Global variable to hold the mkdocs process
mkdocs_process: asyncio.subprocess.Process = None

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def regenerate_mkdocs():
	subprocess.run(["python", regenerate_script])

# Asynchronously capture the output from the mkdocs serve process
async def stream_stdout(process: asyncio.subprocess.Process):
	while True:
		line = await process.stdout.readline()
		if not line:
			break
		print(line.decode(), end="")

# Asynchronously capture the output from the mkdocs serve process
async def stream_stderr(process: asyncio.subprocess.Process):
	while True:
		line = await process.stderr.readline()
		if not line:
			break
		print(line.decode(), end="")

# Function to run mkdocs serve and stream output asynchronously
async def start_mkdocs():
	global mkdocs_process

	logging.info("Starting mkdocs...")
	mkdocs_process = await asyncio.create_subprocess_exec(
		*mkdocs_serve_command,
		stdout=asyncio.subprocess.PIPE,
		stderr=asyncio.subprocess.PIPE
	)

	await asyncio.gather(
		stream_stdout(mkdocs_process), # stdout
		stream_stderr(mkdocs_process)  # stderr
	)

# Function to stop and terminate the mkdocs process
async def stop_mkdocs():
	global mkdocs_process

	if mkdocs_process is None:
		return
	logging.info("Stopping mkdocs...")
	mkdocs_process.terminate()
	await mkdocs_process.wait()
	mkdocs_process = None

# Handler for detecting changes in the mkdocs template file
class MkdocsTemplateChangeHandler(FileSystemEventHandler):
	def __init__(self):
		super().__init__()

	def on_modified(self, event):
		if event.src_path.endswith(template_file):
			logging.info(f"{template_file} has been modified.")
			regenerate_mkdocs()

async def run_main():
	event_handler = MkdocsTemplateChangeHandler()

	# Set up the observer to monitor the file updates
	observer: watchdog.observers.Observer = Observer()
	observer.schedule(event_handler, ".", recursive=False)  # "." is the directory to watch

	# Set up the observer to monitor the file
	try:
		observer.start()
		logging.info(f"Watching {template_file} for changes...")

		# Run the script to regenerate the initial mkdocs file
		regenerate_mkdocs()

		await start_mkdocs()
		while True:
			await asyncio.sleep(1)

	except KeyboardInterrupt:
		logging.info("Interrupted, stopping...")

	except asyncio.exceptions.CancelledError:
		logging.info("Interrupted, stopping...")

	except:
		logging.exception("Unexpected error occurred")
		raise

	finally:
		logging.info("Shutting down...")
		await stop_mkdocs()
		observer.stop()
		observer.join()

if __name__ == "__main__":
	asyncio.run(run_main())
	logging.info("Finished")
