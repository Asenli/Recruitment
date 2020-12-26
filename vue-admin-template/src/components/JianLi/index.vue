<template>
  <div class="main" style="margin: 36px;">
    <div class="basic-info">
      <el-button style="float: right;" size="small" type="primary" @click="save_info">保存</el-button>
      <p class="basic-name female">
        <span style="font-size: 25px;color: #333;font-weight: 600;">{{ form.name }}</span>
        <i class="el-icon-edit" @click="dialogFormVisible = true">编辑</i>
      </p>
      <p>
        <span class="basic-company">软通动力成都分公司</span>
        <span> / </span>
        <span class="basic-job">Python</span>
      </p>
      <p class="basic-self">
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
        <el-form :model="form">
          <el-form-item label="姓名" label-width="119px">
            <el-input v-model="form.name" type="text" placeholder="请输入内容" maxlength="20" show-word-limit />
          </el-form-item>
          <el-form-item label="生日" label-width="119px">
            <el-date-picker v-model="form.date0" type="date" placeholder="年月日" />
          </el-form-item>
          <el-form-item label="性别" label-width="119px">
            <el-radio v-model="form.sex" label="男" border>男</el-radio>
            <el-radio v-model="form.sex" label="女" border>女</el-radio>
          </el-form-item>
          <el-form-item label="学历" label-width="119px">
            <el-radio v-model="form.education" label="本科" border>本科</el-radio>
            <el-radio v-model="form.education" label="专科" border>专科</el-radio>
            <el-radio v-model="form.education" label="研究生" border>研究生</el-radio>
          </el-form-item>
          <el-form-item label="手机号码" label-width="119px">
            <el-input
              v-model="form.mobile"
              type="num"
              placeholder="请输入内容"
              maxlength="12"
              show-word-limit
            />
          </el-form-item>
          <el-form-item label="联系邮箱" label-width="119px">
            <el-input
              v-model="form.email"
              type="text"
              placeholder="请输入内容"
              show-word-limit
            />
          </el-form-item>
          <el-form-item label="开始工作" label-width="119px">
            <el-date-picker
              v-model="form.date1"
              type="month"
              placeholder="年月"
            />
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="sureBase()">确 定</el-button>
        </div>
      </el-dialog>
    </div>
    <div
      class="my-nice-info"
      style="text-align: left;"
    >
      <p class="mynice">
        <span style="font-size: 26px;color: #333;font-weight: 600;"> 个人优势</span>
        <i class="el-icon-edit">编辑</i>
      </p>
      <div class="ql-editor" v-html="myCotent" />
      <!--      <el-dialog title="个人优势" :visible.sync="dialogFormVisible2">-->
      <!--        <el-form :model="form">-->
      <!--          <el-form-item>-->
      <!--            <quill-editor-->
      <!--              ref="myTextEditor"-->
      <!--              v-model="myNiceList"-->
      <!--              :options="editorOption"-->
      <!--            />-->
      <!--          </el-form-item>-->
      <!--        </el-form>-->
      <!--        <div slot="footer" class="dialog-footer">-->
      <!--          <el-button @click="dialogFormVisible2 = false">取 消</el-button>-->
      <!--          <el-button type="primary" @click="myNiceSub">确 定</el-button>-->
      <!--        </div>-->
      <!--      </el-dialog>-->
      <div class="mynice">
        <span style="font-size: 26px;color: #333;font-weight: 600;"> 工作经历</span>
        <i class="el-icon-edit" @click="showDg3()">添加</i>
        <div v-for="(sureWork, i) in sureWorks" :key="i" class="work-class">
          <div v-if="sureWork" class="work-name">
            <span>{{ sureWork.name }}</span>
            <span v-if="sureWork.date1" style="margin-left: 10%;">{{ sureWork.date1[0] }}-{{ sureWork.date1[1] }}</span>
            <i class="el-icon-edit" style="padding-left: 10px;" @click="showDg3(sureWork, i)">编辑</i>
            <i
              class="el-icon-delete"
              style="cursor: pointer;color: #00B38A;float: right;"
              @click="deleteDg3(i)"
            >删除</i>
          </div>
          <p style="margin-left: 20%;">{{ sureWork.vocation }}</p>
          <div class="ql-editor" style="margin: 2%;" v-html="sureWork.cotent" />
        </div>
        <el-dialog title="工作经历" :visible.sync="dialogFormVisible3">
          <el-form :model="work">
            <el-form-item label-width="120px" label="公司名称">
              <el-input v-model="work.name" />
            </el-form-item>
            <el-form-item label-width="120px" label="行业标签">
              <el-button @click="chooseTag">选择标签</el-button>
              <el-button v-for="(tag,index) in workTag" :key="index" type="primary" @click="unAddButton">
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
              <tinymce v-model="content" :height="300" />
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
      <div style="margin-top: 1%;">
        <span>求职期望：</span>
        <el-input v-model="expect" style="width: 220px;" placeholder="请输入意向岗位" />
        <span>求职状态：</span>
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
  </div>
