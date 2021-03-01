import Vue from 'vue'
import vueRouter from 'vue-router'
import login from '../components/page/login.vue'
import index from '../components/page/index.vue'
import geren from '../components/page/geren.vue'
import echar from '../components/page/echar.vue'
import xiugai from '../components/page/xiugai.vue'
import game from '../components/page/game.vue'
import denglu from '../components/page/denglu.vue'


let router=new vueRouter({
    mode:"hash",
    routes:[{
        path:'/',
        name:denglu,
        component:denglu,
    },{
        path:'/index',
        name:index,
        component:index
    },{
        path:'/geren',
        name:geren,
        component:geren
    },{
        path:'/echar',
        component:echar
    },{
        path:'/xiugai',
        name:xiugai,
        component:xiugai
    },{
        path:'/game',
        name:game,
        component:game
    },{
        path:"/login",
        name:login,
        component:login
    }]
})
Vue.use(vueRouter);
export default router;
