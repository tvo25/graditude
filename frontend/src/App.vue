<template>
    <div id="app">
        <router-view/>
    </div>
</template>

<script>

    export default {
        name: 'App',
    };
</script>

<style>
    @import url("https://fonts.googleapis.com/css?family=Lato&display=swap");
    @import url("https://fonts.googleapis.com/css?family=Raleway:300&display=swap");

    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    th,
    label {
        font-family: "Raleway", sans-serif;
    }

    p,
    td {
        font-family: "Lato", sans-serif;
    }
</style>
