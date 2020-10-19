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
    console.log("document ready!");
    var slug = document.getElementById("slug_id").getAttribute("value");
    var initial_tenure = document.getElementById("initial_tenure_id").getAttribute("value");
    var initial_principal = document.getElementById("initial_principal_id").getAttribute("value");
    console.log("initial_principal:");
    console.log(initial_principal);
    console.log("initial_tenure:");
    console.log(initial_tenure);

    // Get tenures
    runAjaxQuery($("#quickLoanDetailRequestForm").attr("data-tenures-url"),{'slug': slug, 'initial_tenure':initial_tenure},"select[name='tenure']");
    // Get principal limits
    runAjaxQuery($("#quickLoanDetailRequestForm").attr("get-principal-limits-url"),{'slug': slug, 'initial_principal':initial_principal},"div[id='div_id_principal']");
    
    console.log(slug)
});