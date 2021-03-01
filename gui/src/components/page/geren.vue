<template>
 <div id='geren'>
    <div class="gtitle-block">
        <div class="top-left" @click="emit()"><router-link to="/index"><img src='static/img/fanhui.png' alt=""/><span>首页</span></router-link></div>
        <span>个人信息</span>
    </div>
    <div class="usermsg">
        <div><img :src='"http://"+this.user.avatarUrl' alt=""/></div>
        
        <ul>
            <li><span>账号：</span><span>{{this.msg.account}}</span></li>
            <li><span>昵称：</span><span>{{this.msg.nick_name}}</span></li>
            <li><span>电话：</span><span>{{this.msg.tel}}</span></li>
            <li><router-link to="/xiugai"><button @click="emit()">修改信息</button></router-link></li>
        </ul>
       
    </div>
     <p class="bottom-title">比赛信息展示</p>
    <div class="tu-block">
       
        <div id="main1"></div>
        <!-- <div id="main2"></div> -->
        <!-- <div id="main3"></div> -->
    </div>
    <div class="biaoge">
        <table border="2">
            <tr>
                <th>用户等级</th>
                <th>用户积分</th>
                <th>胜率</th>
                <th>胜利次数</th>
                <th>最大连胜次数</th>
                <th>比赛次数</th>
                <th>平均成绩</th>
                <th>平均用时</th>
                <th>平均总正确率</th>
                
            </tr>
            <tr>
               <td>{{this.msg.level_grade}}</td>
                <td>{{this.msg.integral_score}}</td>
                <td>{{this.msg.win_rate}}</td>
                <td>{{this.msg.win_num}}</td>
                <td>{{this.msg.max_streak_num}}</td>
                <td>{{this.msg.contest_num}}</td>
                <td>{{this.msg.average_score}}</td>
                <td>{{this.msg.average_time}}</td>
                <td>{{this.msg.correct_rate}}</td>
            </tr>
        </table>
    </div>
  </div>
</template>

