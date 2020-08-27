$(document).ready(function (){
    var searchForm = $('.mg-top').find('.search-form')
    searchInput = searchForm.find("[name='q']")
    var typingTimer;
    var typingInterval = 1500;

    searchForm.keyup(function (event){

        //key released
        clearTimeout(typingTimer)
        typingTimer = setTimeout(autoSearch, typingInterval)
    })

    searchForm.keydown(function (){

        //key pressed
        clearTimeout(typingTimer)
    })

    function autoSearch(){
        window.location.href = '/search/?q=' + searchInput.val()
    }
})