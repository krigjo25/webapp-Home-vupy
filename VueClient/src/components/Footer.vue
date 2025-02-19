<template>
    <footer>
        <div class="copy">
            <p>&copy; {{year}} <a href="">@krigjo25</a> </p>
        </div>

    </footer>
</template>

<script setup>

//  Importing components
//import Validator from './footer_components/Validator.vue';


const year = new Date().getFullYear();
</script>