from enum import Enum
from typing import Dict

from documents import Invoice, CreditNote, DebitNote

class Documents(Enum):
    invoice     = "invoice"
    credit_note = "credit_note"
    debit_note  = "debit_note"

class DocumentFactory:

    @staticmethod
    def create_document(document: str, request: Dict) -> Dict:
        document = document.lower()
        if document == Documents.invoice.name:
            return Invoice.generate(request)
        elif document == Documents.debit_note.name:
            return DebitNote.generate(request)
        elif document == Documents.credit_note.name:
            return CreditNote.generate(request)
        else:
            return {"message": "Document type not found", "status_code": 400}


