function Post_Register() {
   //window.location.href ='../index/index.html'
    var accountValue = document.getElementById('account').value;
    var passwordValue = document.getElementById('password').value;
    var nick_nameValue = document.getElementById('nick_name').value;
    var telValue = document.getElementById('tel').value;

    //var postUrl = "http://129.28.101.21:5000/api/register?account="+accountValue+"&password="+passwordValue+"&nick_name="+nick_nameValue+"&tel="+telValue;

    if(accountValue.length !== 0 && passwordValue.length !== 0 && nick_nameValue.length !== 0 && telValue.length !== 0)
    {
        $.ajax({
            url: "http://129.28.101.21:5000/api/register",
            type: 'POST',

            data: JSON.stringify({
                'account': accountValue,
                'password': passwordValue,
                'nick_name': nick_nameValue,
                'tel': telValue
            }),


            dataType: 'json',
            contentType: 'application/json;charset=UTF-8 ',
            success: function (responseData) {
                 //alert(responseData.msg);
                console.log(responseData);
                if (responseData["status"]){
                    if (responseData["msg"] === "Data insertion success") {

                        window.location.href = '../index/index.html';
                    } else if (responseData["msg"] === "account had been exist") {
                        alert('该账号已注册，请重新注册');
                        var arrValue = document.getElementsByTagName('input');
                        for(var a of arrValue) {
                            a.value = '';
                        }
                    }
                }else if (!responseData["status"]) {
                    alert('注册失败，请重新注册');
                }
            },
            error: function () {
                console.log("注册失败！");
            }

        });
    }else{
        alert('请完善信息');
    }

}



// var oBtn = document.getElementById('btn_register');
// oBtn.onkeydown = function(e) {
//     var ev = window.event || e;
//     var code = ev.keyCode || ev.which;
//     if (code == 116) {
//         ev.keyCode ? ev.keyCode = 0 : ev.which = 0;
//         cancelBubble = true;
//         return false;
//     }
// }