<template>
  <div class="table-form" style="padding: 33px;min-width: 220px;max-width: 500px;">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="名称">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="城市">
        <el-input v-model="form.city" type="text" />
      </el-form-item>
      <el-form-item label="薪资">
        <el-input v-model="form.salary" type="text" />
      </el-form-item>
      <el-form-item label="学历">
        <el-input v-model="form.education" type="text" />
      </el-form-item>
      <el-form-item label="年限要求">
        <el-input v-model="form.experience" type="text" />
      </el-form-item>
      <el-form-item label="公司名称">
        <el-input v-model="form.company" type="text" />
      </el-form-item>
      <el-form-item label="公司福利">
        <el-input v-model="form.fuli" type="textarea" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">立即创建</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { submit_postion } from '../../api/jian'

export default {
  name: 'Index',
  data() {
    return {
      form: {
        name: '',
        city: '',
        salary: '',
        education: '',
        experience: '',
        company: '',
        fuli: ''
      }
    }
  },
  created() {
  },
  methods: {
    onSubmit() {
      return new Promise((resolve, reject) => {
        submit_postion(this.form).then(data => {
          this.dataList = data.data
          this.form = {
            name: '',
            city: '',
            salary: '',
            education: '',
            experience: '',
            company: '',
            fuli: ''
          }
          this.$message({
            message: data.msg,
            type: 'success'
          })
        }).catch(error => {
          reject(error)
        })
      })
    }
  }
}
</script>

<style scoped>
</style>
