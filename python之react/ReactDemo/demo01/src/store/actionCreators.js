import {CHANGE_INPUT, ADD_ITEM, DELETE_ITEM, GET_LIST } from './actionTypes'
import axios from 'axios'


export const changeInputAction = (value) => ({
  type: CHANGE_INPUT,
  value
})

export const addItemAction = () => ({
  type: ADD_ITEM,
})


export const deleteItemAction = (index) => ({
  type: DELETE_ITEM,
  index
})


export const getListAction = (data) => ({
  type: GET_LIST,
  data
})


export const getTodoList = ()=>{
  return (dispatch)=>{
    axios.get('http://basedbproduct.noscan.sparta.html5.qq.com/user/rolelist')
    .then((res)=>{
      const data = res.data.data
      const action = getListAction(data)
      dispatch(action)
    })
    .catch((err)=>{
      console.log(err);
    })
  }
}
