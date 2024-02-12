import os


def _create_path(filename: str) -> str:
    """
    Create a path by joining the `FILES_PATH` with the given `filename`.
    
    Args:
        filename (str): The name of the file.
        
    Returns:
        str: The complete path of the file.
    """
    path = os.path.join(FILES_PATH, filename)
    return path


FILES_PATH = os.path.dirname(__file__) + "/files"
PDF_PATH = _create_path("test.pdf")
PNG_PATH = _create_path("test.png")