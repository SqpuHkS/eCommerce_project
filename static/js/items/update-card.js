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
                console.log("Error\n" + errorData)
            }


        })


        //refresh the cart after remove an item
        function refreshCart(id) {
            var cartItems = $('.cart-body')

            var refreshCartUrl = 'api/cart/'
            var refreshCartMethod = 'GET'
            var data = {}
            $.ajax({
                url: refreshCartUrl,
                method: refreshCartMethod,
                data: data,
                success: function (data) {

                    if (data.items.length > 0) {
                        $('.item-row').each(function (){

                             if(id == $(this).find('button').attr('id') ){

                                $(this).text('')
                            }

                        })

                        cartItems.find('.total').text(data.total)
                        cartItems.find('.subtotal').text(data.subtotal)
                    }
                    else{
                        $('.cart-table').text('Cart is empty')
                    }
                },
                error: function (errorData) {
                    console.log('error')
                }
            })
        }


    })

})