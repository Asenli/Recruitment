<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.name" placeholder="输入姓名" style="width: 120px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-select v-model="listQuery.importance" placeholder="选择工作状态" clearable style="width: 150px" class="filter-item">
        <el-option v-for="item in importanceOptions" :key="item" :label="item" :value="item" />
      </el-select>
      <el-select v-model="listQuery.importance2" placeholder="选择学历" clearable style="width: 150px" class="filter-item">
        <el-option v-for="item in importanceOptions2" :key="item" :label="item" :value="item" />
      </el-select>
      <el-select v-model="listQuery.importance3" placeholder="选择专业" clearable style="width: 150px" class="filter-item">
        <el-option v-for="item in importanceOptions3" :key="item" :label="item" :value="item" />
      </el-select>
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        搜索
      </el-button>
    </div>
    <el-table
      v-loading="listLoading"
      :data="data_list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
      @sort-change="sortChange"
    >
      <el-table-column label="序号" prop="id" sortable="custom" align="center" :class-name="getSortClass('id')">
        <template slot-scope="scope">
          <span>{{ scope.row.id }}</span>
        </template>
      </el-table-column>
      <!--      <el-table-column align="center" label="ID" width="95">-->
      <!--        <template slot-scope="scope">-->
      <!--          {{ scope.$index }}-->
      <!--        </template>-->
      <!--      </el-table-column>-->
      <el-table-column label="姓名" align="center">
        <template slot-scope="scope">
          <span>  {{ scope.row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="期望岗位">
        <template slot-scope="scope">
          {{ scope.row.expect }}
        </template>
      </el-table-column>
      <el-table-column label="求职状态" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.statu }}</span>
        </template>
      </el-table-column>
      <el-table-column label="专业" align="center">
        <template slot-scope="scope">
          {{ scope.row.major }}
        </template>
      </el-table-column>
      <el-table-column label="学历" align="center">
        <template slot-scope="scope">
          {{ scope.row.education }}
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="年龄" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.age | statusFilter">{{ scope.row.age }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="性别" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.sex | statusFilter">{{ scope.row.sex }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="邮箱" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.email | statusFilter">{{ scope.row.email }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column align="center" prop="created_at" label="更新时间">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.add_time }}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="操作">
        <template slot-scope="scope">
          <span>
            <el-button @click="detail(scope)">详情</el-button>
          </span>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog v-el-drag-dialog class="abow_dialog" :visible.sync="dialogTableVisible" title="个人简历" @dragDialog="handleDrag">
      <jian-li-show />
    </el-dialog>
  </div>
</template>

<script>
import { fetchList } from '@/api/table'
import { getInfo } from '../../api/user'
import elDragDialog from '@/directive/el-drag-dialog'
import JianLiShow from '@/components/JianLiShow'
export default {
  directives: { elDragDialog },
  components: { JianLiShow },
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'gray',
        deleted: 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      dialogTableVisible: false,
      data_list: [
        { row: { title: 1, author: 2, pageviews: 3, status: 4, display_time: 22 }}
      ],
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        importance: [],
        importance2: [],
        importance3: [],
        name: undefined,
        sort: '-id'
      },
      importanceOptions: ['离职-随时到岗', '在职-月内到岗', '在职-考虑机会', '在职-暂不考虑'],
      importanceOptions2: ['专科', '本科', '硕士', '博士'],
      importanceOptions3: [],
      gridData: [{
        date: '2016-05-02',
        name: 'John Smith',
        address: 'No.1518,  Jinshajiang Road, Putuo District'
      }],
      options: [
        { value: '选项1', label: '黄金糕' }
      ],
      value: ''
    }
  },
  watch: {
    listQuery: {
      deep: true,
      handler() {
        this.fetchData()
      }
    }
  },
  mounted() {
    this.fetchData()
    window.onresize = () => {
      return (() => {
        this.setDialogWidth()
      })()
    }
  },
  created() {
    this.setDialogWidth()
  },
  methods: {
    setDialogWidth() {
      console.log(document.body.clientWidth)
      var val = document.body.clientWidth
      const def = 800 // 默认宽度
      if (val < def) {
        this.dialogWidth = '100%'
      } else {
        this.dialogWidth = def + 'px'
      }
    },
    // 简历弹框内方法
    handleDrag() {
      this.$refs.select.blur()
    },
    detail(datas) {
      console.log(datas)
      this.dialogTableVisible = true
    },
    getUserInfo() {
      getInfo(this.getToken).then(response2 => {
        console.log(response2)
      })
    },
    getList() {
      this.listLoading = true
      // 重新刷新列表数据
      fetchList(this.listQuery).then(datas => {
        // this.total = response.data.total
        this.importanceOptions3 = datas['major_list']
        const data_list = []
        datas['data'].forEach(function(item, index) {
          data_list.push({ ...item, id: index })
        })
        this.data_list = data_list
        this.listLoading = false
        console.log(data_list)
        // Just to simulate the time of the request
        // setTimeout(() => {
        //   this.listLoading = false
        // }, 1.5 * 1000)
      })
    },
    handleFilter() {
      console.log(this.listQuery)
      this.getList()
    },
    fetchData() {
      this.listLoading = true
      this.getList()
      this.listLoading = false
    },
    sortChange(data) {
      const { prop, order } = data
      if (prop === 'id') {
        this.sortByID(order)
      }
    },
    getSortClass: function(key) {
      const sort = this.listQuery.sort
      return sort === `+${key}` ? 'ascending' : 'descending'
    },
    sortByID(order) {
      if (order === 'ascending') {
        this.listQuery.sort = '+id'
      } else {
        this.listQuery.sort = '-id'
      }
      this.handleFilter()
    }
  }
}
</script>
<style>
.filter-container {
  padding-bottom: 10px;

.filter-item {
  display: inline-block;
  vertical-align: middle;
  margin-bottom: 10px;
}
}

/*.abow_dialog {*/
/*  min-width: 55%;*/
/*}*/
.el-dialog {
  min-width: 55%;
  margin: 0 auto !important;
  height: 60%;
  overflow: hidden;
.el-dialog__body {
  position: absolute;
  left: 0;
  top: 54px;
  bottom: 0;
  right: 0;
  padding: 0;
  z-index: 1;
  overflow: hidden;
  overflow-y: auto;
}
}
.el-dialog__body {
  overflow: auto;
  height: 100%;
}
.el-dialog {
  /*min-width: 21rem;*/
  min-width: 340px;
  top: 30px;
  min-height: 90%;
}
</style>
