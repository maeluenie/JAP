<template>
<nuxt-link :to="'jobDetails/' + id"> 
    <div class = "job">
      <p>{{job}}</p>
    </div>
</nuxt-link>
  
</template>

<script>
export default {
    name: "Jobs",
    props: ["job","id"],
    
}

</script>

<style>

</style>