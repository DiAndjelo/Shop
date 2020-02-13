$(document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);


    function basketUpdating(product_id, nmb, is_delete){
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete){
            data["is_delete"] = true;
        }

         var url = form.attr("action");

         $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 console.log("OK");
                 console.log(data.products_total_nmb);
                 if (data.products_total_nmb || data.products_total_nmb == 0){
                    $('#basket_total_nmb').text(data.products_total_nmb);
                     console.log(data.products);
                     $('.basket-items').html("");
                     $.each(data.products, function(k, v){
                        $('.wd-item-list').append("<div class='media'><img style='max-width: 68px' class='d-flex mr-3' src='"  +
                        "' alt='cart-img'><div class='media-body'><h6 class='mt-0 list-group-title'>" + v.name + " Qty:" + v.nmb + " " +
                        "</h6><div class='cart-price'>$" + v.price_per_item*v.nmb +
                        "</div></div>" +
                        "<a class='delete_item' href='' data-product_id='"+v.id+"'>x</a>" +
                        "</div>");
                     });
                 }

             },
             error: function(){
                 console.log("error")
             }
         })

    }

    form.on('submit', function(e){
        e.preventDefault();
        var nmb = $('#number').val();
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_img = submit_btn.data('product_img');

        basketUpdating(product_id, nmb, is_delete=false)

    });


     $(document).on('click', '.delete_item', function(e){
         e.preventDefault();
         product_id = $(this).data("product_id");
         nmb = 0;
         basketUpdating(product_id, nmb, is_delete=true)
     });

    function calculatingBasketAmount(){
        var total_order_amount = 0;
        $('.total-product-in-basket-amount').each(function() {
            total_order_amount = total_order_amount + parseFloat($(this).text());
        });
        console.log(total_order_amount);
        $('#total_order_amount').text(total_order_amount.toFixed(2));
    }

    $(document).on('change', ".product-in-basket-nmb", function(){
        var current_nmb = $(this).val();
        console.log(current_nmb);

        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
        console.log(current_price);
        var total_amount = parseFloat(current_nmb*current_price).toFixed(2);
        console.log(total_amount);
        current_tr.find('.total-product-in-basket-amount').text(total_amount);

        calculatingBasketAmount();
    });


    calculatingBasketAmount();

});
