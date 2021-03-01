<template>
 <div id='xiugai'>
     <div class="x-title" @click="emit()"><router-link to="/index"><img src="static/img/fanhui.png" alt=""/><span>首页</span></router-link></div>
  <div class="x-block">
       <div class="face-block">
                       <img :src='"http://"+this.user.avatarUrl' alt="加载失败" id="userface"/>
                       <input type="file" name="touxiang" id="file" @change="changepic()"/><br>
                           
                       <input type="submit" value="确认修改" @click="submitinfo(),xiugai(),picture()"/>
                       
          </div>
          <ul>
                
                <li><span>新密码：</span><input class="pwd" type="password" name="pwd"/></li>
                <li><span>昵称：</span><input class="name" type="text" name="nicheng" :value="this.msg.nick_name"/></li>
                <li><span>电话：</span><input class="tel" type="text" name="qitaxinxi" @change="zhengze()" :value="this.msg.tel"/></li>
                <span class="jinggao teljing">电话号码格式不对哦！</span>
          </ul>
         
         
         
     
     
  </div>
  </div>
</template>

<script>
import emit from '../../Emit/emit.js'
export default {
  name: 'xiugai',
  mounted(){

      this.$("#xiugai").height(window.innerHeight);
      console.log(window.innerHeight);
        // $("#file").change(function () {
                  
        //         changepic();
        //     });
         var that=this;
         emit.$on("user",(res)=>{
          console.log(res);
          that.user=res;
          that.$nextTick(function(){
         that.user=res;
            })
          })
      this.$.ajax({
          url:"http://129.28.101.21:5000/api/user/viewPersonInfo",
          type:"get",
          xhrFields:{
              withCredentials:true
          },
          async:true,
          crossDomain:true,
            // data: null,
            datatype:"json",
            contentType: 'application/json;charset=UTF-8 ',
            success:function(result){
                //console.log(result.data)
                that.msg=result.data;
                
            }
      })
    
     
  },
  data () {
    return {
      msg:{},
        user:{}
    }
  },
  methods:{
      zhengze(){
    
	var that=this;
   
     var tel=this.$(".tel").val().match(/^[1][3548][0-9]{9}$/);
     
           // console.log(g,z);
            if(tel==null){
                this.$(".teljing").css({
                    display:"block"
                })
            }else{
                 this.$(".teljing").css({
                    display:"none"
                })
            }
      },
            emit(){
                var that=this;
                setTimeout(function(){
                    emit.$emit("user",that.user);
                    emit.$emit("msg",that.msg)
                },2);
                
            },
            submitinfo(){
                   if(confirm("确认修改资料？")){
                       return true;
                   }else{
                       return false;
                   }
               },
                //实现图片预览
            changepic(e) {
               // 
                var that=this;
                var reads = new FileReader();
                var f = this.$("#file")[0].files[0];
                reads.readAsDataURL(f);
                var that=this;
                reads.onload = function (e) {
                    //console.log(this.result)
                    //console.log(e)
                    that.$("#userface").attr("src", this.result);
                };
                
            },
            xiugai(){
                var that=this;
                var newpwd=this.$(".pwd").val();
                var newname=this.$(".name").val();
                var newtel=this.$(".tel").val();
                console.log(newpwd,newname,newtel);
                that.$.ajax({
                    url:"http://129.28.101.21:5000/api/user/modifyPersonInfo",
                    type:"POST",
                    data:newpwd==""?JSON.stringify({
                        "new_nick_name":newname,
                        "new_tel":newtel
                    }):JSON.stringify({
                        "new_password":newpwd,
                        "new_nick_name":newname,
                        "new_tel":newtel
                    }),
                    xhrFields:{
                        withCredentials:true
                    },
                    crossDomain:true,
                    datatype:"json",
                    async:true,
                    contentType: 'application/json;charset=UTF-8 ',
                    success:function (res){
                        console.log(res);
                       console.log(that.msg);
                    //    that.msg.new_password=newpwd;
                       that.msg.nick_name=newname;
                       that.msg.tel=newtel;
                       that.user.nick_name=newname;
                       alert("信息修改成功！")
                    }
                })
            },
            picture(){
                var that=this;
                var formData = new FormData();
            var file = document.getElementById('file').files[0];
            // var id_token = $('#id_token').val();
            console.log(file)
            formData.append("file", file);
            // formData.append("id_token", id_token);
            console.log(formData)
            if(file==undefined){
                return;
            }
            that.$.ajax({
            url: "http://129.28.101.21:5000/api/user/modifyPersonAvatar",
            type: "POST",
            data: formData,
            dataType: "json",
            xhrFields:{
                withCredentials:true
            },
            crossDomain:true,
             cache: false,//上传文件无需缓存
            processData: false,//用于对data参数进行序列化处理 这里必须false
            contentType: false, //必须*/
            success: function (data) {
                     console.log(data);
                    alert("上传完成");
                    console.log(that.user);
                    that.user.avatarUrl=data.avatarUrl;
                    console.log(that.user)
            // $("#dianziqianmingPath").val(data.msg)
                    }
                }) 

            
}
}
}
</script>

<style lang="scss" scoped>
.jinggao{
    font-size: 14px;
    color: red;
    display: none;
}
#xiugai{
    position: relative;
    width: 100%;
    // height: 100%;
   background-image: linear-gradient(-225deg, #7DE2FC 0%, #B9B6E5 100%);
    box-sizing: border-box;
    overflow: hidden;
    
    .x-title{
        position: fixed;
        left: 0;
        top: 0;
        width: 100%;
        height: 8rem;
       background-image: linear-gradient(to right, #74ebd5 0%, #9face6 100%);
        line-height: 8rem;
        padding: 0 3rem;

        img{
            width: 2.5rem;
            height: 2.5rem;
            vertical-align: middle;
            
        }
        span{
            color: white;
            font-size: 20px;
            vertical-align: middle;
        }
    }
    .x-block{
        width: 100%;
        height: 100%;
        padding: 12rem 0;
        box-sizing: border-box;
        overflow: hidden;
        display: flex;
        flex-direction: row;
        // form{
        //     width: 100%;
        //     height: 100%;
        //     padding: 10rem 6rem;
            ul{
                width: 100%;
                text-align: center;
                flex: 1;
                li{
                    list-style: none;
                    padding: 1.5rem 0;
                    span{
                        display: inline-block;
                        width: 12rem;
                        text-align: right;
                        font-size: 22px;

                    }
                    input{
                        width: 30rem;
                        height: 3rem;
                        border-radius: 8px;
                        border: 1px solid black;
                        padding: 0 1rem;
                        color: black;
                        outline: none;
                    }
                }
            }
            .face-block{
                flex: 1;
                width: 100%;
                text-align: center;
                img{
                    width: 10rem;
                    height: 10rem;
                    display: inline-block;
                    border-radius: 50%;
                }
                input[type=file]{
                    display: inline-block;
                    outline: none;
                }
                input:last-child{
                    position: absolute;
                    left: 50%;
                    bottom: 10rem;
                    margin-left: -2.5rem;
                     padding: 1rem 0;
                    width:12rem;
                    background-image: linear-gradient(to right, #ed6ea0 0%, #ec8c69 100%);
                    border-radius: 10px;
                    color: white;
                    font-size: 18px;
                    outline: none;
                    margin-top: 3rem;
                }
                
            }
        //}
    }
}
</style>
