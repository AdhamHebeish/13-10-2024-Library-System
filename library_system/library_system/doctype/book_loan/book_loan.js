// Copyright (c) 2024, Adham Hebeish and contributors
// For license information, please see license.txt

frappe.ui.form.on("Book Loan", {
    refresh(frm) {

    },
});
frappe.ui.form.on('Book Loan Receipt', {
   book(frm, cdt, cdn) {
       let total_books = 0;
       let total_loan = 0;
       for (let book of frm.doc.books) {
           total_books += 1;
           total_loan += book.price;
       }
       const late_fees = total_loan * 0.35
       const total_price = total_loan + late_fees
       frm.set_value("total_books", total_books);
       frm.set_value("total_loan_deposit", total_loan);
       frm.set_value("late_fees", late_fees);
       frm.set_value("total_price", total_price);
   }
})