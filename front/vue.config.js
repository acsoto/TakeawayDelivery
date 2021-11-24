module.exports = {
  outputDir: 'dist',
  assetsDir: 'static',
  publicPath: '/',
  devServer: {
    port: 8080,
    host: '0.0.0.0'
  },
  pwa: {
    iconPaths: {
      favicon32: 'favicon.ico',
      favicon16: 'favicon.ico',
      appleTouchIcon: 'favicon.ico',
      maskIcon: 'favicon.ico',
      msTileImage: 'favicon.ico'
    }
  }
}
