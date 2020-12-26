<template>
  <div class="login-container">
    <el-form
      ref="loginForm"
      :model="loginForm"
      :rules="loginRules"
      class="login-form"
      auto-complete="on"
      label-position="left"
    >

      <div class="title-container">
        <h3 class="title">人才公会</h3>
      </div>

      <el-form-item prop="username">
        <span class="svg-container">
          <svg-icon icon-class="user" />
        </span>
        <el-input
          ref="username"
          v-model="loginForm.username"
          placeholder="Username"
          name="username"
          type="text"
          tabindex="1"
          auto-complete="on"
        />
      </el-form-item>

      <el-form-item prop="password">
        <span class="svg-container">
          <svg-icon icon-class="password" />
        </span>
        <el-input
          :key="passwordType"
          ref="password"
          v-model="loginForm.password"
          :type="passwordType"
          placeholder="Password"
          name="password"
          tabindex="2"
          auto-complete="on"
          @keyup.enter.native="handleLogin"
        />
        <span class="show-pwd" @click="showPwd">
          <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
        </span>
      </el-form-item>

      <el-button
        :loading="loading"
        type="primary"
        style="width:100%;margin-bottom:30px;"
        @click.native.prevent="handleLogin"
      >登录
      </el-button>
      <div class="tips" />
      <div style="position:relative">
        <a style="padding-left: 20px;cursor: pointer;color:rgb(150, 150, 150);" @click="register">注册</a>
        <!--                    <router-link to="/">注册</router-link>-->
        <a style="cursor: pointer;padding-left:10px;float: right;color: #969696;" @click="showDialog=true"> 忘记密码？</a>
        <!--        <el-button class="thirdparty-button" type="primary" @click="showDialog=true">-->
        <!--          注册-->
        <!--        </el-button>-->
        <!--        <el-button class="thirdparty-button" type="primary" @click="showDialog=true">-->
        <!--          找回-->
        <!--        </el-button>-->
      </div>
    </el-form>
    <el-dialog title="注册" :visible.sync="toRegister">
      <el-row class="register">
        <el-col :span="12" style="width:100%;margin-top: 25px;">
          <div class="grid-content bg-purple-light">
            <div style="width: 100%">
              <div class="login-table">
                <el-form
                  ref="ruleForm"
                  :model="params"
                  status-icon
                  :rules="rules"
                  label-width="100px"
                  class="demo-ruleForm"
                >
                  <el-form-item label="账户名" class="input-left" prop="username">
                    <el-input v-model="params.username" />
                  </el-form-item>
                  <el-form-item class="input-left" prop="email">
                    <label slot="label">邮&nbsp;&nbsp;&nbsp;&nbsp;箱</label>
                    <el-input v-model="params.email" />
                  </el-form-item>
                  <el-form-item label="手机号" class="input-left" prop="phone">
                    <el-input v-model.number="params.phone" />
                  </el-form-item>
                  <el-form-item label="设置密码" class="input-left" prop="password">
                    <el-input v-model="params.password1" maxlength="20" show-password />
                    <span v-if="errMsg" style="font-size: 8px;color: red;">{{ errMsg }}</span>
                  </el-form-item>
                  <el-form-item maxlength="20" label="确认密码" class="input-left" prop="password">
                    <el-input v-model="params.password2" show-password />
                    <span v-if="errMsg2" style="font-size: 8px;color: red;">{{ errMsg2 }}</span>
                  </el-form-item>
                </el-form>
                <div style="font-size: 0.1rem;margin-bottom: 1rem">
                  <span style="color: #a2a2a2;">注册即同意</span>
                  <span style="color: #ff552e">《人才公会使用协议》</span>
                  <span style="color: #a2a2a2;">&</span>
                  <span style="color: #ff552e">《隐私政策》</span>
                </div>
                <a style="cursor: pointer" @click="register">已有账号？去登录</a>
                <!--                <router-link to="/login">已有账号？去登录</router-link>-->
                <el-button type="primary" style="width: 300px;margin: 10px 0 10px 0;" @click="submitForm">确定
                </el-button>
              </div>
            </div>
          </div>
        </el-col>
      </el-row>
    </el-dialog>
  </div>
