
$(document).ready(function(){
form_count = $("[name=inst]").val();
// get extra form count so we know what index to use for the next item.
$("#add-another").click(function() {
    element = $('</br><textarea cols="40" rows="5">');
    element.attr('name', 'extra_field_' + form_count);
    $("#steps").append(element);
    // build element and append it to our forms container

    form_count ++;
    $("[name=inst]").val(form_count);
    // increment form count so our view knows to populate 
    // that many fields for validation
});
});