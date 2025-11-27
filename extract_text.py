import os
from pathlib import Path
from mistralai import Mistral, DocumentURLChunk
from mistralai.models import OCRResponse
import re


api_key="F3wOdUN6pO0nBJCC3NC3thYCH7EwHNQ0"
client = Mistral(api_key=api_key)
print('API connected')

def get_combined_markdown(ocr_response: OCRResponse, filename: str = None) -> str:
    # function to convert OCR data to markdown
    markdowns: list[str] = []
    for page in ocr_response.pages:
        page_markdown = page.markdown
        page_markdown = re.sub(r'!\[.*?\]\(.*?\)', '[Image removed]', page_markdown)
        markdowns.append(page_markdown)
    return "\n\n".join(markdowns)

def process_pdf_file(pdf_path: Path, output_path: Path):
    # function that processes a single PDF file
    if output_path.exists():
        return False
    
    uploaded_file = client.files.upload(
        file={
            "file_name": pdf_path.stem,
            "content": pdf_path.read_bytes(),
        },
        purpose="ocr",
    )
    
    signed_url = client.files.get_signed_url(file_id=uploaded_file.id, expiry=1)
    
    pdf_response = client.ocr.process(
        document=DocumentURLChunk(document_url=signed_url.url),
        model="mistral-ocr-latest",
        include_image_base64=False
    )
    
    combined_markdown = get_combined_markdown(pdf_response, filename=pdf_path.stem)
    
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(combined_markdown)
    
    return True

def process_all_pdfs():
    # function that processes PDF files in the data directory
    pdf_dir = Path("data")
    markdown_dir = Path("markdown DS")
    
    # Find all PDF files in data directory and subdirectories
    pdf_files = list(pdf_dir.rglob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in data directory!")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s) to process\n")
    print("="*60)
    
    processed_count = 0
    skipped_count = 0
    error_count = 0
    
    for idx, pdf_path in enumerate(pdf_files, 1):
        # Calculate relative path from PDF DATASET directory
        relative_path = pdf_path.relative_to(pdf_dir)
        
        # Create corresponding markdown path
        output_path = markdown_dir / relative_path.with_suffix(".md")
        
        # Print detailed progress
        print(f"\n[{idx}/{len(pdf_files)}] File: {pdf_path.name}")
        print(f"    Source: {relative_path}")
        print(f"    Output: {output_path.relative_to(Path('.'))}")
        
        try:
            result = process_pdf_file(pdf_path, output_path)
            if result:
                print(f"    Status: ✓ Successfully processed")
                processed_count += 1
            else:
                print(f"    Status: ⊘ Skipped (already exists)")
                skipped_count += 1
        except Exception as e:
            print(f"    Status: ✗ Error - {str(e)}")
            error_count += 1
        
        print("-"*60)
    
    # Print summary
    print("\n" + "="*60)
    print(f"SUMMARY:")
    print(f"  Total files found: {len(pdf_files)}")
    print(f"  Processed: {processed_count}")
    print(f"  Skipped (already exists): {skipped_count}")
    print(f"  Errors: {error_count}")
    print("="*60)
    print("\n✓ All PDF files processed!")


if __name__ == "__main__":
    process_all_pdfs()