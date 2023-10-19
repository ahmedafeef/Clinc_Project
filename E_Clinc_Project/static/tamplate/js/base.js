
$('select[name="payment_method"]').on('change', function() {
 if ($( this ).val()==1){
 $('.field-check_number').hide();
 $('.field-bank_name').hide();
 $('.field-transaction_number').hide();
// $('form-group field-check_number').hide();
 }else if ($( this ).val()==2){
  $('.field-check_number').show();
  $('.field-bank_name').show();
  $('.field-transaction_number').hide();
 }else if ($( this ).val()==3){
  $('.field-check_number').hide();
  $('.field-bank_name').hide();
  $('.field-transaction_number').show();
 }else{

 $('.field-check_number').hide();
 $('.field-bank_name').hide();
 $('.field-transaction_number').hide();
 }
  }).trigger( "change" );

