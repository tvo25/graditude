<template>
    <v-app>
        <v-content>
          <JobsTable></JobsTable>
        </v-content>
    </v-app>
</template>

<script>
    import JobsTable from './components/JobsTable';

    export default {
        name: 'App',
        components: {
            JobsTable: JobsTable
        },
    };
</script>
