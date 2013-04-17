
$(document).ready(function(){
step_count = Number($("[name=inst]").val())+1;
ing_count = Number($("[name=ings]").val());
pic_count = Number($("[name=pic]").val());

// get extra form count so we know what index to use for the next item.
$("#add-another").click(function() {
    element = $('</br><label for="id_instructions">Step '+String(step_count+1)+':</label><textarea cols="40" rows="5">');
    element.attr('name', 'extra_field_' + step_count);
    $("#steps").append(element);
    // build element and append it to our forms container

    step_count ++;
    $("[name=inst]").val(step_count-1);
    // increment form count so our view knows to populate 
    // that many fields for validation
});


$("#add-ing").click(function() {
	ingsd = $("#ingre").val();
    element = $('<div class="fieldWrapper">'
	        +'<input placeholder="Ingredient Name" id="extra_ings_'+ing_count+'" name="extra_ings_'+ing_count+'" type="text" data-provide="typeahead" data-source=\''+ingsd+'\' autocomplete="off"> <input type="text" placeholder="Amount" id="amount_extra_ings_'+ing_count+'" name="amount_extra_ings_'+ing_count+'"> <select id="unit_extra_ings_'+ing_count+'" name="unit_extra_ings_'+ing_count+'">'
  					+$("#unitss").html()
					+'</select>'
	    +'</div>');
    $("#ingredients").append(element);
    // build element and append it to our forms container

    ing_count ++;
    $("[name=ings]").val(ing_count);
    // increment form count so our view knows to populate 
    // that many fields for validation
});

$("#add-pic").click(function() {
    element = $('<input id="id_picture_'+pic_count+'" name="picture" type="file">');
    $("#pics").append(element);
    // build element and append it to our forms container

    pic_count ++;
    $("[name=pic]").val(pic_count);
    // increment form count so our view knows to populate 
    // that many fields for validation
});


});