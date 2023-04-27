import frappe


@frappe.whitelist()
def create_sales_invoice(inspection): # vehicle_inspection.js call this function before submit doc
    # print(f'\n\n{inspection}\n\n')
    ticket_number = frappe.db.get_value('Vehicle Inspection',inspection,'ticket_number')
    customer = frappe.db.get_value('Parking Ticket',ticket_number,'customer')
    my_query = f"""
        SELECT 
            pt.customer
        FROM
            `tabParking Ticket` AS pt
        JOIN
            `tabVehicle Inspection` AS vi
        ON pt.name = vi.ticket_number
        WHERE vi.name = '{inspection}'
    """
    # customer = frappe.db.sql(my_query, as_diction=True)
    customer = frappe.db.sql(my_query, as_dict=True)[0] # first index
    

    services = frappe.db.get_all('Required Service Detail',filters={'parent':inspection},fields=['service_item','rate','quantity'])
    spare_parts = frappe.db.get_all('Required Spare Detail',filters={'parent':inspection},fields=['spare_item','rate','quantity'])
    items = []
    for x in services:
        a = {
            "item_code": x.service_item,
            "qty": x.quantity,
            "rate": x.rate,
        }
        items.append(a)
    for x in spare_parts:
        a = {
            "item_code": x.spare_item,
            "qty": x.quantity,
            "rate": x.rate,
        }
        items.append(a)
    sales_invoice = frappe.get_doc({
        "doctype": "Sales Invoice",
        "customer": customer['customer'],
        "due_date": frappe.utils.nowdate(),
        "parking_ticket": ticket_number,
        "items":items
    })
    sales_invoice.insert()
    # sales_invoice.submit() # auto submit
    frappe.db.commit() # save into db

    print(f'\n\n{customer}\n\n')
    print(f'\n\n{services}\n\n')
    print(f'\n\n{items}\n\n')
    print(f'\n\nticket_number:{ticket_number}\n\n')