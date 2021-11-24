module.exports = {
  presets: ['@vue/cli-plugin-babel/preset'],
  plugins: [
    [
      'import',
      {
        libraryName: 'Antd',
        libraryDirectory: 'lib',
        style: true
      }
    ]
  ]
}
