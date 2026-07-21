from rag.document_processor import extract_text,create_chunks


def test_extract_txt():
    pages=extract_text("data/ai.txt")

    assert len(pages)>0
    assert "text" in pages[0]
    assert "page" in pages[0]


def test_create_chunks():
    pages=[
        {
            "text":"Artificial Intelligence is a branch of computer science.",
            "page":1
        }
    ]

    chunks=create_chunks(
        pages,
        "test.txt",
        chunk_size=20,
        overlap=5
    )

    assert len(chunks)>0
    assert "text" in chunks[0]
    assert "metadata" in chunks[0]