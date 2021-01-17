import request from '@/utils/request'

// 获取用户简历信息
export function jian_info(user_id) {
  return request({
    url: '/jian',
    method: 'get',
    params: { user_id: user_id }
  })
}

// 保存简历信息
export function save_data(data) {
  return request({
    url: '/jian',
    method: 'post',
    data
  })
}

// 获取岗位信息
export function station_data() {
  return request({
    url: '/position',
    method: 'get'
  })
}

