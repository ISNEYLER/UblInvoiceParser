### Descripcion
Esto es el comienzo de un sencillo modulo Python que extrae información de facturas electrónicas realizadas conforme al anexo técnico de la Dirección de Impuestos y Aduanas Nacionales (DIAN) bajo el estándar UBL.

### ¿Como usar?

```
get_data_invoice(factura_xml)

#La función get_data_invoice retorna la información de la factura como un diccionario.
Se espera que la salida se vea de la siguiente forma:

{
  'invoice': {
    'id': 'XXXXXXX',
    'date': '0000-00-00',
    'cufe': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'seller': {
      'Name': 'XXXXXXX',
      'NIT': '0',
      'City': 'XXXXXXX',
      'State': 'XXXXXXX',
      'Address': 'XXXXXXX',
      'Email': 'XXXXXXX@email.com'
    },
    'client': {
      'Name': 'XXXXXXX',
      'NIT': '0',
      'City': 'XXXXXXX',
      'State': 'XXXXXXX',
      'Address': 'XXXXXXX',
      'Email': 'XXXXXXX@email.com'
    },
    'lines': [
      {
        'SKU': 'XXXXXXX',
        'description': 'XXXXXXX',
        'quantity': '0',
        'price': '0'
      },
      {
        'SKU': 'XXXXXXX',
        'description': 'XXXXXXX',
        'quantity': '0',
        'price': '0'
      },
    ]
  }
}

```

PD. Este es mi primer repo asi que pueden haber errores medio tontos o obvios jsjsj