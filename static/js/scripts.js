/*!
    * Start Bootstrap - SB Admin v7.0.5 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2022 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            clsss = document.getElementsByClassName('container-interactive')[0].classList
            clsss.toggle('container-interactive-nonav');
            clsss.toggle('container-interactive-wnav');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});


document.getElementsByClassName("box-math")[0].addEventListener("click", function (){
    element = document.getElementsByClassName("box-math")[0]
    element.classList.add("box-math-enlarge");
    var rect = element.getBoundingClientRect();
    console.log(rect.top, rect.right, rect.bottom, rect.left);
    console.log(screen.width, screen.height);
    element.style.position = "fixed";
    element.style.width = "100vw";
    element.style.height = "100vh";
    element.style.left = "0px";
    element.style.top = "0px";
    element.style.margin = "0px 0px 0px 0px";
    setTimeout(()=> {open("../../templates/interactive_math.html");},3500);
    
})
