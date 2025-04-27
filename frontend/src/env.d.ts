/// <reference types="@rsbuild/core/types" />

declare module '*.vue' {
   import type { DefineComponent } from 'vue';

   // biome-ignore lint/complexity/noBannedTypes: reason
   // eslint-disable-next-line @typescript-eslint/no-empty-object-type, @typescript-eslint/no-explicit-any
   const component: DefineComponent<{}, {}, any>;
   export default component;
}

declare module '*.png' {
   const value: string;
   export default value;
}
