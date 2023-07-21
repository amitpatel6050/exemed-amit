
// for menubar and slide image on front page
let show_menu = document.querySelector(".show-menu");
let closebtn = document.querySelector(".close-btn");
let setmenu = document.querySelector(".set-menus");
let slide_img = document.querySelector(".slide-image-back");

show_menu.addEventListener("click", () => {
    setmenu.classList.add("set-menus-show");
    slide_img.classList.add("slide-image-front");

})
closebtn.addEventListener("click", () => {
    setmenu.classList.remove("set-menus-show");
    slide_img.classList.remove("slide-image-front");
})

// for dropdown list in menubar
let a_menu = document.querySelector(".a-menu")
let disp_menu = document.querySelector(".display-menu");
a_menu.addEventListener("click", () => {
    disp_menu.classList.toggle("sub-menu")
})

let a_menu1 = document.querySelector(".a-menu1")
let disp_menu1 = document.querySelector(".display-menu1");
a_menu1.addEventListener("click", () => {
    disp_menu1.classList.toggle("sub-menu1")
})

// for search when screen is less than 576px to 768px
let search_val = document.querySelector(".searching")
let search = document.querySelector(".megnifier");
let sear_close = document.querySelector(".close");

search.addEventListener("click", () => {
    search_val.classList.add("searching-val");
})
sear_close.addEventListener("click", () => {
    search_val.classList.remove("searching-val");
})

// header background color change when page is scroll
function changebg() {
    let header = document.querySelector(".main-header");
    let current = window.scrollY;

    if (current > 0) {
        header.classList.add("main-header-fixed");
    } else {
        header.classList.remove("main-header-fixed");
    }
}
window.addEventListener("scroll", changebg)
