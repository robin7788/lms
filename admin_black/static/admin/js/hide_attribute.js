var hide_page=true;
$(document).ready(function(){
    var checkbox =$('.show_hidden_field input[type="checkbox"]');
    var hiddenContent = $(".show_hide_collapse");
    if (checkbox.is(':checked')) {
        hiddenContent.show();
        hide_page=true;
    } else {
        hiddenContent.hide();
        hide_page=false;
    }
    checkbox.click(function(){
        hide_page=!hide_page;

        setDefaultValue(hiddenContent)
        if (hide_page) {
            hiddenContent.slideDown();
        } else {
            hiddenContent.slideUp();
        }
    })

    // reset all values of input field
    function setDefaultValue($container) {
        $container.find('input, textarea, checkbox').each(function() {
            if($(this).attr('type') == 'checkbox')
                $(this).prop("checked", false);
            else if ($(this).attr('type') == 'number')
                $(this).val("0")
            else
                $(this).val("")
        });
    }
})