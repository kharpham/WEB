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


if (next !== null && prev !== null && dots !== null) {
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
}

let total_price = 0;
let cart_items = document.querySelectorAll(".item_price");
cart_items.forEach(cart_item  => {
    total_price += parseFloat(cart_item.textContent);
});
let sum_price = document.querySelector("#total_price");
if (sum_price) {
    sum_price.innerHTML = total_price.toLocaleString('en-US');
}


// Get product's number of likes
document.querySelectorAll('.number-likes').forEach(get_likes);

function get_likes(element) {
  let product_id = element.parentNode.id;
  fetch(`product_info/${product_id}`)
  .then(response => response.json())
  .then(product => {
    element.innerText = product.number_likes;
  });
}

// Like/ unlike products
document.querySelectorAll(".like-btn2").forEach(function(element) {
    element.addEventListener('click', interactProduct);
});
document.querySelectorAll(".unlike-btn").forEach(function(element) {
    element.addEventListener("click", interactProduct);
});
document.querySelectorAll(".like-btn").forEach(function(element) {
    element.addEventListenter("click", interactProduct);
});

function interactProduct(element) {
    let username = document.getElementById("user_username").innerHTML;
    let product_id = this.parentNode.id;
    console.log(product_id);
    fetch(`product_info/${product_id}`)
    .then(response => response.json())
    .then(product => {
        let likes = product.likes;
        let number_likes = product.number_likes;
        // user doens't like the product yet => unlike button
        if (!likes.includes(username)) {
            likes.push(username);
            number_likes++;
            this.className = 'like-btn';
            fetch(`product_info/${product_id}`, {
                method: "PUT",
                body: JSON.stringify({
                    likes: likes,
                    number_likes: number_likes,
                })
            });
            get_likes(this.parentNode.querySelector('.number-likes'));
        }
        else {
            let index = likes.indexOf(username);
            likes.splice(index, 1);
            console.log(likes);
            number_likes--;
            console.log(number_likes);
            this.className = 'unlike-btn';
            fetch(`product_info/${product_id}`, {
                method: "PUT",
                body: JSON.stringify({
                    likes: likes,
                    number_likes: number_likes,
                })
            });
            get_likes(this.parentNode.querySelector('.number-likes'));
        }
    })
}


