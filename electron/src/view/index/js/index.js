
function Get_Login() {

    var accountValue = document.getElementById('account').value;
    var passwordValue = document.getElementById('password').value;

    var finalUrl ="http://127.0.0.1:5000/api/login?account="+accountValue+"&password="+passwordValue;

    if(accountValue.length === 0){
        alert("用户名不能为空！");
    }else if (passwordValue.length === 0){
        alert("密码不能为空！");
    }else if (accountValue.length !== 0 && passwordValue.length !== 0) {
        $.ajax({
			
            url: finalUrl,
            type: "GET",
            xhrFields: {
				withCredentials: true
						},
            dataType: "json",
            success: function (responseData) {
				console.log('登录请求已发送')
				console.log(responseData)
                if (responseData["status"])
                {
                    if (responseData["is_login"]) {
                        //登陆成功，则跳转到游戏首页
						
						window.location.href = "../start/start.html";
                    }else{

                        if (responseData["msg"] === "Account not exist")
                        {
                            alert('此用户不存在');
                            document.getElementById('account').value = '';
                            document.getElementById('password').value = '';
                        }
                        if (responseData["msg"] === "Password error")
                        {
                            alert('密码错误，请重新输入');
                            document.getElementById('password').value = '';
                        }
                    }
                }
            },
            //contentType: "application/json; charset=utf-8",
            error: function () {
                console.log("请求失败！");
            }
        });
    }



}
// var oBtn = document.getElementById('btn_login');
// oBtn.onkeydown = function(e) {
//     var ev = window.event || e;
//     var code = ev.keyCode || ev.which;
//     if (code == 116) {
//         ev.keyCode ? ev.keyCode = 0 : ev.which = 0;
//         cancelBubble = true;
//         return false;
//     }
// }
function findPassword() {
    var accountValue = document.getElementById('f_account').value;
    var nick_nameValue = document.getElementById('nick_name').value;
    var telValue = document.getElementById('tel').value;

    var findUrl ="http://129.28.101.21:5000/api/forgetPassword?account="+accountValue+"&password="+nick_nameValue+"&tel="+telValue;

    $.ajax({

        url: findUrl,
        type: "GET",
        dataType: "json",
        success: function (responseData) {
            console.log(responseData);
            if (responseData['status']) {
                if (responseData['msg'] === "get password success")
                {
                    alert(responseData['password']);
                }else if (responseData['msg'] === 'info error')
                {
                    alert("输入信息有误！");
                }
            }
        },
        //contentType: "application/json; charset=utf-8",
        error: function () {
            console.log("请求失败！");
        }
    });
}


