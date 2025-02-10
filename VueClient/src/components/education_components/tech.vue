<template>
    <div class='tech-container flex-row relative'>
        <div class='tech-wrapper' v-for="tech in language" :key="tech.id">
            <div :class="'tech-' + tech.name"  class="relative"></div>
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
            language:
            [
                {
                    id: 0,
                    name: 'HTML',
                },
                {
                    id: 1,
                    name: 'Python',
                },
                {
                    id: 2,
                    name: 'CS',
                },
            ],
            labels:
            [
                {
                    id: 0,
                    name: 'MVC',
                },
                {
                    id: 1,
                    name: 'Python',
                },
                {
                    id: 2,
                    name: 'CS',
                },
            ]

        };
    }

}
</script>