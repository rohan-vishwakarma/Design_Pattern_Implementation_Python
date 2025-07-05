from base import Document

class Invoice(Document):

    @staticmethod
    def generate(request):
        try:
            return {"message": "Invoice Generated Successfully", "request": request, "status_code" : 201}
        except Exception as e:
            return {"message": f"Something Went Wrong {e}", "request": request, "status_code": 500}

class CreditNote(Document):

    @staticmethod
    def generate(request):
        return {"message": "Creditnote Generated Successfully", "request": request, "status_code" : 201}

class DebitNote(Document):

    @staticmethod
    def generate(request):
        return {"message": "Debitnote Generated Successfully", "request": request, "status_code" : 201}
