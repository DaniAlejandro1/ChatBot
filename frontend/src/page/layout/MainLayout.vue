<script setup lang="ts"></script>

<template>
   <!-- Aqui van los componentes relacionados al header -->
   <header class="h-[12%] w-full flex flex-row justify-between items-center">
      <slot name="header"></slot>
   </header>

   <!-- Aqui van los componentes relacionados al contenido principal -->
   <main class="size-full flex flex-col justify-evenly items-center px-3">
      <slot name="main"></slot>
   </main>

   <!-- Aqui van los componentes relacionados al footer -->
   <footer class="h-[12%] w-full flex flex-row justify-between items-center gap-4">
      <slot name="footer"></slot>
   </footer>
</template>
