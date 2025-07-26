# 📑 Round 1B — Persona-Driven Document Intelligence

## 🔍 Overview

This project is my submission for **Round 1B** of the **Adobe India Hackathon 2025**.  
It acts as an intelligent document analyst that processes a collection of PDF documents, extracting and ranking the most relevant sections for a specific **persona** and **job-to-be-done**.

---

## ✅ Approach Summary

- **Library used:** [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (`fitz` in Python)
- The script loops through **all PDFs** in `/app/input` automatically.
- Each page is scanned for text blocks.
- Relevance is scored by matching **job keywords** in text spans.
- Sections with the highest relevance are ranked and added to the **extracted sections** list.
- Subsections reuse the same content for baseline but can be enhanced further.

---

## ✅ Requirements Met

- ✅ Runs **fully offline** — no internet calls
- ✅ CPU only — no large models, only PyMuPDF (~20MB)
- ✅ Handles multiple PDFs in a loop
- ✅ Model size far below **1 GB**
- ✅ Finishes in under **60 seconds** for typical 3–5 docs
- ✅ Output matches the expected JSON structure with:
  - Metadata (docs, persona, job, timestamp)
  - Extracted sections with importance rank
  - Sub-section analysis

---

## 📂 Project Structure

```plaintext
round1b_persona_intelligence/
 ├── extractor.py
 ├── Dockerfile
 ├── persona_job.json
 ├── input/           # Put your sample PDFs here
 ├── output/          # Result JSON goes here (ignored in .gitignore)
 ├── README.md
 ├── approach_explanation.md
 ├── .gitignore
```
