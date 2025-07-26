import fitz  # PyMuPDF
import os
import json
from datetime import datetime

# Simple keyword matching scorer
def score_text(text, keywords):
    score = 0
    for kw in keywords:
        if kw.lower() in text.lower():
            score += 1
    return score

def process_pdfs(input_dir, persona_job):
    output = {
        "metadata": {
            "input_documents": [],
            "persona": persona_job["persona"],
            "job_to_be_done": persona_job["job_to_be_done"],
            "processing_timestamp": datetime.utcnow().isoformat() + "Z"
        },
        "extracted_sections": [],
        "sub_section_analysis": []
    }

    keywords = persona_job["job_to_be_done"].split()

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            output["metadata"]["input_documents"].append(filename)
            doc = fitz.open(os.path.join(input_dir, filename))

            # Score sections by page
            for page_num, page in enumerate(doc, start=1):
                blocks = page.get_text("blocks")
                for b in blocks:
                    text = b[4].strip()
                    if len(text) > 50:
                        relevance = score_text(text, keywords)
                        if relevance > 0:
                            output["extracted_sections"].append({
                                "document": filename,
                                "page_number": page_num,
                                "section_title": text[:50] + "...",
                                "importance_rank": relevance
                            })
                            # Also add to sub-section (dummy same text for baseline)
                            output["sub_section_analysis"].append({
                                "document": filename,
                                "page_number": page_num,
                                "refined_text": text
                            })

    # Sort by rank
    output["extracted_sections"] = sorted(output["extracted_sections"], key=lambda x: -x["importance_rank"])[:5]

    return output


if __name__ == "__main__":
    input_dir = "/app/input"
    output_dir = "/app/output"

    with open("persona_job.json") as f:
        persona_job = json.load(f)

    result = process_pdfs(input_dir, persona_job)

    with open(os.path.join(output_dir, "result.json"), "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print("✅ Extraction done.")
