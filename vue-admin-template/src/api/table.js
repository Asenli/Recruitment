import request from '@/utils/request'

export function fetchList(params) {
  return request({
    url: '/all_user',
    method: 'get',
    params: { page: params['page'],
      limit: params['limit'],
      statu: params['importance'],
      education: params['importance2'],
      major: params['importance3'],
      name: params['name'],
      username: params['username'],
      sort: params['sort'] }
  })
}
