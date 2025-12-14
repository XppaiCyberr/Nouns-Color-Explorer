# Nouns Color Explorer

A beautiful, interactive tool to explore [Nouns](https://nouns.wtf) by their color palette. This project allows users to search for Nouns that match specific colors, with advanced filtering and visualization options.

## Preview
<img width="1134" height="918" alt="image" src="https://github.com/user-attachments/assets/44684ca0-3df4-48d4-8f79-71003bc43993" />


## Features

- **🎨 Color Search:** Enter a Hex code or use the visual color picker to find Nouns containing that color.
- **🎚️ Fuzzy Matching:** Use the **Color Tolerance** slider to find Nouns with similar shades, not just exact matches.
- **📊 Advanced Sorting:**
  - **Match Strength:** Sort by how well the Noun matches your target color.
  - **Brightest / Darkest:** Discover Nouns with high or low average luminance.
  - **Most / Least Colorful:** Find Nouns with complex or simple palettes.
- **🔍 Detailed Insights:** Click on any Noun to see a complete breakdown of its color palette, including pixel counts and percentages.
- **⚡ Fast & Local:** Runs entirely in the browser using a pre-processed dataset (`noun_colors_extracted.json`).

## How to Use

1.  Clone this repository or download the files.
2.  Open `index.html` in your web browser.
3.  **Start Exploring:**
    - Pick a color using the color picker.
    - Adjust the tolerance slider to broaden your search.
    - Use the dropdown to sort results by brightness or colorfulness.

## Project Structure

- `index.html`: The main application file containing the UI, styling (CSS), and logic (JavaScript).
- `noun_colors_extracted.json`: A JSON dataset mapping Noun IDs to their constituent colors and pixel counts.
- `extract_colors.py` / `append_noun_colors.py`: Python scripts used to generate the color dataset from Noun images.

## Technologies

- **HTML5 & CSS3:** Modern, responsive design using CSS variables and Flexbox/Grid.
- **Vanilla JavaScript:** Efficient DOM manipulation and color calculation logic (no frameworks required).
- **Inter Font:** Typography served via Google Fonts.

## Credits

- **Nouns DAO:** All Noun images are CC0 and sourced from [noun.pics](https://noun.pics).
- **Font:** [Inter](https://rsms.me/inter/) by Rasmus Andersson.

---

*Built for the Nouns community.* ⌐◨-◨
