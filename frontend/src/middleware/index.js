import thunk from "redux-thunk"
import logger from "./logger"
import { applyMiddleware } from "redux"
import { loadingBarMiddleware } from 'react-redux-loading-bar'


export default [
    thunk,
    loadingBarMiddleware,
    logger
]

// export default applyMiddleware(
//     thunk,
//     loadingBarMiddleware,
//     logger,
// )
