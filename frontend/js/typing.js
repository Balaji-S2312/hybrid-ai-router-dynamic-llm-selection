function typeResponse(text) {

    const responseBox = document.getElementById("response");

    responseBox.innerHTML = "";

    let index = 0;

    const speed = 18; // milliseconds

    function type() {

        if (index < text.length) {

            responseBox.innerHTML += text.charAt(index);

            responseBox.scrollTop = responseBox.scrollHeight;

            index++;

            setTimeout(type, speed);

        }

    }

    type();

}