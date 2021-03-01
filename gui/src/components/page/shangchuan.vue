<template>
  <div class="app-container">

    <el-form id="box2" :label-position="labelPosition" v-model="dape" style="display:none; margin-left:10%;">
      
      <el-form-item label="上传音文件">
        <el-input type="file" :value="dape.video" v-model="dape.video" name="video" accept="audio/mpeg" style="width: 20%"></el-input>
      </el-form-item>

      <el-form-item label="更改封面">
        <el-input type="file" :value="dape.file" v-model="dape.file" name="file" accept="image/*" style="width: 20%"></el-input>
      </el-form-item>

      <el-button type="primary" style="width:10%;margin-bottom:30px;" @click.native.prevent="addlist(dape)">提交</el-button>
    </el-form>
  </div>
</template>

<script>
import { stup } from '@/api/manuscript'

export default {
  data() {
    return {
      dape: {
        file: '',
        video: ''
      }
    }
  },
  methods: {
    addlist(cont){

      let fileObj = document.getElementsByName('video')[0].files[0]
      let fileObj2 = document.getElementsByName('file')[0].files[0]

      if (window.confirm('你确定要修改吗')) {
        let formData = new FormData();
        formData.append('file', fileObj2);
        formData.append('video', fileObj);
        stup(formData).then(reponse => {
          const { code, msg } = reponse
          if (code !== 0) {
            Message({
              message: msg,
              type: 'success',
              duration: 5 * 1000
            })
            return
          }
          location.reload()
          Message({
            message: '更改成功',
            type: 'success',
            duration: 5 * 1000
          })
          this.sleep(5000)
          removeToken()
          resetRouter()
          location.reload()
        })
      }
    }
  }
}
</script>


