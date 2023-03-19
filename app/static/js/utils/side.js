all_side = document.querySelectorAll('ul[class="navbar-nav"] > li > a')
currentHref = location.pathname


all_side.forEach(element => {
    element.classList.remove('active')
    if (element.pathname == currentHref){
        element.classList.add('active')
    }
});
