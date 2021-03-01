<template>
 <div id='denglu'>
<div class="login">
	<div class="container-login100">
		<div class="wrap-login100">
			<div class="login100-pic js-tilt" data-tilt>
				<img src="static/img/img-01.png" alt="">
			</div>

			<form class="login100-form validate-form">
				<span class="login100-form-title">
				</span>

				<div class="wrap-input100 validate-input">
					<input class="input100" type="text" id="account" name="account" placeholder="账号">
					<span class="focus-input100"></span>
					<span class="symbol-input100">
						<i class="fa fa-user" aria-hidden="true"></i>
					</span>
				</div>

				<div class="wrap-input100 validate-input">
					<input class="input100" type="password" id="password" name="password" placeholder="密码">
					<span class="focus-input100"></span>
					<span class="symbol-input100">
						<i class="fa fa-lock" aria-hidden="true"></i>
					</span>
				</div>
				<div style="color: darkgrey;">
					<input type="checkbox" id="remember_pw">Remember me
				</div>
				
				<div class="container-login100-form-btn">
					<button type="button" id="btn_login" class="login100-form-btn" @click="Get_Login()">
						登录
					</button>
				</div>

				<div class="p-t-12">
<!--					<a href="#" class="txt2">忘记密码</a>-->
					<div class="text-center">
						<button class="txt2 btn" type="button"  data-toggle="modal" data-target="#myModal" >
							忘记密码？
						</button>
					</div>
					<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
						<div class="modal-dialog" role="document">
							<div class="modal-content"  style="background-image: linear-gradient(to top, #f3e7e9 0%, #e3eeff 99%, #e3eeff 100%);">
								<div class="modal-header">
									<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
									<h4 class="modal-title" id="myModalLabel">Finding Password</h4>
								</div>
								<div class="modal-body">
									<form class="form-horizontal">
										<div class="form-group">
											<label class="col-sm-2 control-label">账号</label>
											<div class="col-sm-10"  style="width: 50%">
												<input type="text" class="form-control" id="f_account" placeholder="account">
											</div>
										</div>
										<div class="form-group" style="padding-top: 40px; ">
											<label class="col-sm-2 control-label">昵称</label>
											<div class="col-sm-10"  style="width: 50%">
												<input type="text" id="nick_name" class="form-control"  placeholder="nick_name" >
											</div>
										</div>
										<div class="form-group" style="padding-top: 40px;">
											<label class="col-sm-2 control-label">电话</label>
											<div class="col-sm-10"  style="width: 50%">
												<input type="text" id="tel" class="form-control"  placeholder="telephone" >
											</div>
										</div>
										<div class="form-group" style="padding-top: 40px; margin-left: 30%;">
											<button type="button" class="btn btn-default" @click="findPassword()">确认</button>
										</div>

									</form>

								</div>
								<div class="modal-footer">
									<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
								</div>
							</div>
						</div>
					</div>
				</div>

				<div class="text-center p-t-136">
					<router-link class="txt2" to="/login">
							还没有账号？立即注册
						<i class="fa fa-long-arrow-right m-l-5" aria-hidden="true"></i>
					</router-link>
				</div>
			</form>
		</div>
	</div>
</div>

  </div>
</template>

<script>
import emit from '../../Emit/emit.js'
export default {
  name: 'denglu',
  data () {
    return {
      msg:'Welcome to Your Vue.js App'
    }
  },
  methods:{
    //   huancun(){
    //       console.log(this)
    //   },
       Get_Login() {

    var accountValue = document.getElementById('account').value;
    var passwordValue = document.getElementById('password').value;
    var that=this;

    var finalUrl ="http://129.28.101.21:5000/api/login?account="+accountValue+"&password="+passwordValue;

    if(accountValue.length === 0){
        alert("用户名不能为空！");
    }else if (passwordValue.length === 0){
        alert("密码不能为空！");
    }else if (accountValue.length !== 0 && passwordValue.length !== 0) {
        $.ajax({

            url: finalUrl,
            type: "GET",
             xhrFields:{
              withCredentials:true
          },
            dataType: "json",
            success: function (responseData) {
                if (responseData["status"])
                {
				  console.log(responseData,responseData.user)
				  setTimeout(function(){
					  emit.$emit("user",responseData.user)
				  },2)
                 
                    if (responseData["is_login"]) {
                        //登陆成功，则跳转到游戏首页
                       that.$router.push({path:"/index"})
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

//   let login = () => {
//   let name = document.getElementById('account');
//   let password = document.getElementById('password');
// };
/**
 * 保存用户名和密码
 */
// let fun=()=>5
// console.log(fun())
// console.log(that.$("#remember_pw").val())

// if(that.$("#remember_pw").val()==="on"){
//     var setCookie = (name, value) => {
//   let Days = 30;
//   let exp = new Date();
//   let date = Math.round(exp.getTime() / 1000) + Days * 24 * 60 * 60;
//   const cookie = {
//     url: "http://www.github.com",
//     name: name,
//     value: value,
//     expirationDate: date
//   };
//   session.defaultSession.cookies.set(cookie, (error) => {
//     if (error) console.error(error);
//   });
// };

//     var saveNameAndPassword = () => {
//     let name = document.getElementById('account').value;
//     let password = document.getElementById('password').value;
//     setCookie('name', name);
//     setCookie('password', password);
//     };
//     saveNameAndPassword();
// }


// /**
//  * 获得
//  */
// let getCookies = () => {
//   session.defaultSession.cookies.get({ url: "http://www.github.com" }, function (error, cookies) {
//     console.log(cookies);
//     if (cookies.length > 0) {
//       let name = document.getElementById('name');
//       name.value = cookies[0].value;
//       let password = document.getElementById('password');
//       password.value = cookies[1].value;
//     }
//   });
// };

// /**
//  * 保存cookie
//  * @param name  cookie名称
//  * @param value cookie值
//  */
// // let setCookie = (name, value) => {
// //   let Days = 30;
// //   let exp = new Date();
// //   let date = Math.round(exp.getTime() / 1000) + Days * 24 * 60 * 60;
// //   const cookie = {
// //     url: "http://www.github.com",
// //     name: name,
// //     value: value,
// //     expirationDate: date
// //   };
// //   session.defaultSession.cookies.set(cookie, (error) => {
// //     if (error) console.error(error);
// //   });
// // };

// getCookies();




},
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
findPassword() {
    var accountValue = document.getElementById('f_account').value;
    var nick_nameValue = document.getElementById('nick_name').value;
    var telValue = document.getElementById('tel').value;
console.log(accountValue,nick_nameValue,telValue)
	var findUrl ="http://129.28.101.21:5000/api/forgetPassword?account="+accountValue+"&nick_name="+nick_nameValue+"&tel="+telValue;
	

    this.$.ajax({

        url: findUrl,
        type: "GET",
		dataType: "json",
		 xhrfields:{
              withCredentials:true
		  },
		 
        success: function (responseData) {
            console.log(responseData,responseData.status);
            if (responseData.status) {
                if (responseData.msg === "get password  success")
                {
					
                    alert("您的密码是"+responseData.password);
                }else if (responseData.msg === 'info error')
                {
                    alert("输入信息有误！");
                }
            }else{
				alert("输入信息有误！")
			}
        },
        //contentType: "application/json; charset=utf-8",
        error: function () {
            console.log("请求失败！");
        }
    });
}


  }
}
</script>

<style  scoped>
@import "../../css/font-awesome.min.css";
@import "../../css/util.css";
@import "../../css/register.css";
@import "../../css/login.css";
</style>
