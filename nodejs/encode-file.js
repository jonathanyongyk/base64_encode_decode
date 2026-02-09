const fs = require('fs');
const path = require('path');

// Get the input file from command line arguments
const inputFile = process.argv[2];

if (!inputFile) {
    console.error('Usage: node encode-file.js <input-file>');
    process.exit(1);
}

// Check if the input file exists
if (!fs.existsSync(inputFile)) {
    console.error(`Error: File "${inputFile}" not found.`);
    process.exit(1);
}

try {
    // Read the file in binary mode
    const fileBuffer = fs.readFileSync(inputFile);
    
    // Base64 encode the contents
    const base64Encoded = fileBuffer.toString('base64');
    
    // Generate output file name (same name with .txt extension)
    const baseName = path.basename(inputFile, path.extname(inputFile));
    const outputFile = path.join(path.dirname(inputFile), `${baseName}_encoded.txt`);
    
    // Save the encoded text to the output file
    fs.writeFileSync(outputFile, base64Encoded, 'utf8');
    
    console.log(`Successfully encoded "${inputFile}"`);
    console.log(`Output saved to: "${outputFile}"`);
    console.log(`Original size: ${fileBuffer.length} bytes`);
    console.log(`Encoded size: ${base64Encoded.length} characters`);
} catch (error) {
    console.error(`Error processing file: ${error.message}`);
    process.exit(1);
}
