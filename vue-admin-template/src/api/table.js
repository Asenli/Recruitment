import request from '@/utils/request'

export function fetchList(params) {
  return request({
    url: '/all_user',
    method: 'get',
    params: { params }
  })
}
