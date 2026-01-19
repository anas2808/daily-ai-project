/**
 * Color Palette Generator
 * This program generates a color palette with a specified number of colors.
 * Each color is represented in hexadecimal format.
 * The user can specify the number of colors desired in the palette.
 */

const generateRandomColor = () => {
  // Generates a random hexadecimal color string
  const randomColor = Math.floor(Math.random() * 16777215).toString(16);
  // Pad with leading zeros if necessary to ensure it is a valid color code
  return `#${randomColor.padStart(6, '0')}`;
};

const generateColorPalette = (numColors) => {
  // Validate input to ensure it's a positive integer
  if (!Number.isInteger(numColors) || numColors <= 0) {
    throw new Error('Number of colors must be a positive integer');
  }
  const palette = [];
  for (let i = 0; i < numColors; i++) {
    palette.push(generateRandomColor());
  }
  return palette;
};

const displayColorPalette = (palette) => {
  // Log each color in the palette to the console
  console.log('Generated Color Palette:');
  palette.forEach((color, index) => {
    console.log(`Color ${index + 1}: ${color}`);
  });
};

const main = () => {
  try {
    const numColors = 5; // Number of colors to generate in the palette
    const colorPalette = generateColorPalette(numColors);
    displayColorPalette(colorPalette);
  } catch (error) {
    console.error('Error generating color palette:', error.message);
  }
};

// Execute the main function to run the program
main();