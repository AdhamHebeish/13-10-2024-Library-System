# Copyright (c) 2024, Adham Hebeish and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Book(WebsiteGenerator):
	def validate(self):
		if len(str(self.isbn).replace(" ","")) != 16:
			frappe.throw("ISBN must be 16 digits long")
		elif self.isbn.isnumeric() == False:
			frappe.throw("The ISBN contains non-digit characters")
	
	def before_save(self):
		self.book_name = f"{self.book_title}, {self.book_series or self.book_author}"