<script>
import emit from '../../Emit/emit.js'
export default {
  name: 'geren',
  mounted(){    
      var that=this;
       emit.$on("usermsg",(res)=>{
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
          async:false,
          crossDomain:true,
            // data: null,
            datatype:"json",
            contentType: 'application/json;charset=UTF-8 ',
            success:function(result){
                console.log(result.data)
                that.msg=result.data;
                console.log(this.msg);
               
            }
      })
      that.draw();

  },
  data () {
    return {
      msg:{},
      user:{}
    }
  },
    methods:{
        emit(){
            var that=this;
            setTimeout(function(){
                emit.$emit("user",that.user)
            },2)
        },
        draw(){
            var that=this;
           // console.log(that.msg)
              var myChart1= this.$echarts.init(document.getElementById('main1'));
var pathSymbols = {
    // reindeer: 'path://M-22.788,24.521c2.08-0.986,3.611-3.905,4.984-5.892 c-2.686,2.782-5.047,5.884-9.102,7.312c-0.992,0.005-0.25-2.016,0.34-2.362l1.852-0.41c0.564-0.218,0.785-0.842,0.902-1.347 c2.133-0.727,4.91-4.129,6.031-6.194c1.748-0.7,4.443-0.679,5.734-2.293c1.176-1.468,0.393-3.992,1.215-6.557 c0.24-0.754,0.574-1.581,1.008-2.293c-0.611,0.011-1.348-0.061-1.959-0.608c-1.391-1.245-0.785-2.086-1.297-3.313 c1.684,0.744,2.5,2.584,4.426,2.586C-8.46,3.012-8.255,2.901-8.04,2.824c6.031-1.952,15.182-0.165,19.498-3.937 c1.15-3.933-1.24-9.846-1.229-9.938c0.008-0.062-1.314-0.004-1.803-0.258c-1.119-0.771-6.531-3.75-0.17-3.33 c0.314-0.045,0.943,0.259,1.439,0.435c-0.289-1.694-0.92-0.144-3.311-1.946c0,0-1.1-0.855-1.764-1.98 c-0.836-1.09-2.01-2.825-2.992-4.031c-1.523-2.476,1.367,0.709,1.816,1.108c1.768,1.704,1.844,3.281,3.232,3.983 c0.195,0.203,1.453,0.164,0.926-0.468c-0.525-0.632-1.367-1.278-1.775-2.341c-0.293-0.703-1.311-2.326-1.566-2.711 c-0.256-0.384-0.959-1.718-1.67-2.351c-1.047-1.187-0.268-0.902,0.521-0.07c0.789,0.834,1.537,1.821,1.672,2.023 c0.135,0.203,1.584,2.521,1.725,2.387c0.102-0.259-0.035-0.428-0.158-0.852c-0.125-0.423-0.912-2.032-0.961-2.083 c-0.357-0.852-0.566-1.908-0.598-3.333c0.4-2.375,0.648-2.486,0.549-0.705c0.014,1.143,0.031,2.215,0.602,3.247 c0.807,1.496,1.764,4.064,1.836,4.474c0.561,3.176,2.904,1.749,2.281-0.126c-0.068-0.446-0.109-2.014-0.287-2.862 c-0.18-0.849-0.219-1.688-0.113-3.056c0.066-1.389,0.232-2.055,0.277-2.299c0.285-1.023,0.4-1.088,0.408,0.135 c-0.059,0.399-0.131,1.687-0.125,2.655c0.064,0.642-0.043,1.768,0.172,2.486c0.654,1.928-0.027,3.496,1,3.514 c1.805-0.424,2.428-1.218,2.428-2.346c-0.086-0.704-0.121-0.843-0.031-1.193c0.221-0.568,0.359-0.67,0.312-0.076 c-0.055,0.287,0.031,0.533,0.082,0.794c0.264,1.197,0.912,0.114,1.283-0.782c0.15-0.238,0.539-2.154,0.545-2.522 c-0.023-0.617,0.285-0.645,0.309,0.01c0.064,0.422-0.248,2.646-0.205,2.334c-0.338,1.24-1.105,3.402-3.379,4.712 c-0.389,0.12-1.186,1.286-3.328,2.178c0,0,1.729,0.321,3.156,0.246c1.102-0.19,3.707-0.027,4.654,0.269 c1.752,0.494,1.531-0.053,4.084,0.164c2.26-0.4,2.154,2.391-1.496,3.68c-2.549,1.405-3.107,1.475-2.293,2.984 c3.484,7.906,2.865,13.183,2.193,16.466c2.41,0.271,5.732-0.62,7.301,0.725c0.506,0.333,0.648,1.866-0.457,2.86 c-4.105,2.745-9.283,7.022-13.904,7.662c-0.977-0.194,0.156-2.025,0.803-2.247l1.898-0.03c0.596-0.101,0.936-0.669,1.152-1.139 c3.16-0.404,5.045-3.775,8.246-4.818c-4.035-0.718-9.588,3.981-12.162,1.051c-5.043,1.423-11.449,1.84-15.895,1.111 c-3.105,2.687-7.934,4.021-12.115,5.866c-3.271,3.511-5.188,8.086-9.967,10.414c-0.986,0.119-0.48-1.974,0.066-2.385l1.795-0.618 C-22.995,25.682-22.849,25.035-22.788,24.521z',
    // plane: 'path://M1.112,32.559l2.998,1.205l-2.882,2.268l-2.215-0.012L1.112,32.559z M37.803,23.96 c0.158-0.838,0.5-1.509,0.961-1.904c-0.096-0.037-0.205-0.071-0.344-0.071c-0.777-0.005-2.068-0.009-3.047-0.009 c-0.633,0-1.217,0.066-1.754,0.18l2.199,1.804H37.803z M39.738,23.036c-0.111,0-0.377,0.325-0.537,0.924h1.076 C40.115,23.361,39.854,23.036,39.738,23.036z M39.934,39.867c-0.166,0-0.674,0.705-0.674,1.986s0.506,1.986,0.674,1.986 s0.672-0.705,0.672-1.986S40.102,39.867,39.934,39.867z M38.963,38.889c-0.098-0.038-0.209-0.07-0.348-0.073 c-0.082,0-0.174,0-0.268-0.001l-7.127,4.671c0.879,0.821,2.42,1.417,4.348,1.417c0.979,0,2.27-0.006,3.047-0.01 c0.139,0,0.25-0.034,0.348-0.072c-0.646-0.555-1.07-1.643-1.07-2.967C37.891,40.529,38.316,39.441,38.963,38.889z M32.713,23.96 l-12.37-10.116l-4.693-0.004c0,0,4,8.222,4.827,10.121H32.713z M59.311,32.374c-0.248,2.104-5.305,3.172-8.018,3.172H39.629 l-25.325,16.61L9.607,52.16c0,0,6.687-8.479,7.95-10.207c1.17-1.6,3.019-3.699,3.027-6.407h-2.138 c-5.839,0-13.816-3.789-18.472-5.583c-2.818-1.085-2.396-4.04-0.031-4.04h0.039l-3.299-11.371h3.617c0,0,4.352,5.696,5.846,7.5 c2,2.416,4.503,3.678,8.228,3.87h30.727c2.17,0,4.311,0.417,6.252,1.046c3.49,1.175,5.863,2.7,7.199,4.027 C59.145,31.584,59.352,32.025,59.311,32.374z M22.069,30.408c0-0.815-0.661-1.475-1.469-1.475c-0.812,0-1.471,0.66-1.471,1.475 s0.658,1.475,1.471,1.475C21.408,31.883,22.069,31.224,22.069,30.408z M27.06,30.408c0-0.815-0.656-1.478-1.466-1.478 c-0.812,0-1.471,0.662-1.471,1.478s0.658,1.477,1.471,1.477C26.404,31.885,27.06,31.224,27.06,30.408z M32.055,30.408 c0-0.815-0.66-1.475-1.469-1.475c-0.808,0-1.466,0.66-1.466,1.475s0.658,1.475,1.466,1.475 C31.398,31.883,32.055,31.224,32.055,30.408z M37.049,30.408c0-0.815-0.658-1.478-1.467-1.478c-0.812,0-1.469,0.662-1.469,1.478 s0.656,1.477,1.469,1.477C36.389,31.885,37.049,31.224,37.049,30.408z M42.039,30.408c0-0.815-0.656-1.478-1.465-1.478 c-0.811,0-1.469,0.662-1.469,1.478s0.658,1.477,1.469,1.477C41.383,31.885,42.039,31.224,42.039,30.408z M55.479,30.565 c-0.701-0.436-1.568-0.896-2.627-1.347c-0.613,0.289-1.551,0.476-2.73,0.476c-1.527,0-1.639,2.263,0.164,2.316 C52.389,32.074,54.627,31.373,55.479,30.565z',
    // rocket: 'path://M-244.396,44.399c0,0,0.47-2.931-2.427-6.512c2.819-8.221,3.21-15.709,3.21-15.709s5.795,1.383,5.795,7.325C-237.818,39.679-244.396,44.399-244.396,44.399z M-260.371,40.827c0,0-3.881-12.946-3.881-18.319c0-2.416,0.262-4.566,0.669-6.517h17.684c0.411,1.952,0.675,4.104,0.675,6.519c0,5.291-3.87,18.317-3.87,18.317H-260.371z M-254.745,18.951c-1.99,0-3.603,1.676-3.603,3.744c0,2.068,1.612,3.744,3.603,3.744c1.988,0,3.602-1.676,3.602-3.744S-252.757,18.951-254.745,18.951z M-255.521,2.228v-5.098h1.402v4.969c1.603,1.213,5.941,5.069,7.901,12.5h-17.05C-261.373,7.373-257.245,3.558-255.521,2.228zM-265.07,44.399c0,0-6.577-4.721-6.577-14.896c0-5.942,5.794-7.325,5.794-7.325s0.393,7.488,3.211,15.708C-265.539,41.469-265.07,44.399-265.07,44.399z M-252.36,45.15l-1.176-1.22L-254.789,48l-1.487-4.069l-1.019,2.116l-1.488-3.826h8.067L-252.36,45.15z',
   reindeer:'path://public/img/icon/jiuyuan.png',
   plane:'path://public/img/icon/dizhen.png',
   rocket:'path://public/img/icon/yujing.png',
};

myChart1.setOption({
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'none'
        },
        formatter: function (params) {
            return params[0].name + ': ' + params[0].value;
        }
    },
    xAxis: {
        data: ['救援知识答题正确率', '构造知识答题正确率', '预测预警知识答题正确率'],
        axisTick: {show: false},
        axisLine: {show: false},
        axisLabel: {
            textStyle: {
                color: '#2580B3'
            }
        }
    },
    yAxis: {
        splitLine: {show: false},
        axisTick: {show: false},
        axisLine: {show: false},
        axisLabel: {show: false}
    },
    color: ['#7DE2FC'],
    series: [{
        name: 'hill',
        type: 'pictorialBar',
        barCategoryGap: '-130%',
        // symbol: 'path://M0,10 L10,10 L5,0 L0,10 z',
        symbol: 'path://M0,10 L10,10 C5.5,10 5.5,5 5,0 C4.5,5 4.5,10 0,10 z',
        itemStyle: {
            normal: {
                opacity: 0.5
            },
            emphasis: {
                opacity: 1
            }
        },
        data: [parseFloat(that.msg.rescue_rate), parseFloat(that.msg.structure_rate), parseFloat(that.msg.predict_rate)],
        z: 10
    }, {
        name: 'glyph',
        type: 'pictorialBar',
        barGap: '-100%',
        symbolPosition: 'end',
        symbolSize: 50,
        symbolOffset: [0, '-120%'],
        data: [{
            value: parseFloat(that.msg.rescue_rate),
            symbol: pathSymbols.reindeer,
            symbolSize: [60, 60]
        }, {
            value: parseFloat(that.msg.structure_rate),
            symbol: pathSymbols.rocket,
            symbolSize: [50, 60]
        }, {
            value: parseFloat(that.msg.predict_rate),
            symbol: pathSymbols.plane,
            symbolSize: [65, 35]
        }]
    }]
});
          
//    myChart1.setOption({
//     title: {
//         // text: '基础雷达图'
//     },
//     tooltip: {},
//     legend: {
//         // data: ['预算分配（Allocated Budget）', '实际开销（Actual Spending）']
//     },
//     radar: {
//         // shape: 'circle',
//         name: {
//             textStyle: {
//                 color: '#fff',
//                 backgroundColor: '#999',
//                 borderRadius: 3,
//                 padding: [3, 5]
//             }
//         },
//         indicator: [
//             { name: '销售（sales）', max: 6500},
//             { name: '管理（Administration）', max: 16000},
//             { name: '信息技术（Information Techology）', max: 30000},
//             { name: '客服（Customer Support）', max: 38000},
//             { name: '研发（Development）', max: 52000},
//             { name: '市场（Marketing）', max: 25000}
//         ]
//     },
//     series: [{
//         name: '预算 vs 开销（Budget vs spending）',
//         type: 'radar',
//         // areaStyle: {normal: {}},
//         data : [
//             {
//                 value : [4300, 10000, 28000, 35000, 50000, 19000],
//                 name : '预算分配（Allocated Budget）'
//             },
//             {
//                 value : [5000, 14000, 28000, 31000, 42000, 21000],
//                 name : '实际开销（Actual Spending）'
//             }
//         ]
//     }]
// });

// var myChart2 = this.$echarts.init(document.getElementById('main2'));
// myChart2.setOption({
//     title : {
//         // text: '某站点用户访问来源',
//         // subtext: '纯属虚构',
//         x:'center'
//     },
//     tooltip : {
//         trigger: 'item',
//         formatter: "{a} <br/>{b} : {c} ({d}%)"
//     },
//     legend: {
//         orient: 'vertical',
//         left: 'left',
//         data: ['直接访问','邮件营销','联盟广告','视频广告','搜索引擎']
//     },
//     series : [
//         {
//             name: '访问来源',
//             type: 'pie',
//             radius : '55%',
//             center: ['50%', '60%'],
//             data:[
//                 {value:335, name:'直接访问'},
//                 {value:310, name:'邮件营销'},
//                 {value:234, name:'联盟广告'},
//                 {value:135, name:'视频广告'},
//                 {value:1548, name:'搜索引擎'}
//             ],
//             itemStyle: {
//                 emphasis: {
//                     shadowBlur: 10,
//                     shadowOffsetX: 0,
//                     shadowColor: 'rgba(0, 0, 0, 0.5)'
//                 }
//             }
//         }
//     ]
// });
//鼠标事件
            // myChart2.on('click',function(params){
            //     console.log(params)
            // })
// var myChart3 = this.$echarts.init(document.getElementById('main3'));
// option3 = {
//     xAxis: {
//         type: 'category',
//         data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
//     },
//     yAxis: {
//         type: 'value'
//     },
//     series: [{
//         data: [120, 200, 150, 80, 70, 110, 130],
//         type: 'bar'
//     }]
// };
// myChart3.setOption(option3);


        }
    }
}
</script>

