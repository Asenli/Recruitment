<template>
  <div class="jianli" style="height: 100%;display: flex;flex-direction: column;margin: 20px 100px 100px 100px;">
    <div style="height: 35px;">
      <div style="">
        <span>期望职位：</span>
        <el-input v-model="expect" style="width: 220px;" placeholder="请输入意向岗位" />
        <span style="margin-left: 20px;">求职状态：</span>
        <el-select v-model="statu" placeholder="请选择当前状态">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
      </div>
    </div>
    <div style="margin-top: 35px;height: 10%;border: 1px solid #b6afaf;padding: 10px;border-radius: 10px;box-shadow: 0 0 0 10px #eeeef0;">
      <div class="basic-info">
        <p class="basic-name female" style="margin-top: 5px;">
          <span style="font-size: 25px;color: #333;font-weight: 600;">{{ form.name }}</span>
          <i class="el-icon-edit" @click="dialogFormVisible = true">编辑</i>
        </p>
        <p style="margin-top: 5px;">
          <span class="basic-company">{{ form.company }}</span>
          <!--            <span> / </span>-->
          <!--            <span class="basic-job"></span>-->
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
        <el-dialog title="基本信息" :visible.sync="dialogFormVisible">
          <el-form :model="dialog_form" :rules="rules" :inline="true">
            <el-form-item label="姓名" label-width="119px">
              <el-input
                v-model="dialog_form.name"
                type="text"
                placeholder="请输入内容"
                maxlength="20"
                style="width: 140px"
              />
            </el-form-item>
            <el-form-item label="生日" label-width="119px">
              <el-date-picker v-model="dialog_form.date0" type="date" placeholder="年月日" style="width: 140px" />
            </el-form-item>
            <el-form-item label="年龄" label-width="119px">
              <el-input
                v-model="dialog_form.age"
                oninput="if(value.length>2)value=value.replace(/[^\d]/g,'').slice(0,2)"
                placeholder="请输入年龄"
                type="number"
                maxlength="2"
                style="width: 140px"
              />
            </el-form-item>
            <el-form-item label="学历" label-width="119px">
              <el-select v-model="dialog_form.education" style="width: 140px" placeholder="请选择">
                <el-option
                  v-for="item in options_education"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-form-item>
            <el-form-item label="专业" label-width="119px">
              <el-input
                v-model="dialog_form.major"
                placeholder="请输入专业"
                type="text"
                style="width: 140px"
              />
            </el-form-item>
            <el-form-item label="性别" label-width="119px">
              <el-select v-model="dialog_form.sex" style="width: 140px" placeholder="请选择">
                <el-option
                  v-for="item in options_sex"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-form-item>
            <el-form-item label="电话" label-width="119px">
              <el-input
                v-model="dialog_form.mobile"
                oninput="if(value.length>11)value=value.replace(/[^\d]/g,'').slice(0,11)"
                placeholder="请输入电话"
                type="text"
                maxlength="13"
                style="width: 140px"
                clearable
              />
            </el-form-item>
            <el-form-item label="邮箱" label-width="119px" prop="buyerEmail" required>
              <el-input v-model="dialog_form.buyerEmail" style="width: 140px" clearable />
            </el-form-item>
            <el-form-item label="工作经验" label-width="119px">
              <el-input
                v-model="dialog_form.workYear"
                oninput="if(value.length>2)value=value.replace(/[^\d]/g,'').slice(0,2)"
                placeholder="请输入年限"
                type="number"
                maxlength="2"
                style="width: 130px"
              />年
            </el-form-item>
            <el-form-item v-show="false" label="开始工作" label-width="119px">
              <el-date-picker
                v-model="dialog_form.date1"
                type="month"
                placeholder="年月"
                style="width: 140px"
              />
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="sureBase()">确 定</el-button>
          </div>
        </el-dialog>
      </div>
    </div>
    <div style="margin-top: 30px;height: 30%;border: 1px solid #b6afaf;padding: 10px;border-radius: 10px;box-shadow: 0 0 0 10px #eeeef0;">
      <p class="mynice">
        <span style="font-size: 26px;color: #333;font-weight: 600;"> 个人优势</span>
        <i class="el-icon-edit" @click="dialogFormVisible2 = true">编辑</i>
      </p>
      <div class="ql-editor" v-html="myCotent" />
      <el-dialog title="个人优势" :visible.sync="dialogFormVisible2">
        <el-form :model="form">
          <el-form-item>
            <quill-editor
              ref="myTextEditor"
              v-model="myYouShi"
              :options="editorOption"
              @blur="onEditorBlur($event)"
              @focus="onEditorFocus($event)"
            />
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible2 = false">取 消</el-button>
          <el-button type="primary" @click="myNiceSub">确 定</el-button>
        </div>
      </el-dialog>
    </div>
    <div style="margin-top: 30px;height: 40%;border: 1px solid #b6afaf;padding: 10px;border-radius: 10px;box-shadow: 0 0 0 10px #eeeef0;">
      <div class="mynice">
        <span style="font-size: 26px;color: #333;font-weight: 600;"> 工作经历</span>
        <i class="el-icon-edit" @click="showDg3()">添加</i>
        <div v-for="(sureWork, i) in sureWorks" :key="i" class="work-class">
          <!--          {{ sureWork }}-->
          <div v-if="sureWork" class="work-name">
            <span>{{ sureWork.name }}</span>
            <span>{{ sureWork.dept }}</span>
            <span>{{ sureWork.vocation }}</span>
            <span v-if="sureWork.date1" style="margin-left: 10%;">{{ sureWork.date1[0] }}-{{ sureWork.date1[1] }}</span>
            <i class="el-icon-edit" style="padding-left: 10px;" @click="showDg3(sureWork, i)">编辑</i>
            <i
              class="el-icon-delete"
              style="cursor: pointer;color: #00B38A;float: right;"
              @click="deleteDg3(i)"
            >删除</i>
          </div>
          <!--          <p style="margin-left: 20%;">{{ sureWork.vocation }}</p>-->
          <div class="ql-editor" style="margin: 2%;" v-html="sureWork.content" />
        </div>
        <el-dialog title="工作经历" :visible.sync="dialogFormVisible3">
          <el-form :model="work">
            <el-form-item label-width="120px" label="公司名称">
              <el-input v-model="work.name" />
            </el-form-item>
            <el-form-item label-width="120px" label="行业标签">
              <el-button @click="chooseTag">选择标签</el-button>
              <el-button v-for="(tag,index) in workTag" :key="index" type="primary">
                {{ tag }}
              </el-button>
            </el-form-item>
            <el-form-item label-width="120px" label="所属部门">
              <el-input v-model="work.dept" />
            </el-form-item>
            <el-form-item label-width="120px" label="职业类型">
              <el-input v-model="work.vocation" />
            </el-form-item>
            <el-form-item label-width="120px" label="在职时间">
              <!--                  <el-input v-model="work.date1"></el-input>-->
              <el-date-picker
                v-model="work.date1"
                type="monthrange"
                range-separator="至"
                value-format="yyyy.MM"
                start-placeholder="开始日期"
                end-placeholder="结束日期"
              />
            </el-form-item>
            <el-form-item label-width="120px" label="工作内容">
              <!--              // 富文本框-->
              <quill-editor
                ref="myTextEditor"
                v-model="content"
                :options="editorOption"
                @blur="onEditorBlur($event)"
                @focus="onEditorFocus($event)"
              />
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible3 = false">取 消</el-button>
            <el-button type="primary" @click="myWork(work, editTag)">确 定</el-button>
          </div>
        </el-dialog>
        <el-dialog title="行业标签" :visible.sync="dialogFormVisible4">
          <!--      <div style="margin-top: 20px">-->
          <!--        <el-radio-group v-model="work.tag" size="medium">-->
          <!--          <el-checkbox   v-for="(name,i) in tagList" :key="i" :label="name" >{{name}}</el-checkbox>-->
          <!--&lt;!&ndash;          <el-radio-button style="margin:2%;" v-for="(name,i) in tagList" :key="i" :label="name">{{name}}&ndash;&gt;-->
          <!--&lt;!&ndash;          </el-radio-button>&ndash;&gt;-->
          <!--        </el-radio-group>-->
          <!--      </div>-->
          <div style="margin-top: 20px">
            <el-checkbox-group v-model="checkboxGroup2" size="medium">
              <el-checkbox-button v-for="(name,i) in tagList" :key="i" :label="name">{{ name }}</el-checkbox-button>
            </el-checkbox-group>
          </div>
          <div slot="footer" class="dialog-footer">
            <el-button @click="selectRadio">确定</el-button>
          </div>
        </el-dialog>
      </div>
    </div>
    <div style="text-align: center;margin-top: 4%;"><el-button size="small" type="primary" @click="save_info">保存</el-button></div>
  </div>
