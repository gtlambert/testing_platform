console.log('file is loading');
console.log('file has got my changes');

$(function() {
    $('#review-mismatches button').click(function() {
        console.log('click');
    	$.ajax({
			url: 'review-mismatch',
			type: 'POST',
            data: {'contentType': $('#review-mismatches select option:selected').attr('value')},
			success: function(data) {
				console.log('this was a successful call');
				console.log('this is the data returned');
				console.log(data);
			}
		});
    });
});

$(function() {
    $('#content button').click(function() {
        console.log('click');
        $.ajax({
            url: 'content',
            type: 'POST',
            data: {'contentType': $('#content select option:selected').attr('value')},
            success: function(data) {
                console.log('this was a successful call');
                console.log('this is the data returned');
                console.log(data);
            }
        });
    });
});



// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
