<template>
    <div class="TextAnime">
        <span
            v-for="(t,index) in app_name"
            :key="index"
            class="item"
            :style="{animationDelay: index*150+'ms'}"
            v-text="t">
        </span>
    </div>
</template>

<script>
export default{
    props: ['app_name']
}
</script>

<style scoped>
@keyframes text-in {
  0% {
    transform: translate(0, -20px);
    opacity: 0;
  }
}
.item {
  display: inline-block;
  min-width: 0.3em;
  font-size: 2rem;
  animation: text-in .8s cubic-bezier(0.22, 0.15, 0.25, 1.43) 0s backwards;
}
</style>