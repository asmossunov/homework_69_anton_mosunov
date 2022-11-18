window.addEventListener('load', function() {

    function getCookie(c_name) {
        if(document.cookie.length > 0) {
            c_start = document.cookie.indexOf(c_name + "=");
            if(c_start != -1) {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if(c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
    }

    let buttonAdd = $('#calculate-add');
    buttonAdd.on('click', function(evt) {
        evt.preventDefault();
        // $('#result').val('');
        $.ajax({
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            url: 'add/',
            type: 'POST',
            data: JSON.stringify({
                'A': $('#number-a').val(),
                'B': $('#number-b').val(),
            }),
            error: function(data) {
                $('#result').css('color', 'red')
                $('#result').html(data.responseJSON.error)

            },
        }).done(
            function(data) {
                $('#result').css('color', 'green')
                $('#result').html(data.result)
            },

        )
    });


    let buttonSubtract = $('#subtract');
    buttonSubtract.on('click', function(evt) {
        evt.preventDefault();
        // $('#result').val('');
        $.ajax({
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            url: 'subtract/',
            type: 'POST',
            data: JSON.stringify({
                'A': $('#number-a').val(),
                'B': $('#number-b').val(),
            }),
            error: function(xhr, status, error) {
                $('#result').css('color', 'red')
                $('#result').html(data.responseJSON.error)
            },
        }).done(
            function(data) {
                $('#result').css('color', 'green')
                $('#result').html(data.result)
            }
        )
    });


    let buttonMultiply = $('#multiply');
    buttonMultiply.on('click', function(evt) {
        evt.preventDefault();
        $.ajax({
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            url: 'multiply/',
            type: 'POST',
            data: JSON.stringify({
                'A': $('#number-a').val(),
                'B': $('#number-b').val(),
            }),
            error: function(xhr, status, error) {
                $('#result').css('color', 'red')
                $('#result').html(data.responseJSON.error)
            },
        }).done(
            function(data) {
                $('#result').css('color', 'green')
                $('#result').html(data.result)

            }
        )
    });


    let buttonDivide = $('#divide');
    buttonDivide.on('click', function(evt) {
        evt.preventDefault();
        $.ajax({
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            url: 'divide/',
            type: 'POST',
            data: JSON.stringify({
                'A': $('#number-a').val(),
                'B': $('#number-b').val(),
            }),
            error: function(xhr, status, error) {
                $('#result').css('color', 'red')
                $('#result').html(data.responseJSON.error)
            },
        }).done(
            function(data) {
                $('#result').css('color', 'green')
                $('#result').html(data.result)

            }
        )
    });

})
