// INITIAL CONFIGURATION

function runAjaxQuery(url_,data_,return_to_) {
    $.ajax({
        url: url_,
        data: data_,
        success: function (data) {
            console.log('query success')
            $(return_to_).html(data);
        }
    });
}

$(document).ready(function() {
    console.log("document ready!")
    
    // Set default choice to GPL
    $("input[id='id_loan_type']").attr('value',"GPL");
    // Get tenures
    runAjaxQuery($("#loanRequestForm").attr("data-tenures-url"),{'loan_type': "GPL"},"select[id='id_tenure']");
    // Get principal limits
    runAjaxQuery($("#loanRequestForm").attr("get-principal-limits-url"),{'loan_type': "GPL"},"div[id='div_id_principal']");
    
    console.log('initial choice set to GPL')
});

// ON TAB CLICK 

$("li[class='nav-item']").click(function () {
    var url = $("#loanRequestForm").attr("data-tenures-url");
    var loan_type = $(this).attr('loan-type');

    // Set choice
    $("input[id='id_loan_type']").attr('value',loan_type);
    // Get tenures
    runAjaxQuery($("#loanRequestForm").attr("data-tenures-url"),{'loan_type': loan_type},"select[id='id_tenure']");
    // Get principal limits
    runAjaxQuery($("#loanRequestForm").attr("get-principal-limits-url"),{'loan_type': loan_type},"div[id='div_id_principal']");
});

// ON 2. EL CLICK 
$("input[id='2el']").click(function () {
    console.log("2. el selected")
    var url = $("#loanRequestForm").attr("data-tenures-url");

    // Set choice to CA2
    $("input[id='id_loan_type']").attr('value','CA2');
    // Get tenures
    runAjaxQuery($("#loanRequestForm").attr("data-tenures-url"),{'loan_type': 'CA2'},"select[id='id_tenure']");
    // Get principal limits
    runAjaxQuery($("#loanRequestForm").attr("get-principal-limits-url"),{'loan_type': 'CA2'},"div[id='div_id_principal']");
});