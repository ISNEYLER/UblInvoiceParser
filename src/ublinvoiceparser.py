import xml.etree.ElementTree as ET

NAME_SPACE = {
        'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2', 
        'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2'
    }

def get_data_invoice(xml):
    document = ET.parse(xml)
    root = document.getroot()
    xmlInvoice = root.find('cac:Attachment/cac:ExternalReference/cbc:Description', NAME_SPACE).text
    invoice = ET.fromstring(xmlInvoice)
    invoiceLines = invoice.findall('cac:InvoiceLine',NAME_SPACE)
    listProducts = []
    for line in invoiceLines:
        dictProducts = {
            'SKU' : line.find('cac:Item/cac:InformationContentProviderParty/cac:AgentParty/cac:PartyIdentification/cbc:ID',NAME_SPACE).text,
            'description' : line.find('cac:Item/cbc:Description',NAME_SPACE).text,
            'quantity' : line.find('cac:Price/cbc:BaseQuantity',NAME_SPACE).text,
            'price' : line.find('cac:Price/cbc:PriceAmount',NAME_SPACE).text,   
        }
        listProducts.append(dictProducts)
    dictInvoice = {
        "invoice": {
            "id": invoice.find('cbc:ID',NAME_SPACE).text,
            "date": invoice.find('cbc:DueDate',NAME_SPACE).text,
            "cufe": invoice.find('cbc:UUID',NAME_SPACE).text,
            "seller": {
                "Name": invoice.find('cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name',NAME_SPACE).text,
                "NIT": invoice.find('cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID',NAME_SPACE).text,
                "City": invoice.find('cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:CityName',NAME_SPACE).text,
                "State": invoice.find('cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:CountrySubentity',NAME_SPACE).text,
                "Address": invoice.find('cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cac:AddressLine/cbc:Line',NAME_SPACE).text,
                "Email": invoice.find('cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:ElectronicMail',NAME_SPACE).text
            },
            "client": {
                "Name": invoice.find('cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name',NAME_SPACE).text,
                "NIT": invoice.find('cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID',NAME_SPACE).text,
                "City": invoice.find('cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:CityName',NAME_SPACE).text,
                "State": invoice.find('cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:CountrySubentity',NAME_SPACE).text,
                "Address": invoice.find('cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cac:AddressLine/cbc:Line',NAME_SPACE).text,
                "Email": invoice.find('cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:ElectronicMail',NAME_SPACE).text
            },
            "lines" : listProducts
        }
    }
    return dictInvoice