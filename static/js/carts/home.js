//refresh the cart after remove an item
export default function refreshCart(id) {
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
                $('.item-row').each(function () {

                    if (id == $(this).find('button').attr('id')) {

                        $(this).text('')
                    }

                })

                cartItems.find('.total').text(data.total)
                cartItems.find('.subtotal').text(data.subtotal)
            } else {
                $('.table').text('Cart is empty')
            }
        },
        error: function (errorData) {
            alert({
                    title: 'Oops!',
                    content: 'Something went wrong...',
                })
        }
    })
}