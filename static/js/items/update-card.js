$(document).ready(function (){
    var itemForm = $('.form-item-ajax')

    itemForm.submit(function (event){
        event.preventDefault()
        var thisForm = $(this)
        var method = thisForm.attr('method')
        var data = thisForm.serialize()
        var actionEndPoint = thisForm.attr('action')

        $.ajax({
            url: actionEndPoint,
            data: data,
            method: method,
            success: function (data){
                console.log('success\n' + data)
            },
            error: function (errorData){
                console.log("Error\n" + errorData)
            }
        })
    })

})