import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter

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
    notebook_path = "/home/ubuntu/VITON_HD_PIPELINE.ipynb"
    output_html_path = "./output.html"  # Optional

    execute_notebook(notebook_path, output_html_path)
