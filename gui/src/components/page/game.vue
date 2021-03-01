<template>
 <div id='game'>
     
     <div class="gameover"><span>{{this.winner.nick_name+"     win"}}</span><span class="back-button" @click="emit()"><router-link to="/index">返回首页</router-link></span></div>
     <div class="g-title" @click="emit()"><div><router-link to="/index"><img src="static/img/fanhui.png" alt=""/><span>首页</span></router-link></div></div>
   <div class="g-block">
       <div class="left-game">
           <img :src='"http://"+this.user.avatarUrl' alt=""/>
           <span style="padding-left: 25px">{{this.user.nick_name}}</span>
           <span style="padding-left: 30px">{{score}}</span>
             <i-progress class="left-process"  :stroke-color="['#108ee9', '#87d068']" :percent="score" :stroke-width="20" text-inside />
       </div>
       <div class="middle-game">
           <div class="daojishi">
                <i-circle :percent="percent" :stroke-color="color">
                <Icon v-if="percent == 0" type="ios-checkmark" size="60" style="color:#5cb85c"></Icon>
                 <span v-else style="font-size:24px">{{ second}}s</span>
                </i-circle>
           </div>
    
   
    <!-- 题目标题 -->
     <div class="timu"><h3 style="text-align: center">{{question.title}}</h3>
    <!--<Tag class="danxuan">{{isSingleChoice}}</Tag>-->
     </div>
    <ButtonGroup class="xuanxiang-block" v-for="(item,index) in question.choice"  vertical :key="index">
    <i-button class="xuanxiang"  @click='show(item.choice_name)' long size='large'>{{item.choice_name+"    "+item.content}}</i-button>
    </ButtonGroup>
    
       </div>
       <div class="right-game">
          
           

           <div> <img :src='"http://"+this.pk_player.avatarUrl' alt=""/></div>
            <span style="padding-right:25px ">{{pk_player.nick_name}}</span>
            <span style="padding-right:30px ">{{pk_player.score}}</span>
           <i-progress class="right-process"  :stroke-color="['#108ee9', '#87d068']" :percent="this.pk_player.score" :stroke-width="20" text-inside />
       </div>
   </div>
   <!-- <loading v-if="this.pipei_success"></loading> -->
  </div>
</template>

<script>

