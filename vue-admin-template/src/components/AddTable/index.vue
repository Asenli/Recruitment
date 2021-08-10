<template>
  <div class="mynice">
    <span> 工作经历</span>
    <i class="el-icon-plus" @click="showDg3()"   title="添加"></i>
    <div v-for="(sureWork, i) in sureWorks" :key="i" class="work-class">
      <div v-if="sureWork" class="work-name">
        <span>{{ sureWork.name }}</span>
        <span v-if="sureWork.date1" style="margin-left: 10%;">{{ sureWork.date1[0] }}-{{ sureWork.date1[1] }}</span>
        <i class="el-icon-edit" style="padding-left: 10px;" @click="showDg3(sureWork, i)"  title="编辑"></i>
        <i
          class="el-icon-delete"
          style="cursor: pointer;color: #409EFF;float: right;"
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
          <quill-editor
            ref="myTextEditor"
            v-model="work.cotent"
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
</template>

<script>
import { quillEditor } from 'vue-quill-editor'

export default {
  name: 'Index',
  components: {
    quillEditor
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

      }
    }
  },
  mounted() {
    this.$axios.get('/userinfo/?user_id=' + localStorage.getItem('userId')).then(res => {
      if (res.data.code === 200 && res.data.data.config) {
        this.sureWorks = res.data.data.config.surework
      }
    })
  },
  methods: {
    unAddButton(tag) {
      const index = this.checkboxGroup2.indexOf(tag)
      if (index > -1) {
        this.checkboxGroup2.spilce(index, 1)
      }
    },
    // 选择标签
    selectRadio(data) {
      this.dialogFormVisible4 = false
      console.log(this.checkboxGroup2)
      this.workTag = this.checkboxGroup2
    },
    onEditorFocus(data) {
      console.log(data)
    },
    deleteDg3(i) {
      // 删除工作经历
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
          'tag': '',
          'dept': '',
          'vocation': '',
          'date1': '',
          'cotent': ''
        }
      }
      this.dialogFormVisible3 = true
    },
    // 选择标签 弹框
    chooseTag() {
      this.dialogFormVisible4 = true
    },
    onEditorBlur() {
      // 失去焦点事件
    },
    onEditorChange() {
      // 内容改变事件
      this.$emit('input', this.sureWorks)
    },
    sureWork(data) {
      // 将工作经历数据传回 首页
      this.data.surework = data
      this.saveUserInfo()
    },
    // 我的工作经历
    myWork(data, i) {
      const sureWorkData = {
        name: this.work.name,
        tag: this.work.tag,
        dept: this.work.dept,
        vocation: this.work.vocation,
        date1: this.work.date1,
        cotent: this.work.cotent,
        // 行业标签
        checkboxGroup2: this.checkboxGroup2
      }
      if (this.editTag) {
        // console.log('修改')
        this.sureWorks.splice(i, 1, data)
        this.editTag = ''
      } else {
        // 保存
        this.sureWorks.push(sureWorkData)
        this.$axios.post('/userinfo/', { config: this.sureWorks }).then(res => {
          // 要发送多次请求  把列表 变成了字段传到后台？？？？？？？？？？？？？？
          console.log(res)
        })
      }
      this.$emit('sure-work', sureWorkData)
      this.dialogFormVisible3 = false
    }
  }
}
</script>

<style scoped>
.el-icon-edit {
  cursor: pointer;
  color: #409EFF;
  float: right;
}
.el-icon-plus {
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
  margin-left: 20%;
  font-weight: 600;
}

.work-class {
  font-size: 14px;
  min-height: 20px;
  margin-top: 1%;
  border: 2px solid #c7c7c7;
}
</style>
