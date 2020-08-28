$(document).ready(function (){
    var searchForm = $('.mg-top').find('.search-form')
    searchInput = searchForm.find("[name='q']")
    var typingTimer;
    var typingInterval = 1500;
    var searchBtn = searchForm.find("[type='submit']")

    searchForm.keyup(function (event){

        clearTimeout(typingTimer)
        typingTimer = setTimeout(autoSearch, typingInterval)
    })

    searchForm.keydown(function (){

        //key pressed
        clearTimeout(typingTimer)
    })

    function displaySearching(){
        searchBtn.addClass('disabled')
        searchBtn.html('<i class="fa fa-spinner fa-spin"></i>')
    }

    function autoSearch(){
        displaySearching()

        setTimeout(function (){
            window.location.href = '/search/?q=' + searchInput.val()
        }, 1000)
    }
})


