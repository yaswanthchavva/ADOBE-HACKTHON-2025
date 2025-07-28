# Challenge 1A: PDF Document Outline Extractor

## 🧠 Overview
This solution solves **Round 1A** of the Adobe India Hackathon 2025.  
The goal is to analyze the structure of PDF documents and extract section-level outlines (like H1, H2, H3) based on font sizes using **PyMuPDF**.

The project is fully containerized using **Docker** and processes all `.pdf` files placed in the `input/` directory, generating structured `.json` outlines in the `output/` directory.

---

## 📁 Project Structure

round1a/
├── input/
│ ├── file01.pdf
│ ├── file02.pdf
│ └── file03.pdf
├── output/
│ ├── file01.json
│ ├── file02.json
│ └── file03.json
├── main.py
├── Dockerfile
├── requirements.txt
└── README.md

---

## 🔍 PDF Outline Extraction Logic

- Extracts visible text from each page
- Uses font size thresholds to classify heading levels:
  - `H1` → font size ≥ 16
  - `H2` → font size ≥ 13
  - `H3` → font size ≥ 11
- Outputs JSON with structured outline:
  - Title of the document (from filename)
  - List of headings with levels and page numbers

---

## 📥 Input

- Drop your `.pdf` files in the `input/` directory.
- No changes to filenames required.

---

## 📤 Output

Each `.pdf` generates a corresponding `.json` in `output/`, like this:

```json
{
  "title": "file01",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
