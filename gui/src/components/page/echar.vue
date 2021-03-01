<template>
    <div class="box">
        <div id="pieChart"></div>
    </div>
</template>
 
<script>
export default {
    mounted(){
        this.chartFn()
    },
    methods:{
        chartFn(){
            // 基于准备好的dom，初始化echarts实例
            var pieChart = this.$echarts.init(document.getElementById('pieChart'));
            pieChart.setOption({
                title:{
                    text:'饼图', //标题
                    subtext: '练习专用',  //副标题
                    x:'center'  // 位置
                },
                legend: {
                    orient: 'vertical', //图例列表的布局朝向。
                    left: 'left', //距离左侧的距离
                    data: ['直接访问','邮件营销','联盟广告','视频广告','搜索引擎']
                },
                series : [
                    {
                        name: '访问来源',
                        type: 'pie', //类型
                        radius : '60%', //饼图的半径
                        center: ['50%', '60%'], //饼图位置的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标。
                        data:[
                            {value:335, name:'直接访问'},
                            {value:310, name:'邮件营销'},
                            {value:234, name:'联盟广告'},
                            {value:135, name:'视频广告'},
                            {value:1548, name:'搜索引擎'}
                        ],
                    }
                ]
            })
            
        }
    }
}
</script>
 
<style scoped>
.box{
    margin-top:50px;
}
#pieChart{
    width:500px;
    height:500px;
}
</style>