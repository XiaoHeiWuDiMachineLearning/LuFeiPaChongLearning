
    const CryptoJS = require('crypto-js');
    // 原始数据
    const data = '123456';
    // 生成MD5摘要
    const md5Digest = CryptoJS.MD5(data).toString();
    console.log('MD5加密:', md5Digest);
    // AES算法
    var key = CryptoJS.enc.Utf8.parse('0123456789abcdef');
    var iv = CryptoJS.enc.Utf8.parse('0123456789abcdef');
    // 待加密数据
    var plaintext = 'Hello, yuan!';
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
    console.log('AES算法:', ciphertext)