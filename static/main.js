// Scroll Top Button

function showScrollTop(){
    if (document.body.scrollTop > 400 || document.documentElement.scrollTop > 400){
        document.getElementById('scrollTop').style.opacity = '1';
        document.getElementById('scrollTop').style.visibility = 'visible';
    } else{
        document.getElementById('scrollTop').style.opacity = '0';
        document.getElementById('scrollTop').style.visibility = 'hidden'; 
    }
}

window.addEventListener('scroll', showScrollTop)

function scrollToTop(){
    window.scrollTo(0,0);
}




// Navbar change on scroll to colour

function changeHoverColor(newColor) {
    const root = document.documentElement;
    root.style.setProperty('--nav-hover-color', newColor);
}

function changeSearchColor(newColor2) {
    const root = document.documentElement;
    root.style.setProperty('--search-bar-color', newColor2);
}

let nav = document.querySelector('nav');

function changeHeader() {
    if (document.body.scrollTop > 50) {
        nav.classList.add('change-header');
        changeHoverColor('#ffff');
        changeSearchColor('#4caf50');


    } else if (document.documentElement.scrollTop > 50) {
        nav.classList.add('change-header');
        changeHoverColor('#ffff');
        changeSearchColor('#4caf50');
    }
    else {
        nav.classList.remove('change-header');
        changeHoverColor('#4caf50');
        changeSearchColor('#ffff');
    }
}
window.addEventListener('scroll', changeHeader)

// Searchbar Appear Onclick

let searchbar = document.getElementById('searchbar');
let searchContainer = document.getElementById('search-container');
let placeholderTexts = ['Search "Premier League"', 'Search "Juventus"', 'Search "Bundesliga 2016"', 'Search "Real Madrid vs Barcelona"', 'Search "2014"', 'Search "Southampton"', 'Search "Bayern vs Dortmund"'];

function showSearch() {
    searchbar.classList.add('visible');
    var randomIndex = Math.floor(Math.random() * placeholderTexts.length);
    searchbar.placeholder = placeholderTexts[randomIndex];
}

function hideSearch() {
    if (!searchContainer.contains(document.activeElement)) {
        searchbar.classList.remove('visible');
    }
}

searchbar.addEventListener('mouseover', showSearch);
searchContainer.addEventListener('mouseleave', hideSearch);


// Slide In Animations

const inViewport = (entries, observer) => {
    entries.forEach(entry => {
        entry.target.classList.toggle('is-inViewport', entry.isIntersecting);
    })
}

const Obs = new IntersectionObserver(inViewport);
const obsOptions = {};

const ELs_inViewport = document.querySelectorAll('[data-inViewport]');
ELs_inViewport.forEach(EL => {
    Obs.observe(EL, obsOptions);
});

// SwiperJS Initialisation


var swiper = new Swiper('.mySwiper', {
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    loop: true,
    slidesPerView: '1.1',
    coverflowEffect: {
        rotate: 0,
        stretch: 0,
        depth: 100,
        modifier: 2.5,
        slideShadows: false,
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    autoplay: {
        delay: 2500,
    }
});


var statsswiper = new Swiper('.stats-swiper', {
    grabCursor: true,
    centeredSlides: true,
    loop: true,
    slidesPerView: 1,
    spaceBetween: 500,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});


// Remove Filters Button

function removeFilters(event) {
    event.preventDefault();
    window.location.href = "/fulldb";
}

// Submit Page Form With No Button

function submitForm(){
    document.getElementById("perpageform").submit();
}


// Explore Button Onclick Redirect To FullDB

function fulldbRedir(){
    window.location.href = "/fulldb";

}

// Advanced Search Form Error Handling And Variable Storing 

function checkFilters(event) {
    var yearFilter = document.getElementById("filteryear").value;
    var startDate = document.getElementById("start").value;
    var endDate = document.getElementById("end").value;

    if (yearFilter !== "" && (startDate !== "" || endDate !== "")) {
        event.preventDefault();
        alert("Please select either a year filter or a date range filter, not both.");
        document.getElementById("start").value = "";
        document.getElementById("end").value = "";
        document.getElementById("filteryear").value = "";
    }
}

// Go Home Button 404 Page

function homeRedir(){
    window.location.href = "/#home";

}



