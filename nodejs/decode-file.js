const fs = require('fs');

// Get the input and output files from command line arguments
const inputFile = process.argv[2];
const outputFile = process.argv[3];

if (!inputFile || !outputFile) {
    console.error('Usage: node decode-file.js <input-file> <output-file>');
    process.exit(1);
}

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
