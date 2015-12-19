$(function(){

    $('#search').keyup(function() {

        $.ajax({
            type: "POST",
            url: "/search/",
            data: {

                'search_text' : $('#search').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()

            },


            success: searchSuccess,
            dataType: 'html'

        });

    });

});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);

}



/*$(function(){

    $('#likebutton').click(function() {

        $.ajax({
            type: "POST",
            url: "/like/",
            data: {

                'liketrigger' : $('#likebutton').attr('name'),
                'csrfmiddlewaretoken': '{{ csrf_token }}'


            },


            success: likeSuccess,
            dataType: 'html'

        });

    });

});

function likeSuccess(data, textStatus, jqXHR)
{
    $('#likenum').html(data);

}*/