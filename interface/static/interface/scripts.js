const header = document.querySelector("header");
window.addEventListener("scroll", function() {
    header.classList.toggle("sticky", window.scrollY > 0);
})

const pageType = document.querySelector("#page-type");
if (pageType.innerHTML === 'blog') {
    document.querySelector("#navbar-blog").className = 'active';
} else if (pageType.innerHTML === 'index') {
    document.querySelector("#navbar-index").className = 'active';
} else if (pageType.innerHTML === 'aboutus') {
    document.querySelector("#navbar-about-us").className = 'active';
}

