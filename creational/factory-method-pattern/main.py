from factory import DocumentFactory

if __name__ == "__main__":

    invoice    = DocumentFactory.create_document("invoice", { "societyid": 4240, "flat": 102 })
    creditnote = DocumentFactory.create_document("credit_note", { "societyid": 4240, "flat": 102 })
    debitnote  = DocumentFactory.create_document("debit_note", { "societyid": 4240, "flat": 102 })

    print(invoice)
    print(creditnote)
    print(debitnote)