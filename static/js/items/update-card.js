import refreshCart from '/static/js/carts/home.js'

$(document).ready(function () {
    var itemForm = $('.form-item-ajax')

    itemForm.submit(function (event) {
        event.preventDefault()
        var thisForm = $(this)
        var method = thisForm.attr('method')
        var data = thisForm.serialize()
        var actionEndPoint = thisForm.attr('action')

        $.ajax({
            url: actionEndPoint,
            data: data,
            method: method,
            success: function (data) {
                var submitSpan = thisForm.find('.submit-span')
                if (data.added) {

                    submitSpan.html('<button type="submit" style="background-color: #ee6666">Remove</button>')
                }
                else if(!data.added && window.location.href.indexOf('cart') !== -1){

                    submitSpan.find('div').addClass('add-item')
                    refreshCart(data.id)
                }
                else if(!data.added) {

                    submitSpan.html('<button type="submit" style="background-color: lightgreen">Add to cart</button>')
                }

                // count and edit the number of items in cart
                var countItems = $('.items-counter')
                countItems.text(data.cart_total)

            },
            error: function (errorData) {
                $.alert({
                    title: 'Oops!',
                    content: 'Something went wrong...',
                    theme: 'supervan',
                })
            }
        })
    })
})