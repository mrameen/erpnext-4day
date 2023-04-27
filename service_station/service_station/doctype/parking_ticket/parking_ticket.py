# Copyright (c) 2023, ameen and contributors
# For license information, please see license.txt

import frappe,random,time
from frappe.model.document import Document

class ParkingTicket(Document):
	def before_insert(self):
		rd = random.randint(0,1000000)
		rd = unixtime()
		print('\n\nbefore_insert() random ticket number:',rd,'\n\n')
		self.ticket_number = rd
    
def unixtime():
    ts = int(time.time())
    return ts