import markdown
import os

def convert_markdown_to_html(input_file_path: str, output_file_path: str) -> None:
    """
    Convert a Markdown file to an HTML file.

    Parameters:
    input_file_path (str): The file path of the input Markdown file.
    output_file_path (str): The file path of the output HTML file.
    
    Raises:
    FileNotFoundError: If the input Markdown file does not exist.
    Exception: For any exceptions encountered during file read/write operations.
    """
    try:
        # Check if the input file exists
        if not os.path.exists(input_file_path):
            raise FileNotFoundError(f"The file {input_file_path} does not exist.")
        
        # Read the Markdown content from the input file
        with open(input_file_path, 'r', encoding='utf-8') as md_file:
            markdown_content = md_file.read()

        # Convert the Markdown content to HTML
        html_content = markdown.markdown(markdown_content)

        # Write the HTML content to the output file
        with open(output_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        print(f"Conversion successful: {input_file_path} -> {output_file_path}")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

def main():
    """
    Main execution block for the Markdown to HTML converter.
    """
    input_file = "example.md"  # Example input Markdown file
    output_file = "example.html"  # Example output HTML file

    convert_markdown_to_html(input_file, output_file)

if __name__ == "__main__":
    main()