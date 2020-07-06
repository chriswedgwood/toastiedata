var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  mode: 'development',
  entry: {
    toastieData: './toastiedata/static/js/toastieData.js',
     }

  ,
  output: {
    path: path.resolve('./toastiedata/static/bundles/'),
    filename: "[name]-[hash].js",
  },

  plugins: [
    new BundleTracker({
      filename: './webpack-stats.json'
    }),
  ],
  module: {
    rules: [{
      test: /\.js$/,
      exclude: /node_modules/,
      loader: 'babel-loader',
      options: {
        presets: ['@babel/preset-env',
          '@babel/react', {
            'plugins': ['@babel/plugin-proposal-class-properties']
          }
        ]
      }
    },
    {
      test: /\.(png|jpg|gif)$/,
      use: [
        {
          loader: 'file-loader',
          options: {
            name: '[name].[ext]',
            outputPath: 'images/'
          }
        }
      ]
    },]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx']
  },



};
