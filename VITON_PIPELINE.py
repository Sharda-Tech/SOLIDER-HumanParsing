import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter
import os
import random
import shutil

def execute_notebook(notebook_path, output_path=None):
    with open(notebook_path) as nb_file:
        notebook = nbformat.read(nb_file, as_version=4)

    # Create an ExecutePreprocessor instance
    executor = ExecutePreprocessor(timeout=-1)  # Set timeout to -1 for no timeout

    # Execute the notebook
    executor.preprocess(notebook, {'metadata': {'path': '.'}})

    # Export the executed notebook to HTML (optional)
    if output_path:
        exporter = HTMLExporter()
        output, _ = exporter.from_notebook_node(notebook)
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(output)

if __name__ == "__main__":
    # Set the paths to the image and cloth folders
    image_folder_path = "/home/ubuntu/test/image"
    cloth_folder_path = "/home/ubuntu/test/cloth"

    # Get a list of image files in the image folder
    image_files = [f for f in os.listdir(image_folder_path) if os.path.isfile(os.path.join(image_folder_path, f))]

    # Get a list of cloth files in the cloth folder
    cloth_files = [f for f in os.listdir(cloth_folder_path) if os.path.isfile(os.path.join(cloth_folder_path, f))]

    # Set the paths for the destination images
    output_folder = "/home/ubuntu/images"
    os.makedirs(output_folder, exist_ok=True)

    for sequential_image in image_files:
        # Choose a cloth file from the cloth folder randomly
        random_cloth = random.choice(cloth_files)

        # Set the paths for the destination images
        person_image_path = os.path.join(output_folder, "person.jpeg")
        cloth_image_path = os.path.join(output_folder, "cloth.jpeg")

        # Copy the selected images to the destination paths
        shutil.copyfile(os.path.join(image_folder_path, sequential_image), person_image_path)
        shutil.copyfile(os.path.join(cloth_folder_path, random_cloth), cloth_image_path)
        exit()

    print("Images saved successfully.")
    
    
    
    notebook_path = "/home/ubuntu/VITON_HD_PIPELINE.ipynb"
    output_html_path = "./output.html"  # Optional

    execute_notebook(notebook_path, output_html_path)
