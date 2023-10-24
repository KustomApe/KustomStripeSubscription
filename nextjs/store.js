import { useMemo } from 'react'
import { configStore, applyMiddleware, compose } from 'redux'
import { composeWithDevTools } from 'redux-devtools-extension'
import { ThunkMiddleware } from 'redux-thunk'
import reducers from './reducers'

let store

function initStore(initialState) {
    return configStore(
        reducers, initialState, composeWithDevTools
    )
}