</template>

<script>
import Tinymce from '@/components/Tinymce'
import { save_data } from '@/api/jian'
// import { getInfo } from '../../api/user'
// import { getToken } from '@/utils/auth'
export default {
  name: 'Index',
  components: { Tinymce },
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
      },
      dialogFormVisible3: false,
      dialogFormVisible4: false,
      checkboxGroup2: [],
      tagList: ['电商', '体育', '教育', '广告营销', '本地生活', '分类信息',
        '新零售', '汽车', '旅游', '医疗健康', '企业服务', '物流', '游戏', '社交',
        '信息安全', '即使通讯', '地图', '云计算', '大数据', '工具软件',
        '房地产', '招聘', '金融', '保险', '硬件'
      ],
      // 工作经历tag
      editTag: '',
      // 选中的Tag
      workTag: [],
      // 确认工作经历
      sureWorks: [
        {
          'checkboxGroup2': [],
          'name': '',
          'tag': '22',
          'dept': '无线',
          'vocation': 'python',
          'date1': '2019-01-28',
          'cotent': '2'
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
      myCotent: '<p>熟悉网络编程，了解HTTP/TCP/UDP等网络协议、Ajax等开发技术；</p><p>熟悉python多线程，多进程开发；</p><p>熟练运用web 开发框架Django、flask开发框架；</p><p>熟练使用MySQL数据库，非关系型数据库Redis、MongoDB的使用;</p><p>熟悉vue、Bootstrap、HTML5、CSS、AJAX等前端;</p><ol><li>了解docker、odoo；</li></ol>',
      form: {
        education: '本科',
        name: '李东兵',
        // 出生
        date0: '',
        // 工作时间
        date1: '',
        // 专业
        major: '计算机',
        workYear: 1,
        mobile: 15008438839,
        city: '',
        // 性别
        sex: '男',
        email: '634163113@qq.com',
        // 住址
        address: '',
        age: '20'
      },
      statu: '离职-随时到岗',
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
        `<h1 style="text-align: center;">请填写工作经历</h1><ul>
        <li>Our <a href="//www.tinymce.com/docs/">documentation</a> is a great resource for learning how to configure TinyMCE.</li><li>Have a specific question? Visit the <a href="https://community.tinymce.com/forum/">Community Forum</a>.</li><li>We also offer enterprise grade support as part of <a href="https://tinymce.com/pricing">TinyMCE premium subscriptions</a>.</li>
      </ul>`
    }
  },
  methods: {
    // 选择标签 弹框
    chooseTag() {
      this.dialogFormVisible4 = true
    },
    // 保存基础信息
    sureBase() {
      this.dialogFormVisible = false
      // this.data.base = this.form
      // this.saveUserInfo()
    },
    showDg3(data, i) {
      // 工作经历弹框
      if (data) {
        this.work = data
        this.editTag = i
      } else {
        this.work = {
          'name': '',
          'tag': '',
          'dept': '',
          'vocation': '',
          'date1': '',
          'cotent': ''
        }
      }
      this.dialogFormVisible3 = true
    },
    save_info() {
      const datas = {}
      datas['phone'] = this.form.mobile
      datas['email'] = this.form.email
      datas['username'] = this.form.name
      datas['education'] = this.form.education
      datas['name'] = this.form.name
      datas['date0'] = this.form.date0
      datas['date1'] = this.form.date1
      datas['major'] = this.form.major
      datas['workYear'] = this.form.workYear
      datas['major'] = this.form.major
      datas['phone'] = this.form.mobile
      datas['city'] = this.form.city
      datas['sex'] = this.form.sex
      datas['email'] = this.form.email
      datas['sex'] = this.form.sex
      datas['address'] = this.form.address
      datas['age'] = this.form.age
      datas['statu'] = this.form.statu
      datas['myCotent'] = this.myCotent
      datas['expect'] = this.expect
      datas['sureWorks'] = this.sureWorks

      // datas['myCotent'] = this.myCotent
      // // 当前状态
      // datas['statu'] = this.statu
      // // 希望意向
      // datas['expect'] = this.expect
      // datas['sureWorks'] = this.sureWorks
      datas['config'] = { form: this.form, myCotent: this.myCotent, statu: this.statu, expect: this.expect, sureWorks: this.sureWorks }
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
  border: 2px solid #c7c7c7;
}

.el-icon-edit {
  cursor: pointer;
  color: #00B38A;
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
  margin-left: 20%;
  font-weight: 600;
}
</style>
