// $(document).ready(function () {
//   console.log('number-seperator works') 
//   $(document).on('input', '.form-field', function (e) {
//     if (/^[0-9.,]+$/.test($(this).val())) {
//       $(this).val(
//         parseFloat($(this).val().replace(/,/g, '')).toLocaleString('en')
//       );
//     } else {
//       $(this).val(
//         $(this)
//           .val()
//           .substring(0, $(this).val().length - 1)
//       );
//     }
//   });
// });

// function numberWithCommas(x) {
//     return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
// }

// $(document).ready(function () {
//   console.log('number-seperator works')
//   $(document).on('input', '.form-field', function (x) {
//     $("input[class='form-field']").attr('value',"GPL");
//   });
// });