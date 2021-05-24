<template>
    <BlogHeader/>
    <ArticleList/>
    <BlogFooter/>
</template>

<script>
    import BlogHeader from "../components/BlogHeader";
    import ArticleList from "../components/ArticleList";
    import BlogFooter from "../components/BlogFooter";

    export default {
        name: "Home",
        components: {ArticleList, BlogFooter, BlogHeader}
    }
</script>

<style scoped>

</style>