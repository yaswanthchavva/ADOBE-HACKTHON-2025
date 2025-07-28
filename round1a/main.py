def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = os.path.splitext(os.path.basename(pdf_path))[0]

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                spans = line.get("spans", [])
                if not spans:
                    continue

                text = " ".join([span["text"] for span in spans]).strip()
                font_size = spans[0]["size"]
                font_flags = spans[0]["flags"]  # bold = 2

                # Combine font size + weight detection
                if font_size > 15 or (font_flags & 2):
                    level = "H1"
                elif font_size > 13:
                    level = "H2"
                elif font_size > 11:
                    level = "H3"
                else:
                    continue

                outline.append({
                    "level": level,
                    "text": text,
                    "page": page_num + 1
                })

    return {"title": title, "outline": outline}

