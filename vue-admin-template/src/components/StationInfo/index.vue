<template>
  <div>
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="名称">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="城市">
        <el-input type="text" v-model="form.city"></el-input>
      </el-form-item>
      <el-form-item label="薪资">
        <el-input type="text" v-model="form.salary"></el-input>
      </el-form-item>
      <el-form-item label="学历">
        <el-input type="text" v-model="form.education"></el-input>
      </el-form-item>
      <el-form-item label="年限要求">
        <el-input type="text" v-model="form.experience"></el-input>
      </el-form-item>
      <el-form-item label="公司名称">
        <el-input type="text" v-model="form.company"></el-input>
      </el-form-item>
      <el-form-item label="公司福利">
        <el-input type="textarea" v-model="form.fuli"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">立即创建</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'Index',
  data() {
    return {
      form: {
        name: '岗位名称',
        city: '成都',
        salary: '2000',
        education: '本科',
        experience: '2年',
        company: '新公司',
        fuli: 'w五险一金'
      }
    }
  },
  created() {
  },
  methods: {
    onSubmit() {
      console.log('submit!')
    }
  }
}
</script>

<style scoped>
</style>
