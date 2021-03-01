<template>
 <div id='app'>
   <div class="s-block">
       <div class="top-block">
           <div class="kong-block"></div>
           <div class="s-title">灾害常识答题平台</div>
            <div class="s-touxiang">
                <div class="caidan">菜单
                    <div class="xiala">
                   <router-link to="/geren"> <span  @click="emit()">个人主页</span></router-link>
                    <span class="tuichu" @click="back()">退出登录</span>
                    
                </div>
                </div>
                
               <!-- <router-link to="/geren"><span>个人主页</span></router-link> -->
                <img :src='"http://"+this.msg.avatarUrl' alt="加载失败"/>
                <span>{{this.msg.nick_name}}</span>
                
            </div>
       </div>
       <div class="bottom-block">
           <div class="left-block">
               <router-link to="/game"><button class="pipei" @click="emit()">开始匹配</button></router-link>
               <audio class="mp3" src="static/mp3/6.mp3"></audio>
           </div>
           <div class="right-block">
               <div class="paihang-block">
                  <div class="top">
                      <span @click="xuanxiangka(index)" v-for='(item,index) in sheng' :key="index">{{item.name}}</span>
                      
                  </div>
                   <div class="bottom">
                       <ul class="title">
                           <li><span>头像</span></li>
                            <li><span>账号</span></li>
                             <li><span>昵称</span></li>
                              <li><span>胜率</span></li>
                           
                       </ul>
                       <ul class="pipei">
                           <li v-for='(item,index) in this.pipei' :key="index">
                               <!-- <img class="huangguan" v-if="index<1" src="static/img/icon/huangguan.png" alt=""/>
                               <img class="huangguan" v-if="index<2" src="static/img/icon/huangguan2.png" alt=""/> -->
                               <img class="huangguan" v-if="index<3" :src='index==0?"static/img/icon/huangguan.png":index==1?"static/img/icon/huangguan2.png":index==2?"static/img/icon/huangguan3.png":""' alt=""/>
                              <div>
                                  <div> <img :src='"http://"+item.avatarUrl' alt=""/></div>
                               <span>{{item.user_id}}</span>
                               <span>{{item.nick_name}}</span>
                               <span>{{item.win_rate}}</span>
                              </div>
                           </li>
                       </ul>
                       <ul class="liansheng">
                           <li v-for='(items,index) in this.liansheng' :key="index">
                                 <img class="huangguan" v-if="index<3" :src='index==0?"static/img/icon/huangguan.png":index==1?"static/img/icon/huangguan2.png":index==2?"static/img/icon/huangguan3.png":""' alt=""/>
                               <div>
                                  <div> <img :src='"http://"+items.avatarUrl' alt=""/></div>
                               <span>{{items.user_id}}</span>
                               <span>{{items.nick_name}}</span>
                               <span>{{items.max_streak_num}}</span>
                              </div>
                           </li>
                       </ul>
                   </div>
               </div>
           </div>
       </div>
    </div>
    <!-- <loading></loading> -->
    
  </div>
</template>

