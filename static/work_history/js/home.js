$(document).ready(function () {
    const customRenderMenu = function(ul, items){
        let self = this;
        let category = null;

        let sortedItems = items.sort(function(a, b) {
           return a.category.localeCompare(b.category);
        });
    
        $.each(sortedItems, function (index, item) {
            if (item.category != category) {
                category = item.category;
                ul.append('<li class="ui-autocomplete-group">' + category + '</li>');
            }
            self._renderItemData(ul, item);
        });
    };

    $("#work_history_tags").tagit({
        minLength: 2,
        removeConfirmation: true,
        autocomplete: {
            appendTo: "#tags_dropdown_wrapper",
            create: function () {
                //access to jQuery Autocomplete widget differs depending
                //on jQuery UI version - you can also try .data('autocomplete')
                $(this).data('uiAutocomplete')._renderMenu = customRenderMenu;
            },
            source: function (request, response) {
                console.log(request.term);
                $.ajax({
                    url: "/api/work-history/?search=" + request.term,
                    dataType: "json",
                    headers: {
                        'X-CSRFToken': $('meta[name="csrftoken"]').attr('content')
                    },
                    success: function (data) {
                        const result = [];
                        for (let key in data) {
                            const items = data[key]
                            for (let i = 0; i < items.length; i ++) {
                                result.push({
                                    label: items[i].label,
                                    value: items[i].category + ': ' + items[i].label,
                                    category: items[i].category
                                })
                            }
                        }
                        response(result)
                    }
                });
            }
        },
    });
});