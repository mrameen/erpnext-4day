// Copyright (c) 2023, ameen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle Inspection', {
	refresh: function(frm) {
		frm.fields_dict['required_services_detail'].grid.get_field('service_item').get_query = function(){
			return {
				filters:[
					['Item','item_group','=','Services']
				]
			}
		};

		frm.fields_dict['required_spare_detail'].grid.get_field('spare_item').get_query = function(){
			return {
				filters:[
					['Item','item_group','=','Spare Parts']
				]
			}
		};
	},
	before_submit: function(frm){
		frappe.call({
			method:'service_station.services.rest.create_sales_invoice',
			args: {
				'inspection': frm.doc.name
			},
			callback: function(r) {
				//
			}
		});
		// frappe.validated = false; // it will not be submitted for testing
	}
});


frappe.ui.form.on('Required Service Detail',"quantity",function(frm,cdt,cdn){
	let selectedRow = locals[cdt][cdn];
	selectedRow.amount = selectedRow.rate * selectedRow.quantity;
	frm.refresh_field('required_services_detail');
	console.log(selectedRow);
})

frappe.ui.form.on('Required Spare Detail',"quantity",function(frm,cdt,cdn){
	let selectedRow = locals[cdt][cdn];
	selectedRow.amount = selectedRow.rate * selectedRow.quantity;
	frm.refresh_field('required_spare_detail');
	console.log(selectedRow);
})