$("i[id='show-hide-payment-plan-btn']").click(function () {
    var table = document.getElementById("id_payment_plan");
    var show = table.getAttribute('show');
    if (show=='summary'){
		for (var i = 0, row; row = table.rows[i]; i++) {
		   //iterate through rows
		   //rows would be accessed using the "row" variable assigned in the for loop
		   row.removeAttribute('hidden', '');
		}
		table.setAttribute('show','all');
	} else {
		for (var i = 11, row; row = table.rows[i]; i++) {
		   //iterate through rows
		   //rows would be accessed using the "row" variable assigned in the for loop
		   
		   row.setAttribute('hidden', '');
		}
		table.setAttribute('show','summary');
	}
});