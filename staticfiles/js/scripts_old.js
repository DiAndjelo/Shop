$(document).ready(function () {
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function (prDf) {
        prDf.preventDefault();
        console.log('123');
        var nmb = $('#number').val();
        console.log(number);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('product_name');
        var product_price = submit_btn.data('product_price');
        var product_img = submit_btn.data('product_img');
        console.log(product_img);
        console.log(product_id);

        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");
        console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.products_total_nmb)
                if (data.products_total_nmb){
                    $('#basket_total_nmb').text(data.products_total_nmb)
                }
                $('.wd-item-list').append("<div class='media'><img style='max-width: 68px' class='d-flex mr-3' src='" + product_img +
                "' alt='cart-img'><div class='media-body'><h6 class='mt-0 list-group-title'>" + product_name + " Qty:" + nmb + " " +
                "</h6><div class='cart-price'>$" + product_price*nmb +
                "</div></div>" +
                "<a class='delete_item' href=''>x</a>" +
                "</div>");
            },
            error: function () {
                console.log("error")
                
            }
        });


    })
});

$(document).on('click', '.delete_item', function (prDf) {
   prDf.preventDefault();
   $(this).closest('div').remove();
});