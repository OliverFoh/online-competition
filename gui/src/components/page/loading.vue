<template>
 <div id='loading'>
   <div class="demo-spin-article">
        <!-- <h3>登金陵凤凰台</h3>
        <address>李白</address>
        <article>
            <p>凤凰台上凤凰游，凤去台空江自流。</p>
            <p>吴宫花草埋幽径，晋代衣冠成古丘。</p>
            <p>三山半落青天外，二水中分白鹭洲。</p>
            <p>总为浮云能蔽日，长安不见使人愁。</p>
        </article>-->
        <Spin size="large" fix v-if="spinShow"></Spin> 
    </div>
    <br>
    切换显示状态：<i-switch @on-change="spinShow = !spinShow"></i-switch>
  </div>
</template>

<script>
export default {
  name: 'loading',
  mounted(){
      this.$("#loading").height(window.innerHeight);
  },
  data () {
    return {
      msg:'Welcome to Your Vue.js App',
       spinShow: true
    }
  }
}
</script>

<style scoped>
@import "../../css/login.css";
@import "../../css/util.css";
#loading{
    position: fixed;
    left: 0;
    top: 0;
    z-index: 100;
    width: 100%;
    height: 100%;
    }
</style>
