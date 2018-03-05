$(document).ready(function() {
    $("#artists").change(function(element) {
        $("#custom-rakings").html('')
        $("#custom-rakings").append("<h3>Rankings para cada artista:</h3>");
        $("#artists option:selected").each(function(key, item) {
            var input = $("<input></input>")
            input.addClass('form-control')
            input.attr({name: item.value, type: 'number', min: 1, max: 5})
            input.val('5')
            $("#custom-rakings").append(item.value);
            $("#custom-rakings").append(input);
            console.log(item);
        });
    });
});