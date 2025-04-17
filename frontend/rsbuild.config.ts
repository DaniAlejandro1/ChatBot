import { defineConfig } from '@rsbuild/core';
import { pluginVue } from '@rsbuild/plugin-vue';
import path from 'path';

export default defineConfig({
   plugins: [pluginVue()],
   resolve: {
      alias: {
         '@': path.resolve(__dirname, './src'),
      },
   },
   module: {
      rules: [
         {
            test: /\.css$/,
            use: ['postcss-loader'],
            type: 'css',
         },
      ],
   },
});
