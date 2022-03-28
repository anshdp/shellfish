function AddToCart(productId) {
    // quantity = document.getElementById('quantity').value
    $.ajax({
        url: '/craft/add_to_cart',
        type: 'POST',
        data: {
            productId,

        },
        success: function(response) {
            console.log(response)
            alert(response.message);
        }
    })
}