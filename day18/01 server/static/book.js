   // 获取四大名著
    // js代码  JS：事件驱动
    var dom = document.getElementsByTagName("p")[1]
    function get_page_books (page) {
        // 查询参数
        var params = {
            'page':page.toString()
        }

        // 数据加密 aes-128
        function encrypt_data(data){

            // AES算法
            var key = CryptoJS.enc.Utf8.parse('0123456789abcdef');
            var iv = CryptoJS.enc.Utf8.parse('0123456789abcdef');
            // 待加密数据
            var plaintext = JSON.stringify(data);
            // 进行AES-128加密，使用CBC模式和PKCS7填充
            var encrypted = CryptoJS.AES.encrypt(
                plaintext, key, {
                    iv: iv,
                    mode: CryptoJS.mode.CBC,
                    padding: CryptoJS.pad.Pkcs7
                }
            );
            // 获取加密后密文
            var ciphertext = encrypted.toString()
            return ciphertext
        }
        var sign = encrypt_data(params);
        params.sign = sign;
        // 发送发ajax，应该JS的代码，但是JS
        $.ajax({
            url: "http://127.0.0.1:5000/books",
            type: "get",
            data: params,
            success: function (res) {
                console.log("res:::", res)
                // dom
                var p3 = $("p").eq(-1)
                p3.html(res.map(item=>`【${item}】`))

            }
        })

    }