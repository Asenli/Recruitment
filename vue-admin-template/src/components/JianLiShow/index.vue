<template>
  <div class="jianli" style="height: auto;display: flex;flex-direction: column;margin: 20px 100px 100px 100px;">
    <div style="height: 35px;">
      <div style="">
        <span>期望职位：</span>
        <el-input v-model="expect" :disabled="true" style="width: 220px;" />
        <span style="margin-left: 20px;">求职状态：</span>
        <el-input v-model="statu" :disabled="true" style="width: 220px;" />
      </div>
    </div>
    <div style="margin-top: 35px;height: 10%;border: 1px solid #b6afaf;padding: 10px;border-radius: 10px;box-shadow: 0 0 0 10px #eeeef0;">
      <div class="basic-info">
        <p class="basic-name female" style="margin-top: 5px;">
          <span style="font-size: 25px;color: #333;font-weight: 600;">{{ form.name }}</span>
        </p>
        <p style="margin-top: 5px;">
          <span class="basic-company">{{ form.company }}</span>
        </p>
        <p class="basic-self" style="margin-top: 5px;">
          <span class="basic-exp">{{ form.workYear }} 年工作经验</span>
          <span class="basic-edu"> / {{ form.education === '本科' ? '本科 ' + '. 统招' : '专科' }}  </span>
          <span class="basic-age"> / {{ form.major }}</span>
          <span class="basic-age"> / {{ form.age }}岁</span>
          <span class="basic-age"> / {{ form.sex }}</span>
        </p>
        <p>
          <span class="basic-tel">
            <i class="el-icon-mobile" /><span>{{ form.mobile }}</span>
          </span>
          <span class="basic-email">
            <i class="el-icon-message" /><span>{{ form.email }}</span>
          </span>
        </p>
        <p><span>
          {{ form.address }}
        </span></p>
      </div>
    </div>
    <div style="margin-top: 30px;height: 30%;border: 1px solid #b6afaf;padding: 10px;border-radius: 10px;box-shadow: 0 0 0 10px #eeeef0;">
      <p class="mynice">
        <span style="font-size: 26px;color: #333;font-weight: 600;"> 个人优势</span>
      </p>
      <div class="ql-editor" v-html="myCotent" />
    </div>
    <div style="margin-top: 30px;border: 1px solid #b6afaf;padding: 10px;border-radius: 10px;box-shadow: 0 0 0 10px #eeeef0;">
      <div class="mynice">
        <span style="font-size: 26px;color: #333;font-weight: 600;"> 工作经历</span>
        <div v-for="(sureWork, i, index) in sureWorks" :key="index" class="work-class">
          <div v-if="sureWork" class="work-name">
            <span>{{ sureWork.name }}</span>
            <span>{{ sureWork.dept }}</span>
            <span>{{ sureWork.vocation }}</span>
            <span v-if="sureWork.date1" style="margin-left: 10%;">{{ sureWork.date1[0] }}-{{ sureWork.date1[1] }}</span>
          </div>
          <div class="ql-editor" style="margin: 2%;" v-html="sureWork.content" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Index',
  props: {
    jianda: {
      type: Object,
      default: function() {}
    }
  },
  data() {
    return {
      editorOption: {
        theme: 'snow',
        modules: {
          toolbar: [
            [{ 'list': 'bullet' }, { 'list': 'ordered' }],
            ['bold']
          ]
        }
      }
    }
  },
  computed: {
    sureWorks() {
      return this.jianda.sureWorks
    },
    statu() {
      return this.jianda.statu
    },
    expect() {
      return this.jianda.expect
    },
    myCotent() {
      return this.jianda.myCotent[0]
    },
    form() {
      return {
        education: this.jianda.education,
        name: this.jianda.name,
        // 出生
        date0: '',
        // 工作时间
        date1: '',
        // 专业
        major: this.jianda.major,
        workYear: this.jianda.workYear,
        mobile: this.jianda.mobile,
        city: this.jianda.city,
        // 性别
        sex: this.jianda.sex,
        email: this.jianda.email,
        // 住址
        address: this.jianda.address,
        age: this.jianda.age
      }
    }
  },
  mounted() {
    console.log(this.jianda)
    console.log(this.jianda.major)
  },
  methods: {
  }
}
</script>

<style scoped>
.work-class {
  font-size: 14px;
  min-height: 20px;
  margin-top: 1%;
  border: 2px solid #c7c7c7;
  padding: 10px;
  border-radius: 10px;
}

.el-icon-edit {
  cursor: pointer;
  color: #409EFF;
  float: right;
}

.mynice {
  font-size: 18px;
  color: #333;
  font-weight: 600;
}

.mynice span {
  content: '';
  border-left: 3px solid #00B38A;
  height: 16px;
  width: 3px;
  left: -7px;
  top: 50%;
  transform: translateY(-50%);
}

.el-radio-button /deep/ .el-radio-button__inner {
  border: 0;
}

.work-name span {
  border-left: 0;
  font-size: 16px;
  color: #333;
  margin-left: 50px;
  font-weight: 600;
}
</style>
