    function delete_product(productId) {
        $.ajax({
            url: '/craft_admin/deleteProduct',
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