</template>

<script>
import { validUsername } from '@/utils/validate'
import { subForm } from '../../api/user'

export default {
  name: 'Login',
  data() {
    const validateUsername = (rule, value, callback) => {
      if (!validUsername(value)) {
        callback(new Error('Please enter the correct user name'))
      } else {
        callback()
      }
    }
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('The password can not be less than 6 digits'))
      } else {
        callback()
      }
    }
    return {
      toRegister: false,
      params: {
        username: 'lidongbing',
        phone: '15008438840',
        password1: 'ldb886718959',
        password2: 'ldb886718959',
        email: '634163114@qq.com',
        // 验证码
        code: ''
      },
      loginForm: {
        username: 'lidongbing',
        password: 'ldb886718959'
      },
      loginRules: {
        username: [{ required: true, trigger: 'blur', validator: validateUsername }],
        password: [{ required: true, trigger: 'blur', validator: validatePassword }]
      },
      loading: false,
      passwordType: 'password',
      redirect: undefined
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        this.redirect = route.query && route.query.redirect
      },
      immediate: true
    },
    //  密码验证
    params: {
      handler(newVal) {
        // r如果是登录菜单 就不效验证 密码
        if (!this.toRegister) {
          this.errMsg = ''
        }
        if ((this.checkStrong(newVal.password1)) < 4) {
          this.errMsg = '必须6-20位，包含字母、数字、特殊字符'
        } else {
          this.errMsg = ''
        }
        if (newVal.password2 !== newVal.password1) {
          this.errMsg2 = '两次密码不一致'
        } else {
          this.errMsg2 = ''
        }
      },
      deep: true,
      immediate: true
    }
  },
  methods: {
    // 提交注册账号
    submitForm(formName) {
      this.$refs.ruleForm.validate((valid) => {
        if (valid) {
          console.log(this.params)
          subForm(this.params).then(res => {
            console.log(res)
            if (res.status === false) {
              alert(res.msg)
            } else {
              this.register()
            }
            this.errInfo = false
            this.info = ''
          }).catch(error => {
            alert('注册异常')
            console.log(error)
          })
          // this.$axios.post(this.ip + '/register/', this.params).then(res => {
          //   if (res.data.status) {
          //     this.register()
          //   }
          //   alert(res.data.msg)
          //   this.errInfo = false
          //   this.info = ''
          //   // this.$router.push({path: 'login'})
          // })
        } else {
          alert('注册异常')
          return false
        }
      })
    },
    // 注册弹框
    register() {
      this.toRegister = !this.toRegister
    },
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },
    handleLogin() {
      this.$refs.loginForm.validate(valid => {
        if (valid) {
          // this.loading = true
          this.$store.dispatch('user/login', this.loginForm).then(() => {
            this.$router.push({ path: this.redirect || '/' })
            this.loading = false
          }).catch(() => {
            this.loading = false
          })
        } else {
          debugger
          console.log('error submit!!')
          return false
        }
      })
    }
  }
}
</script>

<style lang="scss">
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

$bg: #283443;
$light_gray: #fff;
$cursor: #fff;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.login-container {
  .el-input {
    display: inline-block;
    height: 47px;
    width: 85%;

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 12px 5px 12px 15px;
      color: $light_gray;
      height: 47px;
      caret-color: $cursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px $bg inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
  }
}
</style>

<style lang="scss" scoped>
$bg: #2d3a4b;
$dark_gray: #889aa4;
$light_gray: #eee;

.login-container {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;

  .login-form {
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 160px 35px 0;
    margin: 0 auto;
    overflow: hidden;
  }

  .tips {
    font-size: 14px;
    color: #fff;
    margin-bottom: 10px;

    span {
      &:first-of-type {
        margin-right: 16px;
      }
    }
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 26px;
      color: $light_gray;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }
}
</style>
