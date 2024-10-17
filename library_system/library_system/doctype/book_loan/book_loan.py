# Copyright (c) 2024, Adham Hebeish and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime 
from frappe.utils import add_to_date, today


class BookLoan(Document):
	def validate(self):
		# Read-Only Filling
		total_books = 0
		total_deposit = 0
		for x in self.books:
			total_books += 1
			total_deposit += x.price
		late_fees = total_deposit * 0.35
		total_price = total_deposit + late_fees
		self.total_books = total_books
		self.total_loan_deposit = total_deposit
		self.late_fees = late_fees
		self.total_price = total_price
		if today() <= self.loan_date:
			self.return_date = add_to_date(self.loan_date, days = 24)
		else:
			frappe.throw("The Loan date cannot be in the past")
		# Feild Validation
		if len(str(self.cvv).replace(" ","")) != 3:
			frappe.throw("The CVV must be 3 digits long")
		if len(str(self.card_number).replace(" ","")) != 16:
			frappe.throw("Your Card Number must be 16 digits long")
		elif self.card_number.isnumeric() == False:
			frappe.throw("Your Card Number contains non-digit characters")
		
		