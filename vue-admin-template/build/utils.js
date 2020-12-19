const px2remLoader = {
  loader: 'px2rem-loader',
  options: {
    remUnit: 37.5
  }
}


// generate loader string to be used with extract text plugin
function generateLoaders (loader, loaderOptions) {
  var loaders = [cssLoader,px2remLoader]
  if (loader) {
    loaders.push({
      loader: loader + '-loader',
      options: Object.assign({}, loaderOptions, {
        sourceMap: options.sourceMap
      })
    })
  }

  // Extract CSS when that option is specified
  // (which is the case during production build)
  if (options.extract) {
    return ExtractTextPlugin.extract({
      use: loaders,
      publicPath:'../../',
      fallback: 'vue-style-loader'
    })
  } else {
    return ['vue-style-loader'].concat(loaders)
  }
}