import loading from './loading.vue'
import emit from '../../Emit/emit.js'
export default {
  name: 'game',
  components:{
      loading
  },
   
  mounted(){
            this.$("#game").height(window.innerHeight);
       // this.show()
            
            //console.log('开始倒计时');
            var that=this;
            emit.$on("usermsg",function(res){
                that.user=res;
                console.log(that.user,res);
                that.$nextTick(function(){
                    that.user=res;
                })
            })
            var namespace = '/compete';
            var socket = io.connect('http://129.28.101.21:5000'+ namespace);
            //console.log(location.protocol + '//' + document.domain + ':' + location.port +
            this.socketObj=socket;
            socket.on('connect',function (res) {        //监听初次连接回复
                if (res){
                    console.log(res)
                    that.connectStatus=res.connect
                    if (that.connectStatus===true){     //如果连接成功继续收听消息
                      console.log('连接服务器成功')
                      that.socketObj.emit('join',{'match':false,'connect':true,'ready':false,'msg':'客户端请求匹配'},function (res) {   //发起匹配请求
                          if(res){
                              console.log(res)
                          }
                      })

                    }

                }

            })
            that.socketObj.on('server_response',function (res) {    //监听后续回复
                if(res){

                        /*玩家信息返回*/
                      if(res['connect']===true&&res['match']===true&&res['ready']===false&&res['type']==='playerInfo'){
                        console.log('收到服务器返回的玩家信息')
                        console.log(res.data)
                          //绑定玩家信息
                          //
                          // that.playerA.id=res.data[0]['account']
                          // that.playerA.nick_name=res.data[0]['nick_name']
                          // that.playerA.avatarUrl=res.data[0]['avatar_url']
                          that.pk_player.id=res.data['account']
                          that.pk_player.nick_name=res.data['nick_name']
                          that.pk_player.avatarUrl=res.data['avatar_url']
                          //that.socketObj.emit()
                      }
                      if(res['connect']===true&&res['match']===true&&res['ready']===true&&res['type']==='question'){    //接收服务器题目信息
                          console.log('收到服务器返回的第'+(++that.questionIndex)+'题目')
                          that.is_answer=false;
                          that.question=res.data;
                          /*记录不同题型的个数*/
                          if(that.question['type']==='预警与监测'){
                              that.predictNum++;
                          }
                          if(that.question['type']==='构造与特点'){
                              that.structureNum++;
                          }
                          if(that.question['type']==='防震与救援'){
                              that.rescueNum++;
                          }



                          that.percent=100
                          if(that.timer===null){
                              that.timer = setInterval(that.updateSeconds, 1000);
                          }
                          console.log(res.data)
                      }
                      if(res['type']==='scoreInfo'){    //接收对方玩家分数信息
                          if(res.data['id']===that.pk_player['id']){
                            that.pk_player['currentQuestionScore']=res.data['current_score']
                            that.pk_player['score']=that.pk_player['score']+that.pk_player['currentQuestionScore']

                          }
                          else {
                            console.log('对方还未作答')
                          }

                      }
                      if (res['type']==='finalResult'){
                          clearInterval(that.timer)
                          if (res['winer']!=null){
                            //   that.$Modal.info({
                            //       title: '比赛结果',
                            //       content:'胜者为'+res['winer']['id']
                              //});
                              that.winner=res['winer'];

                              that.$(".gameover").css({
                                  display:"block"
                              })
                              // if(res['winer']!=that.pk_player['id']){
                              //     console.log('You win!')
                              // }
                              // else {
                                console.log(res['winer'])
                              //}

                            

                          }
                          else {
                            // that.$Modal.info({
                            //       title: '比赛结果',
                            //       content:'平局'
                            //   });
                             that.$(".gameover").css({
                                  display:"block"
                              })
                              that.$(".gameover").html("平局");
                            console.log('平局')

                          }
                      }


                    // this.timer = setTimeout(()=>{   //设置延迟执行
                    //     that.question=res.data
                    // },800);


                }

            })
            /*this.show()
            this.timer = setInterval(this.updateSeconds, 1000);
            console.log('开始倒计时')*/
  },
  data () {
    return {
      msg:'Welcome to Your Vue.js App',
       visible: false,
       user:{},
        question:{},
            winner:{},
            isSingleChoice:'单选',
            isShow:true,
            timer:null,
            percent:100,
            second:'10',
            score:0,
            is_answer:false,
            is_end:false,
            currentQuestionIndex:0,
            currentQuestionScore:0,
            pk_player:{
                'id':null,
                'nick_name':null,
                'avatarUrl':null,
                'score':0,
                'currentQuestionScore':0,
                'currentQuestionIndex':0
            },
            single:false,
            questionIndex:0,
            socketObj:null,
            tinum:0,
            pipei_success:true,
            correctNum:0,
            rescueNum:0,
            rescueRightNum:0,
            rescueRate:0,
            structureNum:0,
            structureRightNum:0,
            structureRate:0,
            predictNum:0,
            predictRightNum:0,
            predictRate:0,
            contest_info:{},

            all_time:0,
    }
  },
  methods:{
      emit(){
          var that=this;
        setTimeout(function(){
            emit.$emit("user",that.user);
        },2)
        that.$(".gameover").css({
            display:"none"
        })
      },
       show:function (choice_name) {
                var that=this
                console.log('开始执行show函数')
                //clearInterval(that.timer)
                //that.timer=null

                //console.log('choice为'+choice)
                if(choice_name!=0){   //用户作答时执行
                    console.log(choice_name)
                    this.is_answer=true
                    console.log('标准答案为'+this.question.result)
                    if(choice_name===this.question.result){     //进行打分

                        //统计不同题型正确个数
                        if (this.question.type==='预警与监测'){
                            this.predictRightNum++
                        }
                        if(this.question['type']==='构造与特点'){
                              this.structureRightNum++
                        }
                        if(this.question['type']==='防震与救援'){
                            this.rescueRightNum++
                        }

                        //console.log('当前剩余秒数为'+this.second)
                        this.currentQuestionScore=this.second
                        this.score=this.score+this.currentQuestionScore
                        this.$Modal.success({
                            title: '恭喜你,选对了',
                            content: '不错哟^.^'
                        });
                    }
                    else {
                        this.$Modal.error({
                            title: '有点遗憾，选错了',
                            content: '正确答案:  '+that.question.result
                        });
                    }
                }
                if(choice_name===0){  //用户未作答时执行
                    this.is_answer=false
                    console.log('该题未作答')
                    this.currentQuestionScore=0
                }
                //当前题目序号加1
                this.currentQuestionIndex++
                if(this.currentQuestionIndex===10){     //判断游戏是否结束

                    this.is_end=true
                    //计算不同题型正确率
                    if(this.predictNum!=0){
                        this.predictRate=this.predictRightNum/this.predictNum

                    }
                    if(this.structureNum!=0){
                        this.structureRate=this.structureRightNum/this.structureNum
                    }
                    if(this.rescueNum!=0){
                        this.rescueRate=this.rescueRightNum/this.rescueNum
                    }
                    this.contest_info={
                      'predictRate':this.predictRate,
                      'rescueRate':this.rescueRate,
                      'structureRate':this.structureRate,
                      'correct_num':this.correctNum
                    }

                }


                this.socketObj.emit('scoreInfo',{'is_answer':this.is_answer,'is_end':this.is_end,'currentQuestionIndex':this.currentQuestionIndex,'current_score':this.currentQuestionScore,'contest_info':this.contest_info,'msg':'提交成绩'},function (res) {      //上传自己实时分数
                    if(res){
                        console.log(res)
                    }

                })
        },
    updateSeconds:function(){

            //倒计时为0,代表未作答，进行更换下一道题
            if(this.percent===0){
                console.log('倒计时为0')

                this.show(0)
                return false
            }
            this.percent-=10;
            this.second=this.percent/10
        },
        reLoad:function () {
            this.isShow=false
        },
               //获取题目信息
          getQuestionInfo:function(){
              if(this.questionIndex<10){
                  this.socketObj.emit('')
              }

          },
          //提交答题结果
          commitAnswerResult:function(){
              this.socketObj.emit('')

          },
        },
     computed: {
            color () {
                let color = '#2db7f5';
                if (this.percent == 0) {
                    color = '#5cb85c';
                }
                return color;
            }
        }
        

       
        
  
}
</script>

