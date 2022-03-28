    function update_product(productId) {
        console.log(productId)

        $.ajax({
            url: '/craft_seller/UpdateProduct',
            type: 'POST',
            data: {
                productId
            },
            success: function(response) {
                console.log(response)
                alert(response.message);
            }
        })

    }