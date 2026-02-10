import sys
import os
import base64
import argparse


def decode_file(input_file, output_file):
    """Decode a base64-encoded text file back to its original binary form.

    Args:
        input_file: Path to the base64-encoded text file.
        output_file: Path to save the decoded binary output.

    Returns:
        A dict with 'input_file', 'output_file', 'encoded_size', and 'decoded_size'.

    Raises:
        FileNotFoundError: If the input file does not exist.
        IOError: If reading or writing fails.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f'File "{input_file}" not found.')

    # Read the base64 encoded text file
    with open(input_file, 'r', encoding='utf-8') as f:
        base64_text = f.read().strip()

    # Decode the base64 content to binary
    decoded_data = base64.b64decode(base64_text)

    # Save the decoded binary to the output file
    with open(output_file, 'wb') as f:
        f.write(decoded_data)

    return {
        'input_file': input_file,
        'output_file': output_file,
        'encoded_size': len(base64_text),
        'decoded_size': len(decoded_data),
    }


def main():
    parser = argparse.ArgumentParser(
        description='Decode a base64-encoded text file back to its original binary form.',
        epilog='Sample call: python decode-file.py --input photo_encoded.txt --output photo_restored.png',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('--input', required=True, help='Path to the base64-encoded text file.')
    parser.add_argument('--output', required=True, help='Path to save the decoded output file.')
    args = parser.parse_args()

    try:
        result = decode_file(args.input, args.output)
        print(f'Successfully decoded "{result["input_file"]}"')
        print(f'Output saved to: "{result["output_file"]}"')
        print(f'Encoded size: {result["encoded_size"]} characters')
        print(f'Decoded size: {result["decoded_size"]} bytes')
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
