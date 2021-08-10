<template>
  <div class="table-form" style="display: flex;align-items: center;justify-content: center;padding: 33px;">
    <el-form style="width: 450px;" ref="form" :model="form" label-width="80px">
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
<!--        <el-input v-model="form.education" type="text" />-->
        <el-select v-model="form.education" style="position: relative;font-size: 14px;display: inline-block;width: 100%;" placeholder="请选择">
          <el-option
            v-for="item in options_education"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="年限要求">
        <el-input v-model="form.experience" type="text" />
      </el-form-item>
      <el-form-item label="公司名称">
        <el-input v-model="form.company" type="text" />
      </el-form-item>
      <el-form-item label="岗位描述">
        <el-input v-model="form.fuli" type="textarea" />
      </el-form-item>
      <el-form-item style="justify-content: space-between;display: flex;">
        <el-button type="primary" @click="onSubmit">创建</el-button>
<!--        <el-button>取消</el-button>-->
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
      options_education: [{
        value: '专科',
        label: '专科'
      }, {
        value: '本科',
        label: '本科'
      }, {
        value: '硕士',
        label: '硕士'
      }, {
        value: '博士',
        label: '博士'
      }],
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
          this.$message.success(data.msg)
        }).catch(error => {
          reject(error)
        })
      })
    }
  }
}
</script>

<style scoped>
.el-form-item {
  padding: 12px;
}
</style>
