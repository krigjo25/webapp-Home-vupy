<template>
    <nav>
        <button :disabled=" current < 2" @click="current--">Previous</button>
        <span v-if="current > 0"> {{ current }} / {{ total }}</span>
        <button :disabled="current === total" @click="current++">Next</button>
    </nav>
</template>

<script setup>

//  Importing dependencies
import { ref, watch, defineProps, defineEmits } from 'vue';

//  Initializing reactive objects
const total = ref(1);
const current = ref(1);

const emit = defineEmits(['update']);
const props = defineProps(
{
    data: 
    {
        type: Number,
        required: true
    }
});

//  Watch for changes in the 'data' prop
watch(() => props.data, (newValue) => 
        {
            total.value = newValue;
        }, 
        { immediate: true });

// Watch for changes in the 'current' prop
watch(() => current.value, (newValue) => 
        {
            emit('update', newValue);
        });

</script>