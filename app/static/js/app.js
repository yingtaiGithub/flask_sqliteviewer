/* Add your Application JavaScript */
$(document).ready(function(){
    $(function(){
        $("#table td").each(function() {
            var text = $(this).text();
            $(this).html('');
            $(this).append($('<span>'+text+'<span>'));
        });

    });

    $(".area").click(function() {
        var area_name = $(this).attr('id')
//        var child_selector = 'td:first-child:contains("' + area_name + '")'
        var child_selector = 'td:nth-child(2):contains("' + area_name + '")'
        var regions = $(this).closest('div').find(".region")

        if( $(this).is(':checked') ) {

            regions.each(function(){
                this.checked=true;
            });

//            $('tr:has('+child_selector+')').css('display', 'none')
            $('tr:has('+child_selector+')').each(function(){
                $(this).find("td:nth-child(3) > span").css('display', 'none');
//                $(this).find("td:nth-child(5) > span").css('display', 'none');
                $(this).find("td:nth-child(6) > span").css('display', 'none');
            });

        } else {
            regions.each(function(){
                this.checked=false;
            });

//            $('tr:has('+child_selector+')').css('display', 'table-row')
            $('tr:has('+child_selector+')').each(function(){
                $(this).find("td:nth-child(3) > span").css('display', 'inline-block');
//                $(this).find("td:nth-child(5) > span").css('display', 'inline-block');
                $(this).find("td:nth-child(6) > span").css('display', 'inline-block');
            });
        }
    })

    $(".region").click(function() {
        var region_name = $(this).attr('id').replace(/\s/g, '');
        var child_selector = 'td:nth-child(3):contains("' + region_name + '")'

        if ($(this).is(":checked")) {
            $('tr:has('+child_selector+')').each(function(){
                $(this).find("td:nth-child(3) > span").css('display', 'none');
//                $(this).find("td:nth-child(5) > span").css('display', 'none');
                $(this).find("td:nth-child(6) > span").css('display', 'none');
            });
        } else {
            $('tr:has('+child_selector+')').each(function(){
                $(this).find("td:nth-child(3) > span").css('display', 'inline-block');
//                $(this).find("td:nth-child(5) > span").css('display', 'inline-block');
                $(this).find("td:nth-child(6) > span").css('display', 'inline-block');
            });
        }
    })
});
