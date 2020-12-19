import { login, logout, getInfo } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'
import { resetRouter } from '@/router'

const getDefaultState = () => {
  return {
    token: getToken(),
    name: '',
    avatar: '',
    menus: ''
    // 新增菜单权限
  }
}

const state = getDefaultState()

const mutations = {
  RESET_STATE: (state) => {
    Object.assign(state, getDefaultState())
  },
  SET_TOKEN: (state, token) => {
    state.token = token
  },
  SET_NAME: (state, name) => {
    state.name = name
  },
  SET_AVATAR: (state, avatar) => {
    state.avatar = avatar
  },
  // 新增
  SET_MENUS: (state, menus) => {
    state.menus = menus
  }
}

const actions = {
  // user login
  login({ commit }, userInfo) {
    const { username, password } = userInfo
    return new Promise((resolve, reject) => {
      login({ username: username.trim(), password: password }).then(response => {
        const { data } = response
        commit('SET_TOKEN', data.token)
        setToken(data.token)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get user info
  getInfo({ commit, state }) {
    return new Promise((resolve, reject) => {
      getInfo(state.token).then(response => {
        const { data } = response

        if (!data) {
          return reject('Verification failed, please Login again.')
        }
        const { username, avatar } = data
        // 模拟请求数据
        const menus = [
          {
            'path': '/system',
            'redirect': '/menu',
            'component': 'Layout',
            'meta': {
              'title': '系统管理',
              'icon': 'form'
            },
            'children': [{
              'path': '/menu',
              'name': 'menu',
              'component': 'menu/index',
              'meta': {
                'title': '简历筛选',
                'icon': 'table'
              }
            },
            {
              'path': '/roles',
              'name': 'roles',
              'component': 'roles/index',
              'meta': {
                'title': '简历管理',
                'icon': 'table'
              }
            },
            {
              'path': '/administrator',
              'name': 'administrator',
              'component': 'dashboard/index',
              'meta': {
                'title': '用户管理',
                'icon': 'table'
              }
            }
            ]
          }

        ]
        // 如果需要404 页面，请在此处添加
        menus.push({
          path: '/404',
          component: '404',
          hidden: true
        }, {
          path: '*',
          redirect: '/404',
          hidden: true
        })
        commit('SET_NAME', username)
        commit('SET_AVATAR', avatar) // 角色
        commit('SET_MENUS', menus) // 触发vuex SET_MENUS 保存路由表到vuex
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user logout
  logout({ commit, state }) {
    return new Promise((resolve, reject) => {
      logout(state.token).then(() => {
        removeToken() // must remove  token  first
        resetRouter()
        commit('RESET_STATE')
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // remove token
  resetToken({ commit }) {
    return new Promise(resolve => {
      removeToken() // must remove  token  first
      commit('RESET_STATE')
      resolve()
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}

