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
//            $('tr:has('+child_selector+')').each(function(){
//                $(this).find("td:nth-child(3) > span").css('display', 'none');
////                $(this).find("td:nth-child(5) > span").css('display', 'none');
//                $(this).find("td:nth-child(6) > span").css('display', 'none');
//            });

        } else {
            regions.each(function(){
                this.checked=false;
            });

//            $('tr:has('+child_selector+')').css('display', 'table-row')
//            $('tr:has('+child_selector+')').each(function(){
//                $(this).find("td:nth-child(3) > span").css('display', 'inline-block');
////                $(this).find("td:nth-child(5) > span").css('display', 'inline-block');
//                $(this).find("td:nth-child(6) > span").css('display', 'inline-block');
//            });
        }
    })

    $(".region").click(function() {
        var region_name = $(this).attr('id').replace(/\s/g, '');
        var child_selector = 'td:nth-child(3):contains("' + region_name + '")'

//        if ($(this).is(":checked")) {
//            $('tr:has('+child_selector+')').each(function(){
//                $(this).find("td:nth-child(3) > span").css('display', 'none');
////                $(this).find("td:nth-child(5) > span").css('display', 'none');
//                $(this).find("td:nth-child(6) > span").css('display', 'none');
//            });
//        } else {
//            $('tr:has('+child_selector+')').each(function(){
//                $(this).find("td:nth-child(3) > span").css('display', 'inline-block');
////                $(this).find("td:nth-child(5) > span").css('display', 'inline-block');
//                $(this).find("td:nth-child(6) > span").css('display', 'inline-block');
//            });
//        }
    })


    $("#submit").click(function(){
        $("td > span").css('display', 'inline-block')

        var checked_areas = new Array()
        var checked_regions = new Array()

        $(".area:checked").each(function(){
            checked_areas.push($(this).attr('id'))
        })

        $(".area:not(:checked)").closest('div').find('.region:checked').each(function(){
            checked_regions.push($(this).attr('id'))
        })

        jQuery.each(checked_areas, function(i, area){
            var child_selector = 'td:nth-child(2):contains("' + area + '")'
            $('tr:has('+child_selector+')').each(function(){
                $(this).find("td:nth-child(3) > span").css('display', 'none');
//                $(this).find("td:nth-child(5) > span").css('display', 'none');
                $(this).find("td:nth-child(6) > span").css('display', 'none');
            });
        });

        jQuery.each(checked_regions, function(i, region) {
            var child_selector = 'td:nth-child(3):contains("' + region + '")'
            $('tr:has('+child_selector+')').each(function(){
                $(this).find("td:nth-child(3) > span").css('display', 'none');
//                $(this).find("td:nth-child(5) > span").css('display', 'none');
                $(this).find("td:nth-child(6) > span").css('display', 'none');
            });
        });

        $.getJSON($SCRIPT_ROOT + '/submit', {
            areas: JSON.stringify(checked_areas),
            regions: JSON.stringify(checked_regions)
        }, function(data){

        });
    });

    $("#restart").click(function() {
        $.getJSON($SCRIPT_ROOT + '/get_status', {
        }, function(data){
            // Uncheck all checkboxes:
            $("input:checkbox").removeAttr('checked');

            // Check the areas and regions.
            var areas = data.areas;
            var regions = data.regions;

            jQuery.each(areas, function(i, area){
                $('#' + area).prop('checked', true);

                var child_selector = 'td:nth-child(2):contains("' + area + '")'
                var regions = $('#' + area).closest('div').find(".region")

                regions.each(function(){
                    this.checked=true;
                });

                $('tr:has('+child_selector+')').each(function(){
                    $(this).find("td:nth-child(3) > span").css('display', 'none');
    //                $(this).find("td:nth-child(5) > span").css('display', 'none');
                    $(this).find("td:nth-child(6) > span").css('display', 'none');
                });
            });

            jQuery.each(regions, function(i, region) {
                $('#' + region).prop('checked', true);

                var child_selector = 'td:nth-child(3):contains("' + region + '")'
                $('tr:has('+child_selector+')').each(function(){
                    $(this).find("td:nth-child(3) > span").css('display', 'none');
    //                $(this).find("td:nth-child(5) > span").css('display', 'none');
                    $(this).find("td:nth-child(6) > span").css('display', 'none');
                });

            })
        });
    })
});

