$(document).ready(function(){
    setInterval(function(){
        $.ajax({
            type: 'GET',
            url : "/getMessages",
            success: function(response){
                //alert(response.message)
                $("#msg-area").empty();
                for (var key in response.messages)
                {
                    let textToShow = "<p> " + response.messages[key].sender +  " to "  + response.messages[key].reciever +" : " + response.messages[key].messageText+" </p>"
                    console.log(textToShow)
                    $("#msg-area").append(textToShow);
                }
            },
            error: function(response){
            }
        });
    },1000);
    })