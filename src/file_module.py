class FileParser:
    def __init__(self, file_path: str):
        """
        Initialize the file parser with the path to the input file.

        Args:
            file_path (str): The path to the input file.

        Returns:
            None
        """
        self.file_path = file_path

    def parse_file(self) -> tuple[list[str], list[list[str]]]:
        """
        Parse the input file to extract the header and details.

        The method reads a file specified by the file_path attribute,
        processes it to separate the header from the details, and returns
        them as a tuple.

        Returns:
            tuple[list[str], list[list[str]]]: A tuple containing the header columns
                                               and the list of detail rows.
        """
        # Open the file and read all lines
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        # Extract header from the first line, skipping the initial 'H' character
        header = lines[0].strip().split("|")[1:]

        # Extract details, filtering to include only lines starting with '|D|'
        details = [line.strip().split("|")[1:] for line in lines[1:] if line.startswith('|D|')]

        return header, details