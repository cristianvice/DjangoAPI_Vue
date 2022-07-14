module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset'
  ],
},

{
  test: /\.(js|mjs|jsx|ts|tsx)$/,
  exclude: /node_modules/,
  use: {
    loader: 'babel-loader',
    options: {
      plugins: ['@babel/plugin-syntax-top-level-await'],
    }
  }
}



