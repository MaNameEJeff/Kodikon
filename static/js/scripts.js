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

//box-math
elems = document.getElementsByClassName("int-box");
for(let i=0;i<elems.length;i++){
    console.log(elems[i],`${i}`)
    elems[i].addEventListener("click", ()=>{
        element = elems[i];
        // console.log(element,`${i}hhhhhhhhhhhhhhhhhhh`);
        if (element.classList.contains("box-math")){
            console.log(element,`${i}ghjghjfghfhdhd`);
            document.querySelector(':root').style.setProperty('--math-eng','19%');
        }else{
            document.querySelector(':root').style.setProperty('--math-eng','54%');
        }
        element.classList.add("box-enlarge");
        var rect = element.getBoundingClientRect();
        console.log(rect.top, rect.right, rect.bottom, rect.left);
        console.log(screen.width, screen.height);
        element.style.position = "fixed";
        element.style.width = "100vw";
        element.style.height = "100vh";
        element.style.left = "0px";
        element.style.top = "0px";
        element.style.margin = "0px 0px 0px 0px";
        
        setTimeout(()=>{
            if (element.classList.contains("box-math"))
                location.href = "math";
            else
                location.href = "eng";
        },800);
    });
}

colors = ['red','green','yellowgreen','blue','lightblue',]

async function setUserName(){
    await fetch('../static/js/user.json')
    .then((response) => response.json())
    .then((json) => {
        document.getElementById("userName").innerHTML = json.userName;
    });
}