<template>
  <div class="container">
    <ul class="sojob-list" style="width: 100%;">
      <li v-for="(data,i) in dataList" :key="i">
        <div class="flex-container">
          <div class="flex-item">
            <h3 class="div-h3">{{ data.name }}</h3>
            <p>
              <span style="color: #f60;">{{ data.salary }}</span> | <span>成都</span> |
              <span>{{ data.education }}</span> | <span>{{ data.experience }}</span> <span><el-button type="primary" round size="mini">立即沟通</el-button></span>
            </p>
            <p style="text-align: left"><span>{{ data.keyword }}</span>&#8194; &#8194;
              <span>{{ data.add_time }}</span></p>
          </div>
          <div class="company-info">
            <p><span>{{ data.company }}</span></p>
<!--            <p><span>建筑</span></p>-->
            <p class="temptation"><span>绩效奖金</span><span>岗位晋升</span><span>午餐补助</span></p>
          </div>
        </div>
      </li>
    </ul>
    <div id="box2" class="side">
      <el-carousel height="400px" direction="vertical" :autoplay="true">
        <el-carousel-item v-for="item in imageArry" :key="item">
          <img width="320" :src="item" class="rightImg">
        </el-carousel-item>
      </el-carousel>
      <el-carousel style="margin-top: 5px" :interval="3000" arrow="always" :autoplay="true">
        <el-carousel-item v-for="item in imageArry" :key="item">
          <img width="320" :src="item" class="rightImg">
        </el-carousel-item>
      </el-carousel>
    </div>
  </div>
</template>

<script>
import { station_data } from '../../api/jian'

export default {
  name: 'Index',
  data() {
    return {
      imageArry: [
        require('../../assets/ranjith-a.jpg'),
        require('../../assets/ranjith.jpg'),
        require('../../assets/vista.jpg')],
      dataList: []
    }
  },
  mounted() {
    this.getInfo()
  },
  methods: {
    getInfo() {
      return new Promise((resolve, reject) => {
        station_data().then(data => {
          this.dataList = data.data
          console.log(this.dataList)
        }).catch(error => {
          reject(error)
        })
      })
    }
  }
}
</script>

<style scoped>
.box {
  height: 100%;
  display: -webkit-flex;
  display: flex;
}

#box1 {
  width: 720px;
  -webkit-justify-content: space-around;
  justify-content: space-around;
  overflow-y: auto;
  height: 750px;
}

#box2 {
  width: 35%;
  -webkit-justify-content: space-around;
  justify-content: space-around;
}

.el-icon-edit {
  cursor: pointer;
  color: #00B38A;
  float: right;
}

.basic-info {
  text-align: left;
}

.container {
  display: flex;
  width: 980px;
  height: 85%;
  margin-right: auto;
  margin-left: auto;
}

.el-date-editor.el-input, .el-date-editor /deep/ .el-input__inner {
  width: 100%;
}

.el-radio.is-bordered + .el-radio /deep/ .is-bordered {
  margin-left: 0;
  margin-top: 5px;
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
}

.flex-container {
  display: -webkit-flex;
  display: flex;
  -webkit-justify-content: space-between;
  justify-content: space-between; /*外层元素属性设置为space-between*/
  width: 100%;
  height: 100px;
  /*background-color: lightgrey;*/
  /*padding: 14px 18px 14px 21px;*/
}

.flex-item {
  text-decoration: none;
  color: #666;
  float: left;
}

.company-info {
  float: right;
  padding: 0 5px 3px 20px;
  width: 230px;
  font-size: 14px;
  min-height: 90px;
  border-left: 1px dotted #8197a2;
  font-family: Microsoft Yahei;
}

.div-h3 {
  display: inline-block;
  line-height: 24px;
  margin: 0;
  padding-right: 70px;
  font-size: 18px;
  font-family: Microsoft Yahei;
  font-weight: 400;
  color: #3d9ccc;
  overflow: hidden;
  white-space: nowrap;
  -o-text-overflow: ellipsis;
  text-overflow: ellipsis;
}

.sojob-list li {
  position: relative;
  margin-top: 12px;
  border: 1px solid #e5e5e5;
  padding: 14px 18px 14px 21px;
}

.sojob-list {
  padding: 0;
  margin: 0;
  list-style: none;
}

.temptation {
  /*margin: 0 9px 0;*/
}

.temptation span {
  float: left;
  padding: 2px 10px;
  border: 1px solid #e1f2fa;
  margin-right: 6px;
  margin-bottom: 10px;
  font-size: 12px;
  background-color: #edf9ff;
  color: #3d9ccc;
}

.side {
  float: left;
  margin-left: 30px;
  width: 230px;
  overflow: hidden;
  _display: inline;
  margin-top: 12px;
  /*border: 1px solid #e5e5e5;*/
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;

}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}
</style>
