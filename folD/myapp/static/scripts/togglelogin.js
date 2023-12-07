document.addEventListener('DOMContentLoaded', function () {
    let element = document.querySelector(".LOGIN_label");
    let circle = document.querySelector(".LOGIN_moving_circle");

    let login = document.getElementsByClassName("lgn");
    let register = document.getElementsByClassName("rgstr");

    let count = 0;

    element.addEventListener("click", function () {
        circle.classList.toggle('clicked')
        
        if (count === 0) {
            for (let i = 0; i < register.length; i++) {
                register[i].classList.add("on");
            }
            for (let i = 0; i < login.length; i++) {
                login[i].classList.add("off");
            }
            count = 1;
        } else {
            for (let i = 0; i < register.length; i++) {
                register[i].classList.remove("on");
            }
            for (let i = 0; i < login.length; i++) {
                login[i].classList.remove("off");
            }
            count = 0;
        }
    });
});