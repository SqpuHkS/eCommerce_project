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
                    console.log(data.added + 'remove')
                    submitSpan.html('<button type="submit" style="background-color: #ee6666"> Remove </button>')
                } else {
                    console.log(data.added + 'add to')
                    submitSpan.html('<button type="submit"\n style="background-color: lightgreen"> Add to cart </button>')
                }

                // count and edit the number of items in cart
                var countItems = $('.items-counter')
                countItems.text(data.cart_total)

                currentPath = window.location.href

                if (currentPath.indexOf('cart') !== -1) {
                    refreshCart()
                }

            },
            error: function (errorData) {
                console.log("Error\n" + errorData)
            }
        })

        //refresh the cart after remove an item
        function refreshCart() {
            var cartItems = $('.cart-body')

            var refreshCartUrl = 'api/cart/'
            var refreshCartMethod = 'GET'
            var data = {}
            $.ajax({
                url: refreshCartUrl,
                method: refreshCartMethod,
                data: data,
                success: function (data) {
                    var row = cartItems.find('.item-rows')
                    console.log(row)
                    console.log(data)
                    if (data.items.length > 0) {
                        cartItems.find('.total').text(data.total)
                        cartItems.find('.subtotal').text(data.subtotal)
                    }
                },
                error: function (errorData) {
                    console.log('error')
                }
            })
        }


    })

})