<style lang="scss" scoped>
#geren{
    width: 100%;
    height: 100%;
    overflow-x: hidden;
    padding: 0 0 6rem 0;
    .gtitle-block{
        position: relative;
        width: 100%;
        text-align: center;
       padding: 3rem 0;
     background-image: linear-gradient(-225deg, #7DE2FC 0%, #B9B6E5 100%);
        color: white!important;
        font-size: 26px;
        .top-left{
           position: absolute;
           left:0;
           top:50%;
           height: 4rem;
           margin-top: -2rem;
            padding: 0 3rem;
            line-height: 4rem;
           img{
                width: 2rem;
                height: 2rem;
                vertical-align: middle;
           }
           span{
               font-size: 16px;
               vertical-align: middle;
               color: white;
           }
        }
    }
    .usermsg{
        width: 100%;
        height: 100%;
        div:nth-child(1){
            width: 100%;
            min-height: 3rem;
            padding: 1rem;
            text-align: center;
            img{
                width: 14rem;
                height: 14rem;
                border-radius: 50%;
            }
        }
       
            ul{
                width: 100%;
                text-align: center;
                padding: 0 0 2rem 0;
                li{
                    list-style: none;
                    padding: 0.5rem 10rem;
                    display: flex;
                    flex-direction: row;
                    font-size: 22px;
                    span:nth-child(1){
                        flex: 1.1;
                        display: inline-block;
                        width: 8rem;
                        text-align: right;
                        padding: 0 1rem 0 0;
                    }
                    span:nth-child(2){
                        flex: 1;
                       
                       text-align: left;
                        
                    }
                }
                li:nth-child(4){
                    display: flex;
                    justify-content: center;
                    button{
                       background: #ff9a9e;
                       padding: 1rem 2rem;
                       border-radius: 10px;
                       font-size: 16px;
                       color: white;
                       outline: none;
                       border: none;
                       outline: none;
                    }
                }
            }
        
    }
    .bottom-title{
            font-size: 20px;
            color: black;
            font-weight: bold;
            text-align: center;
        }
    .tu-block{
        width: 100%;
        min-height: 40rem;
        display: flex;
        flex-direction: row;
        
        #main1{
            flex: 1;
            padding: 2rem;
            display:flex;
            justify-content: center;
        }
        #main2{
            flex: 1;
            padding: 2rem;
        }
        #main3{
            flex: 1
        }
    }
    .biaoge{
        width: 100%;
        min-height: 10rem;
        padding: 0rem 3rem;
        text-align: center;
        display: flex;
        justify-content: center;
        table{
            width: 80%;
            height: 100%;
            text-align: center;
            border-collapse:collapse;
            border: 2px solid black;
            th{
                height: 80px;
               text-align: center;
               border: 2px solid black;
               background: #7DE2FC;
               
            }
            
            td
            {
                height:50px;
                vertical-align:bottom;
                padding:15px;
                border: 2px solid black;
            }
        }
    }
}
</style>
