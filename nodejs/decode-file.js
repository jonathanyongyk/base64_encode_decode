const fs = require('fs');

// Parse named arguments
function parseArgs(args) {
    const parsed = {};
    for (let i = 0; i < args.length; i++) {
        if (args[i] === '--input' && i + 1 < args.length) {
            parsed.input = args[++i];
        } else if (args[i] === '--output' && i + 1 < args.length) {
            parsed.output = args[++i];
        }
    }
    return parsed;
}

const args = parseArgs(process.argv.slice(2));

if (!args.input || !args.output) {
    console.error('Usage: node decode-file.js --input <input-file> --output <output-file>');
    console.error('Sample call: node decode-file.js --input "file_encoded.txt" --output "file.zip"');
    process.exit(1);
}

const inputFile = args.input;
const outputFile = args.output;

// Check if the input file exists
if (!fs.existsSync(inputFile)) {
    console.error(`Error: File "${inputFile}" not found.`);
    process.exit(1);
}

try {
    // Read the base64 encoded text file
    const base64Text = fs.readFileSync(inputFile, 'utf8').trim();
    
    // Decode the base64 content to binary
    const decodedBuffer = Buffer.from(base64Text, 'base64');
    
    // Save the decoded binary to the output file
    fs.writeFileSync(outputFile, decodedBuffer);
    
    console.log(`Successfully decoded "${inputFile}"`);
    console.log(`Output saved to: "${outputFile}"`);
    console.log(`Encoded size: ${base64Text.length} characters`);
    console.log(`Decoded size: ${decodedBuffer.length} bytes`);
} catch (error) {
    console.error(`Error processing file: ${error.message}`);
    process.exit(1);
}
