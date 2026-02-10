import sys
import os
import base64
import argparse


def encode_file(input_file, output_file=None):
    """Base64 encode a file and save the result to a text file.

    Args:
        input_file: Path to the file to encode.
        output_file: Path to save the encoded output. If None, generates
                     a name based on the input file (e.g. foo_encoded.txt).

    Returns:
        A dict with 'input_file', 'output_file', 'original_size', and 'encoded_size'.

    Raises:
        FileNotFoundError: If the input file does not exist.
        IOError: If reading or writing fails.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f'File "{input_file}" not found.')

    # Read the file in binary mode
    with open(input_file, 'rb') as f:
        file_data = f.read()

    # Base64 encode the contents
    base64_encoded = base64.b64encode(file_data).decode('utf-8')

    # Generate output file name if not provided
    if output_file is None:
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(os.path.dirname(input_file) or '.', f'{base_name}_encoded.txt')

    # Save the encoded text to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(base64_encoded)

    return {
        'input_file': input_file,
        'output_file': output_file,
        'original_size': len(file_data),
        'encoded_size': len(base64_encoded),
    }


def main():
    parser = argparse.ArgumentParser(
        description='Base64 encode a file and save the encoded output to a text file.',
        epilog='Sample call: python encode-file.py --input photo.png --output photo_encoded.txt',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('--input', required=True, help='Path to the file to encode.')
    parser.add_argument(
        '--output',
        default=None,
        help='Path for the output encoded text file. '
             'Defaults to <basename>_encoded.txt in the same directory as the input.',
    )
    args = parser.parse_args()

    try:
        result = encode_file(args.input, args.output)
        print(f'Successfully encoded "{result["input_file"]}"')
        print(f'Output saved to: "{result["output_file"]}"')
        print(f'Original size: {result["original_size"]} bytes')
        print(f'Encoded size: {result["encoded_size"]} characters')
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
