import { login, logout, getInfo } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'
import { resetRouter } from '@/router'

const getDefaultState = () => {
  return {
    token: getToken(),
    name: '',
    avatar: '',
    roles: '',
    menus: '',
    // 新增菜单权限
    user_id: ''
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
  SET_ROLES: (state, roles) => {
    state.roles = roles
  },
  SET_AVATAR: (state, avatar) => {
    state.avatar = avatar
  },
  // 新增
  SET_MENUS: (state, menus) => {
    state.menus = menus
  },
  // user id
  SET_USER_ID: (state, id) => {
    state.user_id = id
  }
}

const actions = {
  // user login
  login({ commit }, userInfo) {
    this.loading = true
    const { username, password } = userInfo
    return new Promise((resolve, reject) => {
      login({ username: username.trim(), password: password }).then(response => {
        console.log('登录')
        if (response.statu === true) {
          const { data } = response
          commit('SET_TOKEN', data.token)
          localStorage.setItem('user_id', data.id)
          commit('SET_USER_ID', data.id)
          setToken(data.token)
          resolve()
          this.loading = false
          // 登录就跳转固定页面
          this.$router.push('/dashboard')
        } else {
          console.log('登录111')
          alert(response.msg)
          this.loading = false
        }
      }).catch(error => {
        reject(error)
        this.loading = false
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
        const { menus, roles, username, avatar } = data
        if (!roles || roles.length <= 0) {
          reject('getInfo: roles must be a non-null array!')
        }
        // 如果需要404 页面，请在此处添加
        // menus.push({
        //   path: '/404',
        //   component: '404',
        //   hidden: true
        // }, {
        //   path: '*',
        //   redirect: '/404',
        //   hidden: true
        // })
        commit('SET_ROLES', roles)
        commit('SET_NAME', username)
        commit('SET_AVATAR', avatar) // 角色
        // debugger  获取菜单列表
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

