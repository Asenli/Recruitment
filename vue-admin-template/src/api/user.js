import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/userinfo',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/logout',
    method: 'post'
  })
}
export function subForm(data) {
  return request({
    url: '/register',
    method: 'post',
    data
  })
}

// export function userInfos() {
//   return request({
//     url: '/userinfo',
//     method: 'get'
//   })
// }