<script>
import loading from './loading.vue'
import emit from '../../Emit/emit.js'
export default {
  name: 'app',
  components:{
      loading
  },
  
  mounted(){
      var that=this;
    
          emit.$on("user",(res)=>{
          console.log(res);
          that.msg=res;
          that.$nextTick(function(){
      
            })
          })
          
    //   this.$.ajax({
    //       url:"http://129.28.101.21:5000/api/user/viewPersonInfo",
    //       type:"GET",
    //       xhrFields:{
    //           withCredentials:true
    //       },
    //       crossDomain:true,
    //       asnyc:true,
    //       success:function(res){
    //           console.log(res);
    //           that.msg=res.data;
    //           console.log(that.msg);
    //       }
    //   })
      var type2="max_streak_num";
       this.$.ajax({
          url:"http://129.28.101.21:5000/api/rank/orderBy?"+"type="+type2,
          type:"GET",
          xhrFields:{
              withCredentials:true
          },
          async:true,
          crossDomain:true,
            // data: null,
            datatype:"json",
            contentType: 'application/json;charset=UTF-8 ',
            success:function(result){
                console.log(result.data)
                that.liansheng=result.data;
                console.log(that.pipei);
                //that.msg=result.data;
                //console.log(this.msg);
            }
      })
       var type1="win_rate";
       this.$.ajax({
          url:"http://129.28.101.21:5000/api/rank/orderBy?"+"type="+type1,
          type:"GET",
          xhrFields:{
              withCredentials:true
          },
          async:true,
          crossDomain:true,
            // data: null,
            datatype:"json",
            contentType: 'application/json;charset=UTF-8 ',
            success:function(result){
                console.log(result.data);
                that.pipei=result.data;
                console.log(that.liansheng)
                //that.msg=result.data;
                //console.log(this.msg);
            }
      })
    //   console.log(window.innerHeight)
    //   console.log(this.$("#app"))
      this.$(".s-block").height(window.innerHeight);
    //    $.ajax({
    //         url: "http://129.28.101.21:5000/api/register",
    //         type: 'POST',

    //         data: JSON.stringify({
    //             'account': accountValue,
    //             'password': passwordValue,
    //             'nick_name': nick_nameValue,
    //             'tel': telValue
    //         }),


    //         dataType: 'json',
    //         contentType: 'application/json;charset=UTF-8 ',
    //         success: function (responseData) {
    //              //alert(responseData.msg);
    //             console.log(responseData);
    //             if (responseData["status"]){
    //                 if (responseData["msg"] === "Data insertion success") {

    //                     that.$router.push({path:"/denglu"});
    //                 } else if (responseData["msg"] === "Account had been exist") {
	// 					window.alert('该账号已注册，请重新注册');
	// 					console.log(1)
    //                     var arrValue = document.getElementsByTagName('input');
    //                     for(var a of arrValue) {
    //                         a.value = '';
    //                     }
    //                 }
    //             }else if (!responseData["status"]) {
    //                 alert('注册失败，请重新注册');
    //             }
    //         },
    //         error: function () {
    //             console.log("注册失败！");
    //         }y

  },
  data () {
    return {
      msg:{},
      pipei:[],
      liansheng:[],

      sheng:[
          {
          name:'胜率排行榜',
          child:[{
                touxiang:'public/img/person_tou.jpg',
                name:'小新'
            },{
                touxiang:'public/img/person_tou.jpg',
                name:'小新'
            },{
                touxiang:'public/img/person_tou.jpg',
                name:'小新'
            },{
                touxiang:'public/img/person_tou.jpg',
                name:'小新'
            }]
      },{
          name:'连胜排行榜',
          child:[{
                touxiang:'public/img/person_tou.jpg',
                name:'小明',
            },{
                touxiang:'public/img/person_tou.jpg',
                name:'小明',
            },{
                touxiang:'public/img/person_tou.jpg',
                name:'小明',
            }]
      }
      ],
      
     
    }
  },
  methods:{
      emit(){
          var that=this;
		setTimeout(function(){
            emit.$emit("usermsg",that.msg)
        },3)
            // document.getElementsByClassName("mp3").play();
           
      },
      xuanxiangka(index){
          this.$(".bottom>ul").eq(index+1).show().siblings(".bottom>ul:not(.title)").hide();
          if(index+1==1){
                this.$(".title>li").eq(3).children().html("胜率")
          }else if(index+1==2){
              this.$(".title>li").eq(3).children().html("最大连胜次数");
          }
          
      },
      back(){
          var that=this;
          this.$.ajax({
              url:"http://129.28.101.21:5000/api/out",
              type:"GET",
              xhrFields:{
                  withCredentials:true
              },
              crossDomain:true,
              dataType:"json",
              success:function (res){
                  alert("已退出登录");
                  if(res["is_login"]===false){
                     that.$router.push({path:"/"});
                  }
              }
          })
      }
  }
}
</script>

