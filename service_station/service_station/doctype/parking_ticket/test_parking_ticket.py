# Copyright (c) 2023, ameen and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestParkingTicket(FrappeTestCase):
	def test_parking_ticket(self):
		test_ticket = frappe.get_doc({
			"doctype":"Parking Ticket",
			"customer": "_Test Customer 2",
			"vehicle": "BNV2790"
		}).insert()
		print('\n\nDone insert into Parking Ticket')
