<template>
    <div class='tech-container flex-row relative'>
        <div class='tech-wrapper' v-for="tech in techs" :key="tech.id">
            <div :class="tech.label"  class="relative"></div>
                <span class='tech-label'> {{ tech.name }} </span>
        </div>
    </div>
</template>
<script>

export default
{
    data()
    {
        return{
            techs:
            [
                {
                    id: 0,
                    name: 'HTML',
                    label: 'tech-UI'
                },
            ],
        };
    }

}
</script>