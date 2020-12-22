import request from '@/utils/request'

export function save_data(data) {
  return request({
    url: '/userinfo',
    method: 'post',
    data
  })
}

export function station_data() {
  return request({
    url: '/position',
    method: 'get'
  })
}
