<template>

<section class="copy">
    <p>&copy; 2024 - {{date}}. All rights reserved. By <a href="/"><span>@krigjo25</span></a></p>
</section>

</template>

<script setup>


const date = new Date().getFullYear();

</script>