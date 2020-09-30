$('#contact-form').submit(function (e) { 

        var name = document.getElementById('inputname'),
        email = document.getElementById('inputemail'),
        message = document.getElementById('inputmessage');

        console.log(message);
        if (!name.value || !email.value || !message.value){
            window.alert("Please check your entries");
        }
        else {
            $.ajax({
                url: '//formspree.io/thuykhuedn@gmail.com',
                method: 'POST',
                data: $(this).serialize(),
                dataType: 'json',
            });
            e.preventDefault();
            $(this).get(0).reset();
            window.alert("Message sent!")
        }

    });