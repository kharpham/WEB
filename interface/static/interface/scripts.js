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
    
let list = document.querySelector('.slide-list');
let items = document.querySelectorAll('.slide');
let dots = document.querySelectorAll('.dots li');
let prev = document.getElementById('prev');
let next = document.getElementById('next');

let activeSlide = 0;
let lengthItems = items.length;

next.onclick = function() {
    if (activeSlide + 1 >= lengthItems) {
        activeSlide = 0;
    }
    else {
        activeSlide += 1;
    }
    reloadSlider();
    dots[activeSlide].className = "dot-active";

}

prev.onclick = function() {
    if (activeSlide <= 0) {
        activeSlide = lengthItems - 1;
    }
    else {
        activeSlide -= 1;
    }
    reloadSlider();
}
let refreshSlider = setInterval(() => {
    next.click()
}, 5000);

function reloadSlider() {
    let checkLeft = items[activeSlide].offsetLeft;
    list.style.left = -checkLeft + 'px';
    let lastActive = document.querySelector('.dot-active');
    lastActive.classList.remove('dot-active');
    dots[activeSlide].classList.add('dot-active');
    clearInterval(refreshSlider);
    refreshSlider = setInterval(() => {
        next.click()
    }, 5000);
}

dots.forEach((dot, key) => {
    dot.addEventListener('click', function() {
        activeSlide = key;
        reloadSlider();
    })
})