</template>

<script>
// import Tinymce from '@/components/Tinymce'
import { save_data } from '@/api/jian'
import { quillEditor } from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
import { jian_info } from '../../api/jian'
export default {
  name: 'Index',
  components: { quillEditor },
  data() {
    var checkEmail = (rule, value, callback) => {
      const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/
      if (!value) {
        return callback(new Error('邮箱不能为空'))
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback()
        } else {
          callback(new Error('请输入正确的邮箱格式'))
        }
      }, 100)
    }
    return {
      user_id: localStorage.getItem('user_id'),
      // 个人优势弹框
      editorOption: {
        theme: 'snow',
        modules: {
          toolbar: [
            [{ 'list': 'bullet' }, { 'list': 'ordered' }],
            ['bold']
          ]
        }
      },
      options_sex: [{
        value: '男',
        label: '男'
      }, {
        value: '女',
        label: '女'
      }],
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
      rules: {
        buyerEmail: [
          { validator: checkEmail, trigger: 'blur' }
        ]
      },
      dialogFormVisible3: false,
      dialogFormVisible4: false,
      // 个人优势编辑内容
      myYouShi: '',
      // 个人优势确认后
      myCotent: '',
      tagList: ['电商', '体育', '教育', '广告营销', '本地生活', '分类信息',
        '新零售', '汽车', '旅游', '医疗健康', '企业服务', '物流', '游戏', '社交',
        '信息安全', '即使通讯', '地图', '云计算', '大数据', '工具软件',
        '房地产', '招聘', '金融', '保险', '硬件', '其他'
      ],
      checkboxGroup2: [],
      // 选中的Tag
      workTag: [],
      // 工作经历tag
      editTag: '',
      // 确认工作经历
      sureWorks: [
        {
          'checkboxGroup2': [''],
          'name': '',
          'tag': '1',
          'dept': '',
          'vocation': '',
          'date1': '',
          'content': ''
        }
      ],
      work: {
        'name': '',
        'tag': '',
        'dept': '',
        'vocation': '',
        'date1': '',
        'cotent': ''

      },
      dialogFormVisible: false,
      form: {
        education: '学历',
        name: 'XXX',
        // 出生
        date0: '',
        // 工作时间
        date1: '',
        // 专业
        major: 'xxx',
        workYear: 1,
        mobile: '00000000000',
        city: '',
        // 性别
        sex: '性别',
        email: 'xxxxx@qq.com',
        // 住址
        address: 'xxxxx区xxx街道',
        age: 20
      },
      // 基本信息弹框表单
      dialog_form: {
        education: '',
        name: '',
        // 出生
        date0: '',
        // 工作时间
        date1: '',
        // 专业
        major: '',
        workYear: 0,
        mobile: '',
        city: '',
        // 性别
        sex: '',
        buyerEmail: '',
        // 住址
        address: '',
        age: ''
      },
      dialogFormVisible2: false,
      statu: '',
      expect: '', // 期望意向
      options: [{
        value: '离职-随时到岗',
        label: '离职-随时到岗'
      }, {
        value: '在职-月内到岗',
        label: '在职-月内到岗'
      }, {
        value: '在职-考虑机会',
        label: '在职-考虑机会'
      }, {
        value: '在职-暂不考虑',
        label: '在职-暂不考虑'
      }
      ],
      content:
        `<ul>
        <li>工作职责...</li><li>工作内容...</li><li>工作成果...</li>
      </ul>`
    }
  },
  created() {
    this.getInfo()
  },
  methods: {
    getInfo() {
      return new Promise((resolve, reject) => {
        jian_info(this.user_id).then(data => {
          this.form = data.data
          this.dialog_form = data.data
          this.statu = data.data.statu
          this.myCotent = data.data.myCotent
          this.expect = data.data.expect
          this.sureWorks = data.data.sureWorks
        }).catch(error => {
          reject(error)
        })
      })
    },
    deleteDg3(i) {
      // 移除删除工作经历
      this.sureWorks.splice(i, 1)
    },
    showDg3(data, i) {
      // 工作经历弹框
      if (data) {
        this.work = data
        this.editTag = i
      } else {
        this.work = {
          'name': '',
          'dept': '',
          'vocation': '',
          'date1': ''
        }
      }
      this.dialogFormVisible3 = true
    },
    // 编辑个人经历
    myWork(data, i) {
      console.log(this.work)
      const sureWork = {
        name: this.work.name,
        tag: this.workTag,
        dept: this.work.dept,
        vocation: this.work.vocation,
        date1: this.work.date1,
        content: this.content
      }
      if (this.editTag) {
        this.sureWorks.splice(i, 1, data)
        this.editTag = ''
      } else {
        this.sureWorks.push(sureWork)
      }
      console.log(this.sureWorks)
      this.dialogFormVisible3 = false
    },
    // 选择标签
    selectRadio(data) {
      this.dialogFormVisible4 = false
      this.workTag = this.checkboxGroup2
    },
    onEditorBlur() {
      // 失去焦点事件
    },
    onEditorFocus(data) {
      console.log(data)
    },
    onEditorChange() {
      // 内容改变事件
      this.$emit('input', this.content)
    },
    // 选择标签 弹框
    chooseTag() {
      this.dialogFormVisible4 = true
    },
    // 保存个人优势
    myNiceSub() {
      this.myCotent = this.myYouShi
      this.dialogFormVisible2 = false
    },
    // 保存基础信息
    sureBase() {
      // this.data.base = this.form
      // this.save_info()
      this.dialogFormVisible = false
      this.form = this.dialog_form
    },
    // 保存简历
    save_info() {
      const datas = {}
      datas['username'] = this.form.name
      datas['education'] = this.form.education
      datas['name'] = this.form.name
      datas['date0'] = this.form.date0
      datas['date1'] = this.form.date1
      datas['major'] = this.form.major
      datas['workYear'] = this.form.workYear
      datas['phone'] = this.form.mobile
      datas['email'] = this.form.buyerEmail
      datas['city'] = this.form.city
      datas['sex'] = this.form.sex
      datas['address'] = this.form.address
      datas['age'] = this.form.age
      // 当前状态
      datas['statu'] = this.statu
      datas['myCotent'] = this.myCotent
      // 希望意向
      datas['expect'] = this.expect
      datas['sureWorks'] = this.sureWorks
      datas['config'] = {
        form: this.form,
        myCotent: this.myCotent,
        statu: this.statu,
        expect: this.expect,
        sureWorks: this.sureWorks
      }
      // datas['user_id'] = 1
      console.log(datas)
      return new Promise((resolve, reject) => {
        save_data(datas).then((response) => {
          console.log(response)
        }).catch(error => {
          reject(error)
        })
      })
    }
  }
}
</script>

<style scoped>
.work-class {
  font-size: 14px;
  min-height: 20px;
  margin-top: 1%;
  /*border: 2px solid #c7c7c7;*/
}

.el-icon-edit {
  cursor: pointer;
  color: #00B38A;
  float: right;
}

.mynice {
  /*font-size: 18px;*/
  /*color: #333;*/
  /*font-weight: 600;*/
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
  /*font-size: 16px;*/
  color: #333;
  margin-left: 10%;
  /*font-weight: 600;*/
}

#app .hideSidebar .main-container {
  width: 100%;
  height: 100%;
}

#app .main-container {
  margin-left: 327px;
}

.el-dialog{
  display: flex;
  flex-direction: column;
  margin:0 !important;
  position:absolute;
  top:50%;
  left:50%;
  transform:translate(-50%,-50%);
  /*height:600px;*/
  max-height:calc(100% - 30px);
  max-width:calc(100% - 30px);
}
.el-dialog .el-dialog__body{
  flex:1;
  overflow: auto;
}
</style>
