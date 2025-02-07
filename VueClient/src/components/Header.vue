<template>
    <a href='/'>
        <div class="align-items-flex-end-row justify-flexstart-row padding">
            <Logo />
        </div>
    </a>
</template>

<script>
    import Logo from './header_components/Logo.vue'
    export default {
        name: 'Header',
        components: 
        {
            Logo
        },
    };
</script>