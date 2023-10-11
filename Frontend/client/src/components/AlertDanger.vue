<template>
    <div>
        <div class="alert alert-danger" role="alert">{{ message }}</div>
        <br/>
    </div>
</template>

<script>
    export default{
        props: ['message'],
    };
</script>