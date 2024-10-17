Referencing {{ doc.name }}:

{{ doc.full_name }}'s books are due in 72 hours.
The return date is {{ doc.return_date }}.
The customer will pay an extra {{ doc.late_fees }} if they do not return the books on time.

Contact Information:

- Email: {{ doc.email_address }}
- Phone Number: {{ doc.phone_number }}
- Address: {{ doc.address }} (Postal Code: {{ doc.postal_code }} )

Transactional Information:

- Books Loaned: {{ doc.total_books }}

- Loan: {{ doc.total_loan_deposit }}
- Loan + Fees: {{ doc.total_price }}

The customer will be notified after 24 hours of the sending of this message.