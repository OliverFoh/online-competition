<template>
 <div id='login'>   
<div class="login">
	<div class="container-login100">
		<div class="wrap-login100">
			<div class="login100-pic js-tilt" data-tilt>
				<img src="static/img/img-01.png" alt="IMG">
			</div>

			<form class="login100-form validate-form" action="/index">
<!--				<span class="login100-form-title">-->
<!--					用户注册-->
<!--				</span>-->

				<div class="wrap-input100 validate-input">
					<input class="input100 inputer zhanghao" type="text" id="account" name="account" placeholder="账号">
                   <img class="tubiao" src="static/img/icon/zhanghao.png" alt=""/>
                    <span class="jinggao zhangjing">账号必须是8位！</span>
					<!-- <span class="focus-input100"></span>
					<span class="symbol-input100">
						<i class="fa fa-user" aria-hidden="true"></i>
					</span> -->
				</div>

				<div class="wrap-input100 validate-input">
					<input class="input100" type="text" id="nick_name" name="nick_name" placeholder="昵称">
                    
					<span class="focus-input100"></span>
					<span class="symbol-input100">
						<i class="fa fa-address-book" aria-hidden="true"></i>
					</span>
				</div>

				<div class="wrap-input100 validate-input">
					<input class="input100" type="password"  id="password" name="pass" placeholder="密码">
					<span class="focus-input100"></span>
					<span class="symbol-input100">
						<i class="fa fa-lock" aria-hidden="true"></i>
					</span>
				</div>



				<div class="wrap-input100 validate-input">
					<input class="input100 tel inputer" @change="zhengze()" type="text" id="tel" name="tel" placeholder="电话号码">
                    <img class="tubiao" src="static/img/icon/dianhua.png" alt=""/>
                    <span class="jinggao teljing">电话号码格式不对哦！</span>
					<!-- <span class="focus-input100"></span>
					<span class="symbol-input100">
						<i class="fa fa-phone" aria-hidden="true"></i>
					</span> -->
				</div>
				
				<div class="container-login100-form-btn">
					<button type="button" id="btn_register" class="login100-form-btn" @click="Register()">
						注册
					</button>
				</div>
                <span class="go"><router-link to="/">已有账号，去登录</router-link></span>
			</form>
		</div>
	</div>
</div>
 </div>
</template>

<script>

export default {
  name: 'login',
  data () {
    return {
     
    }
  },
  methods:{
      zhengze(){
            
            var g=this.$(".tel").val().match(/^[1][3548][0-9]{9}$/);
            //console.log(g);
            if(g==null){
                this.$(".teljing").css({
                    display:"block"
                })
            }else{
                 this.$(".teljing").css({
                    display:"none"
                })
            }
             var z=this.$(".zhanghao").val().match(/[0-9]{8}/);
            //console.log(g,z);
            if(z==null){
                this.$(".zhangjing").css({
                    display:"block"
                })
            }else{
                this.$(".zhangjing").css({
                    display:"none"
                })
            }
      },
	Register() {
   //window.location.href ='../index/index.html'
    var accountValue = document.getElementById('account').value;
    var passwordValue = document.getElementById('password').value;
    var nick_nameValue = document.getElementById('nick_name').value;
    var telValue = document.getElementById('tel').value;
	var that=this;
    //var postUrl = "http://129.28.101.21:5000/api/register?account="+accountValue+"&password="+passwordValue+"&nick_name="+nick_nameValue+"&tel="+telValue;
     var g=this.$(".tel").val().match(/^[1][3548][0-9]{9}$/);
     var z=this.$(".zhanghao").val().match(/^[0-9]{8}$/);
           // console.log(g,z);
            if(g==null){
                this.$(".teljing").css({
                    display:"block"
                })
            }
             if(z==null){
                this.$(".zhangjing").css({
                    display:"block"
                })
            }
    if(g!=null&& passwordValue.length !== 0 && nick_nameValue.length !== 0 && z!=null)
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

             xhrfields:{
              withCredentials:true
          },
            dataType: 'json',
            contentType: 'application/json;charset=UTF-8 ',
            success: function (responseData) {
                 //alert(responseData.msg);
                console.log(responseData);
                if (responseData["status"]){
                    if (responseData["msg"] === "Data insertion success") {

                        that.$router.push({path:"/"});
                    } else if (responseData["msg"] === "Account had been exist") {
						window.alert('该账号已注册，请重新注册');
						console.log(1)
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

  }
}
</script>

<style lang="scss" scoped>
@import "../../css/font-awesome.min.css";
@import "../../css/util.css";
@import "../../css/register.css";
.go{
    font-size: 12px!important;
    color: green;
    margin: 0.5rem 0 0 2rem;
}
.inputer{
    position: relative !important;
}
.tubiao{
    width: 15px;
    height: 15px;
    position: absolute;
    left: 33px;
    top: 50%;
    margin-top: -7.5px;
}

.jinggao{
    color: red;
    font-size: 12px;
    margin: 0 0 0 3rem;
    display: none;
}

</style>
