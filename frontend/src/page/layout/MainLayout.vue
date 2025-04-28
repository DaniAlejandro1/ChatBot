<script setup lang="ts"></script>

<template>
   <!-- Aqui van los componentes relacionados al header -->
   <header class="h-[12%] z-10 w-full flex flex-row justify-between items-center px-0">
      <slot name="header"></slot>
   </header>

   <!-- Aqui van los componentes relacionados al contenido principal -->
   <main class="h-[76%]  z-0 w-full flex flex-col justify-evenly items-center px-0">
      <slot name="main"></slot>
   </main>

   <!-- Aqui van los componentes relacionados al footer -->
   <footer
      class="h-[12%] w-full z-0 flex flex-row justify-between items-center gap-4 px-0 relative"
   >
      <slot name="footer"></slot>
   </footer>
</template>
