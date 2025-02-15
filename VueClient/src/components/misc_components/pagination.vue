<template>
    <nav>
        <button :disabled=" current < 2" @click="current--">Previous</button>
        <span> {{ current }} / {{ total }}</span>
        <button :disabled="current === total" @click="current++">Next</button>
    </nav>
</template>

<script>

import { ref, watch, reactive } from 'vue';
const total = ref(1);
const current = ref(1);

export default
{
    props: 
    {
        data: 
        {
            type: Number,
            required: true
        }
    },
    emit: ['update'],
    setup(props, { emit }) 
    {
        //  Watch for changes in the 'data' prop
        watch(() => props.data, (newValue) => {
            total.value = newValue;
        }, { immediate: true });

        // Watch for changes in the 'current' prop
        watch(() => current.value, (newValue) => {
            emit('update', newValue);
        });

        return { current, total };
    },
}
</script>