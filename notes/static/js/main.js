const menuIcon = document.getElementById('menu-icon');
const closeIcon = document.getElementById('cross-icon');
const mobileNav = document.querySelector('.mobile-nav');




menuIcon.addEventListener('click',(event)=>{
    event.preventDefault()
    mobileNav.classList.remove('hidden')
})

closeIcon.addEventListener('click',(event)=>{
    event.preventDefault()
    mobileNav.classList.add('hidden');
})

