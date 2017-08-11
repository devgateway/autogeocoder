import { injectReducer } from '../../store/reducers'

export default (store) => ({
  path : 'docsList',
  /*  Async getComponent is only invoked when route matches   */
  getComponent (nextState, cb) {
    /*  Webpack - use 'require.ensure' to create a split point
        and embed an async module loader (jsonp) when bundling   */
    require.ensure([], (require) => {
      /*  Webpack - use require callback to define
          dependencies for bundling   */
      const Comp = require('./containers/docsContainer').default
      const reducer = require('./modules/docsModule').default

      /*  Add the reducer to the store on key 'counter'  */
      injectReducer(store, { key: 'docsqueue', reducer })

      /*  Return getComponent   */
      cb(null, Comp)

    /* Webpack named bundle   */
  }, 'docsList')
  }
})