<style lang="scss" scoped>
#app{
    width: 100%;
    height: 100%;
    .s-block{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
       
        .top-block{
            flex: 1;
            width: 100%;
       background-image: linear-gradient(-225deg, #5D9FFF 0%, #B8DCFF 48%, #6BBBFF 100%);
          // background-image: linear-gradient(120deg, #89f7fe 0%, #66a6ff 100%);
            display: flex;
            flex-direction: row;
            padding: 1rem 0;
            font-size: 26px;
            color: white;
            vertical-align: middle;
            .kong-block{
                flex: 1;
            }
             .s-title{
                flex: 1;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .s-touxiang{
                flex: 1;
                text-align: right;
                padding: 0 3rem 0 0;
                display: flex;
                align-items: center;
                justify-content: flex-end;
                
               .caidan{
                   width: 10rem;
                   position: relative;
                   padding: 0rem 1rem;
                   background: transparent;
                   text-align: center;
                   color:white;
                   font-size: 18px;
                   height: 4rem;
                   line-height: 4rem;
                                    //   border: 1px solid silver;
                //   box-sizing: border-box;
                .xiala{
                    position: absolute;
                    left: 0;
                    top: 4rem;
                    background: white;
                    //background-image: linear-gradient(-225deg, #5D9FFF 0%, #B8DCFF 48%, #6BBBFF 100%);
                    // border: 1px solid silver;
                    color: white;
                    width: 10rem;
                   // padding: 0 2rem 1rem 2rem;
                    display: none;
                    a{
                       
                        color: rgb(114, 108, 108)!important;
                        font-size: 14px;
                        span{
                            font-size: 14px;
                            color: rgb(114, 108, 108)!important;
                        }
                    }
                    span{
                        width: 100%;
                        display: block;
                        font-size: 14px;
                        // margin: 0 0 0.5rem 0;
                        color: rgb(114, 108, 108)!important;
                        cursor: pointer;
                       
                    }
                    span:hover{
                        background: rgb(43, 196, 235);
                        color: white!important;
                    }
                }
               }
               .caidan::after{
                   content: "";
                   position: absolute;
                   right: 10px;
                   top: 50%;
                   margin-top: -3px;
                    border: 6px solid;
                   border-color:white  transparent  transparent  transparent;
                  
               }
               .caidan:hover .xiala{
                   display: block;
               }
                img{
                    width: 6rem;
                    height: 6rem;
                    border-radius: 50%;
                    vertical-align: middle;
                    margin: 0 2rem;
                }
                span{
                    font-size: 18px;
                    color: white;
                }
                // .tuichu{
                //     display: flex;
                //     justify-content: flex-end;
                //     align-items: flex-end;
                //     color: white;
                // }
            }
        }
        .bottom-block{
            flex: 6;
            width: 100%;
            min-height: 38rem;
            display: flex;
            flex-direction: row;
            background-image: linear-gradient(120deg, #89f7fe 0%, #66a6ff 100%);
            .left-block{
                flex: 1;
                display: flex;
                align-items: center;
                justify-content: center;
                .pipei{
                    width: 15rem;
                    padding: 2rem 0;
                    border-radius: 20px;
                    background-image: linear-gradient(-225deg, #FFE29F 0%, #FFA99F 48%, #FF719A 100%);
                    border: none;
                    outline: none;
                    color: white;
                    font-size: 26px;
                    font-weight: bold;
                }
            }
            .right-block{
                flex: 1;
                display: flex;
                align-items: center;
                justify-content: center;
               .paihang-block{
             // background-image: linear-gradient(to top, #f3e7e9 0%, #e3eeff 99%, #e3eeff 100%);
             background: white;
                   width: 46rem;
                   min-height: 35rem;
                   border: 1px solid white;
                   display: flex;
                   flex-direction: column;
                   border-radius: 6px;
                   .top{
                       display: flex;
                       height: 3rem;
                       flex-direction: row;
                       align-items: center;
                       justify-items: center;
                       border-bottom:1px solid silver; 
                       padding: 3rem 0;
                       span{
                           flex: 1;
                           color: rgb(255, 195, 66);
                           font-size: 18px;
                            text-align: center;
                            cursor: pointer;
                       }
                   }
                   .bottom{
                       flex: 7;
                       overflow-y: scroll;
                       .title{
                           width: 100%;
                           overflow: hidden;
                           display: flex;
                           flex-direction: row;
                           padding-left: 2.8rem;
                           border-bottom: 1px solid silver;
                           li{
                               float: left;
                               list-style:none;
                               flex: 1;
                               color: orange;
                               display: flex;
                               justify-content: center;
                           }
                           li:nth-child(1){
                                display: flex;
                               justify-content: center;
                           }
                       }
                       ul{
                           
                           li{
                               position: relative;
                               list-style: none;
                               padding: .5rem .8rem;
                               box-sizing: border-box;
                               cursor: pointer;
                               display: flex;
                               flex-direction: row;
                               background: transparent;
                               border-radius: 6px;
                               margin: 1rem 0;  
                               .huangguan{
                                   position: absolute;
                                   left: 3px;
                                   top: 50%;
                                   margin-top: -1.5rem;
                                   width: 3rem;
                                   height: 3rem;
                                   vertical-align: middle;
                                   }
                                  
                               div{
                                   display: flex;
                                   width: 100%;
                                   height: 100%;
                                   flex-direction: row;
                                    padding-left: 2rem;
                                div{
                                    flex: 1;
                                    vertical-align: middle;
                                    img{
                                  
                                   vertical-align: middle;
                                   width: 5rem;
                                   height: 5rem;
                                   border-radius: 50%;

                               }
                                }
                               
                               span{
                                   flex: 1;
                                   font-size: 16px;
                                   color: orange;
                                   margin: 0 0 0 1rem;
                                   justify-content: center;
                                    display: flex;
                                    align-items: center;
                                    vertical-align: middle;
                                    overflow: hidden;
                                    text-overflow: ellipsis;
                                    white-space: nowrap;
                               }
                              
                               }
                               
                           }
                       }
                       .liansheng{
                           display: none;
                       }
                   }
               }
            }
        }
       
    }
}
</style>
