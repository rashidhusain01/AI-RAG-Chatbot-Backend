import fitz


def extract_text_from_pdf(pdf_path):
   
   doc = fitz.open(pdf_path)

   text = ""

   for page in doc:
      text += page.get_text()
      
   doc.close()
   
   return text


def split_text_into_chunks(text, chunk_size=700, overlap=150):

   chunks = []
   start = 0
   
   while start < len(text):
      end = start + chunk_size
      chunk = text[start:end]
      chunks.append(chunk)
      start += chunk_size - overlap

   return chunks 