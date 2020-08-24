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
                var submitSpan = thisForm.find('.submit-span')
                if(data.added)
                    submitSpan.html('<button type="submit" style="background-color: #ee6666">Remove</button>')
                else 
                    submitSpan.html('<button type="submit"\n style="background-color: lightgreen">Add to cart</button>')
            },
            error: function (errorData){
                console.log("Error\n" + errorData)
            }
        })
    })

})