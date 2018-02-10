document.addEventListener("DOMContentLoaded", function(event) {
    var form = document.getElementById("answer");
    if (form) {
        setSubmitAction(form, submitAnswerForm);
    } else {
        form = document.getElementById("register_form");
        if (form) {
            setSubmitAction(form, submitRegisterForm);
        }
    }

    var email_form = document.getElementById("email_form");
    if (email_form) {
        setSubmitAction(email_form, submitEmailForm);
    }

    var canvas = document.getElementById("mountains");
    var width = Math.max(screen.width, screen.height);
    var height = 150;
    var resolutionScale = 2;

    canvas.width = width * resolutionScale;
    canvas.height = height * resolutionScale;
    canvas.style.width = width + "px";
    canvas.style.height = height + "px";

    drawMountains("#ad778e", [100, 150, 200]);
    drawMountains("#65455d", [50, 100, 150, 200, 250]);
    drawSideMountains();
});

function setSubmitAction(form, func) {
    if (form) {
        form.addEventListener("submit", function(event) {
            event.preventDefault();
            func(form);
        });
    }
}

function drawSideMountains() {
    var canvases = document.getElementsByClassName("side-mountain");
    var color = "#432e3e";
    var width = 500;

    for (var i = 0; i < canvases.length; i++) {
        var canvas = canvases.item(i);
        var context = canvas.getContext("2d");

        canvas.width = width;
        canvas.height = width;
        drawTriangle(context, 0, canvas.height / 2.0, canvas.width, canvas.height / 2.0, color);

        // Mirrored
        var gradient = context.createLinearGradient(0, canvas.height / 2.0, 0, canvas.height);
        gradient.addColorStop(0, "#193854");
        gradient.addColorStop(1, "#225380");
        drawTriangle(context, 0, canvas.height / 2.0, canvas.width, -canvas.height / 2.0, gradient);
    }
}

function drawMountains(color, heights) {
    var canvas = document.getElementById("mountains");
    var context = canvas.getContext("2d");

    var baseHeight = 50;
    var positions = [];
    var prevY;
    var x = 0;
    var y = randElement(heights);

    context.beginPath();
    y = randElement(heights);
    prevY = y;
    context.moveTo(x, y);

    while (x < canvas.width) {
        y = randElement(heights);
        x += Math.abs(prevY - y);
        prevY = y;

        context.lineTo(x, y);
        positions.push([x, y]);
    }

    context.lineTo(x, heights[heights.length - 1] + baseHeight);
    context.lineTo(0, heights[heights.length - 1] + baseHeight);
    context.lineTo(0, positions[positions.length - 1][1]);
    context.fillStyle = color;
    context.fill();
}

function drawTriangle(context, x, y, width, height, color) {
    context.beginPath();
    context.moveTo(x, y);
    context.lineTo(x + width, y);
    context.lineTo(x + (width / 2.0), y - height);
    context.lineTo(x, y);

    context.fillStyle = color;
    context.fill();
}

function randElement(array) {
    return array[randIntInclusive(0, array.length - 1)];
}

function randIntInclusive(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function submitAnswerForm(form) {
    var request = new XMLHttpRequest();
    var formData = new FormData();

    formData.append("csrf_token", form.csrf_token.value);
    formData.append("answer", form.answer.value);

    request.addEventListener("load", function(event) {
        if (event.target.status == 200) {
            var rsvp = document.getElementById("rsvp");
            removeAllChildren(rsvp);
            rsvp.innerHTML = event.target.responseText;

            var form = document.getElementById("register_form");
            if (form) {
                setSubmitAction(form, submitRegisterForm);
            }

            var email_form = document.getElementById("email_form");
            if (email_form) {
                setSubmitAction(email_form, submitEmailForm);
            }
        } else {
            console.log("Response", event.target.status);
        }
    });

    request.open("POST", "/answer");
    request.send(formData);
}

function submitRegisterForm(form) {
    var request  = new XMLHttpRequest();
    var formData = new FormData();

    formData.append("csrf_token", form.csrf_token.value);
    formData.append("first_name", form.first_name.value);
    formData.append("last_name", form.last_name.value);
    formData.append("allergies", form.allergies.value);
    formData.append("vegetarian", form.vegetarian.checked);
    formData.append("vegan", form.vegan.checked);
    formData.append("kids_menu", form.kids_menu.checked);

    request.addEventListener("load", function(event) {
        // Remove errors.
        var errors = document.getElementsByClassName("error");
        for (var i = 0; i < errors.length; i++) {
            errors[i].parentElement.removeChild(errors[i]);
        }

        if (event.target.status == 200) {
            var response = event.target.responseText;
            var reg_list = document.getElementById("reg_list");

            // Add newly created participant to list of participants.
            var participant = document.createElement("li");
            participant.innerHTML = response + "<a id=\"" + response + "\" onclick=\"javascript:deleteParticipant(this.id)\">x</a>";
            reg_list.appendChild(participant);

            form.reset();

        } else if (event.target.status == 400) {
            var message = "Vennligst fyll ut fornavn og etternavn / Please provide given names and family name.";
            addMessage(form, "error", message);
        }
    });

    request.open("POST", "/register");
    request.send(formData);
}

function submitEmailForm(form) {
    var request = new XMLHttpRequest();
    var formData = new FormData();

    formData.append("csrf_token", form.csrf_token.value);
    formData.append("email", form.email.value);

    request.addEventListener("load", function(event) {
        // Remove errors.
        var errors = document.getElementsByClassName("error");
        for (var i = 0; i < errors.length; i++) {
            errors[i].parentElement.removeChild(errors[i]);
        }

        if (event.target.status == 200) {
            var response = event.target.responseText;
            var email = document.getElementById("registered_email");
            if (email) {
                email.innerHTML = form.email.value;
            }
            form.reset();
            location.reload();
        } else if (event.target.status == 400) {
            var message = "Feil i epost / Error in email";
            addMessage(form, "error", message);
        }
    });

    request.open("POST", "/email");
    request.send(formData);
}

function deleteParticipant(participant) {
    var request = new XMLHttpRequest();

    request.addEventListener("load", function(event) {
        if (event.target.status == 200) {
            if (event.target.responseText == "deleted") {
                var p = document.getElementById(participant);
                p.parentElement.parentElement.removeChild(p.parentElement);
            }
        } else {
            console.log("Response:", event.target.status);
        }
    });

    request.open("POST", "/delete");
    request.send(participant);
}

function addMessage(parent, className, messageText) {
    var message = document.createElement("p");
    message.innerHTML = messageText;
    message.className = className;

    parent.appendChild(message);
}

function removeAllChildren(parent) {
    while (parent.lastChild) {
        parent.removeChild(parent.lastChild);
    }
}
