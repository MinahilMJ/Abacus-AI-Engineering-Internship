import os
import fitz

def extract_text_from_pdf(file_path):
    pages=[]

    document=fitz.open(file_path)

    for page_number,page in enumerate(document):
        text=page.get_text()

        if text.strip():
            pages.append({
                "text":text.strip(),
                "page":page_number+1
            })

    document.close()

    return pages

def extract_text_from_txt(file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        text=file.read()

    return [
        {
            "text":text.strip(),
            "page":None
        }
    ]

def extract_text(file_path):
    extension=os.path.splitext(file_path)[1].lower()

    if extension==".pdf":
        return extract_text_from_pdf(file_path)

    if extension==".txt":
        return extract_text_from_txt(file_path)

    raise ValueError("Only PDF and TXT files are supported")

def create_chunks(pages,source,chunk_size=500,overlap=50):
    chunks=[]

    for page in pages:
        text=page["text"]
        page_number=page["page"]

        start=0
        chunk_number=0

        while start<len(text):
            end=start+chunk_size

            chunk_text=text[start:end].strip()

            if chunk_text:
                chunks.append({
                    "text":chunk_text,
                    "metadata":{
                        "source":source,
                        "page":page_number,
                        "chunk_id":f"{source}_{page_number}_{chunk_number}"
                    }
                })

            start=end-overlap
            chunk_number+=1

    return chunks