<style lang="scss" scoped>
.timu{
    position: relative;
    width: 100%;
    min-height: 10rem;
    margin-top: 2rem;
    .danxuan{
        position: absolute;
        right: 0;
        bottom: 10px;
    }
}
.danxuan{
    float: right;
}
.ivu-btn>span{
    white-space: pre-wrap;
}
.xuanxiang-block{
    //display: flex;
    width: 100%;
    text-align: center;
    //justify-self: center;
    padding: 1rem 1rem;
}
.xuanxiang{
    position: relative;
    display: inline-block;
    width: 70rem;
    padding: 1rem 2rem;
    min-height: 4rem;
    white-space: pre-wrap;
   // overflow: hidden;
//   span{
//      // position: absolute;
//      white-space: nowrap;
//       word-wrap: break-word;
//       text-overflow: ellipsis;
//       float: left;
//   }
    
}
#game{
    position: relative;
    width: 100%;
    height: 100%;
    //background: rgb(139, 228, 240);
     background-image: linear-gradient(-225deg, #5D9FFF 0%, #B8DCFF 48%, #6BBBFF 100%);
  .gameover{
        position: absolute;
        left: 50%;
        top: 50%;
        margin-left: -25rem;
        margin-top: -15rem;
        z-index: 10;
        width: 50rem;
        height: 30rem;
        background: url('../../assets/yanhua2.gif') no-repeat white;
        background-size: 100% 100%;
        border: 2px solid white;
        line-height: 30rem;
        text-align: center;
        border-radius: 15px;
        display: none;
        span:nth-child(1){
            display: block;
            height: 30%;
            font-size: 46px;
            font-weight: bold;
            color: orange;
        }
        span:nth-child(2){
            display: inline!important;
            font-size: 15px;
            color: gray;
            float: right;
            cursor: pointer;
        }
    }
    .g-title{
        position: fixed;
        left: 0;
        top: 0;
        width: 100%;
        height: 6rem;
        background: rgba(255, 255, 255, 0.418);
        padding: 0 2rem;
        line-height: 6rem;
       div{
           display: inline-block;
            img{
            width: 2.5rem;
            height: 2.5rem;
            vertical-align: middle
        }
        span{
            color: white;
            font-size: 18px;
            vertical-align: middle;
        }
       }
    }
    .g-block{
        padding: 8rem 0 0 0;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: row;
        
        .left-game{
            //position: relative;
            flex: 1;
            display: flex;
            flex-direction: column;
            padding: 1rem 10rem;
            //justify-content: center;
            img{
                width: 8rem;
                height: 8rem;
                border-radius: 50%;
            }
            span{
                color: white;
                font-size: 20px;
                font-weight: bold;
                vertical-align: middle;
                margin: 1rem 0 0 0;
                padding: 0 0 0 1rem;
            }
            span:last-child{
                display: block;
                padding: 1rem 3rem;
            }
            .left-process{
                position: absolute;
                left:-76px;
                bottom: 258px;
                 transform: rotate(-90deg);
                 width: 40rem;
                 height: 3rem;
                 
            }
        }
        .middle-game{
            flex: 3;
            .daojishi{
                width: 100%;
                display: flex;
                justify-content: center;
                margin: 1rem 0 0 0;
            }
            
        }
        .right-game{
            flex: 1;
            display: flex;
            flex-direction: column;
            align-content: flex-end;
            padding: 1rem 10rem;
            div{
                text-align: right;
                 img{
                width: 8rem;
                height: 8rem;
                border-radius: 50%;
               
               
            }
            }
           
            span{
                color: white;
                font-size: 20px;
                font-weight: bold;
                margin: 1rem 0 0 0;
                padding: 0 1rem 0 0;
               text-align: right;
            }
            span:last-child{
                display: block;
                padding: 1rem 3rem;
            }
            .right-process{
                position: absolute;
                right: -76px;
                bottom: 259px;
                 transform: rotate(-90deg);
                 width: 40rem;
                 height: 3rem;
            }
        }
    }
}
</style>
