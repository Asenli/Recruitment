import request from '@/utils/request'

export function save_data(data) {
  return request({
    url: '/userinfo',
    method: 'post',
    data
  })
}
